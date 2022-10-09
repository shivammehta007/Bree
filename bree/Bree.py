
import benepar
import spacy

# class Token:

#     def __init__(self, obj) -> None:
#         self.obj = obj
        
#     def __repr__(self) -> str:
#         return f"{self.obj.text}, {self.obj.id}"
    
#     def __str__(self) -> str:
#         return f"{self.obj.text}, {self.obj.id}"
    
#     def __eq__(self, __o: object) -> bool:
#         return self.obj.text == __o.obj.text and self.obj.id == __o.obj.id
    
    
class Node:

    def __init__(self, val, babies=[], parent=None) -> None:
        self.val = val
        self.babies = babies
        self.parent = None
 

    def __eq__(self, __o: object) -> bool:
        return self.val == __o.val
    
    def __hash__(self) -> int:
        return hash(self.val)
    
    def __repr__(self) -> str:
        return self.val.obj.text
    
    def __str__(self) -> str:
        return self.val.obj.text
    
    def return_matching_baby(self, token):
        for baby in self.babies:
            if baby.val == token:
                return baby
        return None
    

class Bree:

    def __init__(self, root) -> None:
        self.root = root
    
    
    def push(self, constituent, garbage=set(['PUNCT', 'DET', 'CCONJ'])) -> None:
        if len(constituent) == 1:
            return 

        for token in constituent:
            if token.pos_ in garbage:
                continue

            new_node  = Node(token)
            current_node = self.root
            while(current_node and new_node != current_node):
                
            


        
        
        pass
