f = 'E:/mid/mid-term/ANM/00 - Numerical Methods Index.md'
c = open(f, 'r').read()
c = c.replace('NM --> PRF["5. Polynomial Solvers"]', 'NM --> PRF["5. Polynomial Solvers"]\n    NM --> INT["6. Interpolation & Curve Fitting"]')
open(f, 'w').write(c)
print('Mermaid updated')
