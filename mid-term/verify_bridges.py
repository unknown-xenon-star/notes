"""
Pure-Python verification of MI bridge balance equations (v2).
Branch-impedance aware. Convention: A(top) B(left) C(bottom) D(right);
source A-C, detector B-D unless stated. Balance <=> V_B - V_D = 0.
Anderson uses the classic 5-node form with detector B-E.
"""
import cmath

def gauss_solve(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[piv][c]) < 1e-15:
            raise ValueError("singular")
        M[c], M[piv] = M[piv], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                for k in range(c, n + 1):
                    M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]

def solve(elements, nodes, det_pair, w=1000.0, Va=1.0):
    """elements: list of (nodeA, nodeB, impedance Z). det_pair: (n1, n2)."""
    idx = {n: i for i, n in enumerate(nodes)}
    n = len(nodes)
    Y = [[0j] * n for _ in range(n)]
    for a, bb, Z in elements:
        y = 1.0 / Z
        ia, ib = idx[a], idx[bb]
        Y[ia][ia] += y; Y[ib][ib] += y
        Y[ia][ib] -= y; Y[ib][ia] -= y
    I = [0j] * n
    Y[idx['A']] = [0j] * n; Y[idx['A']][idx['A']] = 1; I[idx['A']] = Va
    Y[idx['C']] = [0j] * n; Y[idx['C']][idx['C']] = 1
    V = gauss_solve(Y, I)
    return V[idx[det_pair[0]]] - V[idx[det_pair[1]]]

def Zser(w, *els):
    """series R/L/C: elements as ('R',v)|('L',v)|('C',v)"""
    Z = 0j
    for k, v in els:
        if k == 'R': Z += complex(v)
        elif k == 'L': Z += 1j * w * v
        elif k == 'C': Z += 1 / (1j * w * v)
    return Z

def Zpar(w, *els):
    """parallel R/L/C"""
    Y = 0j
    for k, v in els:
        if k == 'R': Y += 1 / complex(v)
        elif k == 'L': Y += 1 / (1j * w * v)
        elif k == 'C': Y += 1j * w * v
    return 1 / Y

PASS = True
def check(name, dv, expect_zero=True):
    global PASS
    ok = (abs(dv) < 1e-9) if expect_zero else (abs(dv) > 1e-9)
    PASS &= ok
    print(f"{'PASS' if ok else 'FAIL'} | {name:62s} | {dv:.2e}")

w = 1000.0
D = ('B', 'D')

# 1. Wheatstone
check("Wheatstone balanced",
      solve([('A','B',complex(10)),('B','C',complex(100)),('A','D',complex(47.2)),('D','C',complex(472))], ['A','B','C','D'], D))
check("Wheatstone unbalanced control",
      solve([('A','B',complex(10)),('B','C',complex(100)),('A','D',complex(47.2)),('D','C',complex(500))], ['A','B','C','D'], D), False)

# 2. Maxwell inductance bridge: Z1=R1, Z2=R2, Z3=R3+jwL3 (series), Z4=Rx+jwLx
R1,R2,R3,L3 = 1000.0, 2000.0, 500.0, 0.08
Rx, Lx = R2*R3/R1, R2*L3/R1
check("Maxwell L bridge balanced (Rx=R2R3/R1, Lx=R2L3/R1)",
      solve([('A','B',complex(R1)),('B','C',complex(R2)),
             ('A','D',Zser(w,('R',R3),('L',L3))),('D','C',Zser(w,('R',Rx),('L',Lx)))], ['A','B','C','D'], D))
check("Maxwell L bridge unbalanced control",
      solve([('A','B',complex(R1)),('B','C',complex(R2)),
             ('A','D',Zser(w,('R',R3),('L',L3))),('D','C',Zser(w,('R',Rx),('L',Lx*1.01)))], ['A','B','C','D'], D), False)

# 3. Maxwell LC bridge: Z1=R1||C1, Z2=R2, Z3=R3, Z4=Rx+jwLx
R1,R2,R3,C1 = 500.0, 1000.0, 200.0, 1e-6
Lx, Rx = R2*R3*C1, R2*R3/R1
check("Maxwell LC bridge balanced (Lx=R2R3C1, Rx=R2R3/R1)",
      solve([('A','B',Zpar(w,('R',R1),('C',C1))),('B','C',complex(R2)),
             ('A','D',complex(R3)),('D','C',Zser(w,('R',Rx),('L',Lx)))], ['A','B','C','D'], D))
check("Maxwell LC unbalanced control",
      solve([('A','B',Zpar(w,('R',R1),('C',C1))),('B','C',complex(R2)),
             ('A','D',complex(R3)),('D','C',Zser(w,('R',100.0),('L',Lx)))], ['A','B','C','D'], D), False)

# 4. Hay bridge: Z1=R1 + 1/jwC1 series
R1,R2,R3,C1 = 1000.0, 2000.0, 500.0, 0.5e-6
den = 1 + (w*R1*C1)**2
Lx = R2*R3*C1/den
Rx = w**2 * R1*R2*R3*C1**2/den
check("Hay bridge balanced (den=1+w^2R1^2C1^2)",
      solve([('A','B',Zser(w,('R',R1),('C',C1))),('B','C',complex(R2)),
             ('A','D',complex(R3)),('D','C',Zser(w,('R',Rx),('L',Lx)))], ['A','B','C','D'], D))
check("Hay unbalanced control (Maxwell formula misuse)",
      solve([('A','B',Zser(w,('R',R1),('C',C1))),('B','C',complex(R2)),
             ('A','D',complex(R3)),('D','C',Zser(w,('R',R2*R3/R1),('L',R2*R3*C1)))], ['A','B','C','D'], D), False)

# 5. Anderson bridge: A-B unknown (R1+jwL1); A-D=R2; B-C=R3; D-C=R4; D-E=r; E-C=C.
#    Detector B-E.  Expect: R1 = R2R3/R4 ; L1 = (R3/R4)[R2R4 + r(R2+R4)]C
def anderson_dv(R1,L1,R2,R3,R4,r,C,w=1000.0):
    return solve([('A','B',Zser(w,('R',R1),('L',L1))),('A','D',complex(R2)),
                  ('B','C',complex(R3)),('D','C',complex(R4)),
                  ('D','E',complex(r)),('E','C',Zser(w,('C',C)))],
                 ['A','B','C','D','E'], ('B','E'), w)
R2,R3,R4,r,C = 2000.0, 500.0, 1000.0, 100.0, 2e-6
R1 = R2*R3/R4          # 1000 ohm
L1 = (R3/R4)*(R2*R4 + r*(R2+R4))*C
check("Anderson balanced (R1=R2R3/R4, L1=(R3/R4)[R2R4+r(R2+R4)]C)",
      anderson_dv(R1, L1, R2, R3, R4, r, C))
check("Anderson unbalanced control",
      anderson_dv(R1, L1*1.05, R2, R3, R4, r, C), False)
# cross-check L1 by numeric bisection with R1 fixed
lo, hi = 1e-9, 50.0
flo = anderson_dv(R1, lo, R2,R3,R4,r,C).real
fhi = anderson_dv(R1, hi, R2,R3,R4,r,C).real
for _ in range(300):
    mid = 0.5*(lo+hi); fm = anderson_dv(R1, mid, R2,R3,R4,r,C).real
    if (flo < 0) == (fm < 0): lo, flo = mid, fm
    else: hi = mid
Lx_num = 0.5*(lo+hi)
m = abs(Lx_num - L1) < 1e-9
PASS &= m
print(f"{'PASS' if m else 'FAIL'} | Anderson L1 formula vs numeric null: formula={L1:.8f} numeric={Lx_num:.8f}")

# 6. De Sauty: Z1=R1, Z2=R2, Z3=C3, Z4=Cx -> Cx = C3*R1/R2
R1,R2,C3 = 1000.0, 2000.0, 0.1e-6
Cx = C3*R1/R2
check("De Sauty balanced (Cx = C3 R1/R2)",
      solve([('A','B',complex(R1)),('B','C',complex(R2)),
             ('A','D',Zser(w,('C',C3))),('D','C',Zser(w,('C',Cx)))], ['A','B','C','D'], D))
# imperfect capacitors: balance only when D_x = D_3  (equal dissipation factors)
r3, rx = 50.0, 100.0   # choose rx so that w*Cx*rx == w*C3*r3 -> rx = C3*r3/Cx
rx = C3*r3/Cx
check("De Sauty imperfect caps balance when Dx=D3",
      solve([('A','B',complex(R1)),('B','C',complex(R2)),
             ('A','D',Zser(w,('R',r3),('C',C3))),('D','C',Zser(w,('R',rx),('C',Cx)))], ['A','B','C','D'], D))
check("De Sauty imperfect caps fail when Dx!=D3",
      solve([('A','B',complex(R1)),('B','C',complex(R2)),
             ('A','D',Zser(w,('R',r3),('C',C3))),('D','C',Zser(w,('R',2*rx),('C',Cx)))], ['A','B','C','D'], D), False)

# 7. Schering: Z1=R1||C1, Z2=R2, Z3=C3 (lossless std), Z4=Cx series Rx
#    Cx = C3 R1/R2 ; Rx = R2 C1/C3 ; tan delta = w R1 C1
R1,C1,R2,C3 = 1000.0, 0.5e-6, 500.0, 0.2e-6
Cx = C3*R1/R2
Rx = R2*C1/C3
check("Schering balanced (Cx=C3R1/R2, Rx=R2C1/C3)",
      solve([('A','B',Zpar(w,('R',R1),('C',C1))),('B','C',complex(R2)),
             ('A','D',Zser(w,('C',C3))),('D','C',Zser(w,('R',Rx),('C',Cx)))], ['A','B','C','D'], D))
check("Schering unbalanced control",
      solve([('A','B',Zpar(w,('R',R1),('C',C1))),('B','C',complex(R2)),
             ('A','D',Zser(w,('C',C3))),('D','C',Zser(w,('R',Rx*1.1),('C',Cx)))], ['A','B','C','D'], D), False)
print(f"       tan-delta identity: w*R1*C1 = {w*R1*C1:.6f} ; w*Rx*Cx = {w*Rx*Cx:.6f} (must be equal)")
PASS &= abs(w*R1*C1 - w*Rx*Cx) < 1e-12

# 8. Kelvin double bridge (CLASSIC Golding topology):
#    Left chain: A -> Rx -> L1 -> r(yoke) -> L2 -> Rs -> C   (low-resistance loop)
#    Outer divider: A -> P -> B -> Q -> C     (battery A-C)
#    Inner divider: L1 -> p -> E, L2 -> q -> E (bridges the link ends)
#    Detector: B-E.  Candidate balance: Rx = (P/Q)Rs + k*r*(P/Q - p/q)
def kelvin_dv(Rx,Rs,P,Q,p,q,r,w=1000.0):
    return solve([('A','L1',complex(Rx)),('L1','L2',complex(r)),('L2','C',complex(Rs)),
                  ('A','B',complex(P)),('B','C',complex(Q)),
                  ('L1','E',complex(p)),('L2','E',complex(q))],
                 ['A','B','C','L1','L2','E'], ('B','E'))
# (a) equal ratios: correction vanishes; Rx = (P/Q)Rs
check("Kelvin balanced P/Q=p/q=1", kelvin_dv(0.005, 0.005, 100, 100, 100, 100, 0.002))
# (b) ratio arms P/Q=10, p/q=15 (differ) -> correction term active
P,Q,p,q,r,Rs = 1000.0, 100.0, 150.0, 10.0, 0.5, 0.001
Rx_base = (P/Q)*Rs
# numeric truth by bisection on Rx
for probe in [1e-9, 0.005, 0.01, 0.02, 0.05, 0.1, 0.5]:
    print(f"   probe Rx={probe:<7.4f} -> residual real = {kelvin_dv(probe,Rs,P,Q,p,q,r).real:+.6e}")
lo, hi = 1e-6, 1.0
flo = kelvin_dv(lo,Rs,P,Q,p,q,r).real
fhi = kelvin_dv(hi,Rs,P,Q,p,q,r).real
for _ in range(300):
    mid = 0.5*(lo+hi); fm = kelvin_dv(mid,Rs,P,Q,p,q,r).real
    if (flo < 0) == (fm < 0): lo, flo = mid, fm
    else: hi = mid
Rx_num = 0.5*(lo+hi)
corr = Rx_num - Rx_base
print(f"Kelvin: numeric Rx = {Rx_num:.10f} ohm (base (P/Q)Rs = {Rx_base:.6f}, correction = {corr:+.8f})")
# candidate correction forms
expected_sign = (P/Q - p/q)   # = -5
for nm, val in {
    "q*r/(p+q+r) * (P/Q - p/q)": q*r/(p+q+r)*(P/Q - p/q),
    "p*r/(p+q+r) * (P/Q - p/q)": p*r/(p+q+r)*(P/Q - p/q),
    "q*r/(p+q+r) * (p/q - P/Q)": -q*r/(p+q+r)*(P/Q - p/q),
    "r/(p+q+r) * (Q*p - P*q)/Q": r/(p+q+r)*(Q*p - P*q)/Q,
}.items():
    m = abs(val - corr) < 1e-9
    PASS &= m
    print(f"   {'MATCH' if m else 'no   '} | correction {nm:34s} = {val:+.8f}")
# (c) p/q = P/Q kills the correction even with big yoke r
P,Q,p,q,r,Rs = 1000.0, 100.0, 200.0, 20.0, 0.5, 0.001
check("Kelvin correction vanishes when p/q=P/Q", kelvin_dv((P/Q)*Rs, Rs, P, Q, p, q, r))

print()
print("ALL PASS:", PASS)
