# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 01:43:49 2022

@author: chant
"""


from Simplex import Tableau

if __name__ == '__main__':
    """
    max Z=11*x1+16*x2+15*x3
    Z -11*x1-16*x2-15*x3=0
    
    contraintes
    X1+x2+x3<=12 000
    (2/3)*x1+(2/3)*x2+x3 <=4 600
    (1/2)*x1+ (1/3)*x2+ (1/2)*x3 <=2 400
    x1,x2,x3 >= 0
    """
    t = Tableau([-11,-16,-15])
    t.add_constraint([1, 2, (3/2)], 12000)
    t.add_constraint([(2/3), (2/3), 1], 4600)
    t.add_constraint([(1/2), (1/3), (1/2)], 2400)
    t.solve()