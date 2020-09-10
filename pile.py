
# Création de pile #
def cree_pile(n):
    return[1]+[None]*n


def empiler(p, x):
    if(not is_full(p)):
        p[p[0]]=x; p[0]+=1
    return p

def depiler(p):
    if(not is_empty(p)):
        p[p[0]-1]=None; p[0]-=1
    return p

def is_empty(p): return p[0]==1 #Vérification de si la pile n'est pas vide #
def is_full(p): return p[-1]!=None





#-----------------------------------------------------------------------------------------------------#











#Différentes erreurs #
if __name__ == "__main__": # Exécution caché #
    error = "Pile obsolète !"
    pile = cree_pile(2) # Création 2 piles pour test et bug #
    assert pile==[1,None,None],error+"pile.cree_pile(n) résultat faux"
    empiler(pile, "test")
    assert pile==[2,"test",None],error+"pile.empiler(p,x) résultat faux"
    depiler(pile)
    assert pile==[1,None,None],error+"pile.depiler(p) résultat faux"

print(pile)
        