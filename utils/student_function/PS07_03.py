import PS07
class BTNode(PS07.BTNode):
    
    def height(self):
        alturaIzquierda=0;alturaDerecha=0
        if((self.left is None) and (self.right is None)):return 0
        if self.left is not None:
            alturaIzquierda=self.left.height()+1
        if self.right is not None:
            alturaDerecha=self.right.height()+1
        if alturaIzquierda>alturaDerecha:return alturaIzquierda
        else: return alturaDerecha
    
    def balance_factor(self):
        a=0;b=0
        if self.left is not None:
            a=self.left.height()+1
        if self.right is not None:
            b=self.right.height()+1
        result=(a-b)
        return result
    
    def balance_factor_tree(self):
        r = self.__class__(self.balance_factor(), \
                           left=self.left.balance_factor_tree() if self.left is not None else None,
                           right=self.right.balance_factor_tree() if self.right is not None else None,
                          )
        return r
    
    def rotate_right(self):
        
        p=self.clone()
        q=self.left.clone()
        a=p.balance_factor()
        b=q.balance_factor()
        assert a==2 ,"Nelson p"
        assert b==1 , "Nelson q"
        p.left=q.right
        q.right=p
        return q
    
    def rotate_left(self):
        p=self.clone()
        q=self.right.clone()
        a=p.balance_factor()
        b=q.balance_factor()
        assert a==-2 ,"Nelson p"
        assert b==-1 , "Nelson q"
        p.right=q.left
        q.left=p
        return q
        