import numpy as np
from IPython.display import Math

class Pol3:
    
    def __init__(self):
        self.coefs = [0]
        
    def add_term(self, c, e):
        s=len(self.coefs)
        if s<=e:
            while s<e+1:
                self.coefs=self.coefs+[0]
                s+=1
            self.coefs[e]=self.coefs[e]+c    
        else :
            self.coefs[e]=self.coefs[e]+c
        return self

    def show(self):
        s = "+".join(["%s^{%s}"%(str(c) if e==0 else str(c)+"x" if c!=1 else "x", str(e) if e not in [0,1] else "") for e,c in enumerate(self.coefs) if c!=0])
        s = s.replace("+-", "-")
        return Math(s)
    