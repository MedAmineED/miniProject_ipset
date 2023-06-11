from numpy import array, empty

tab = empty(100, dtype=dict)

def saisir():
    n = int(input("saisir le nombre des articles"))
    while(n <= 0 or n > 100):
        n = int(input("choisir un nombre compris entre 0 et 100 pour fixer le nombre des articles"))
    return n

def remplir(n):
    for i in range(0, n):
        tab[i] = {}
        tab[i]["ref"] = input("choisir la reference de votre article --: ")
        tab[i]["nom"] = input("choisir le nom de votre article --: ")
        tab[i]["cat"] = input("choisir la categorie de votre article --: ")
        tab[i]["achat"] = int(input("choisir le prix d'achat de votre article --: "))
        tab[i]["vente"] = int(input("choisir le prix de vente de votre article --: "))
        print("-----------------------------------------")
    return tab

def trie(n, direction, prop):
    
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            condition = False
            if(direction == 1):
                condition = tab[i][prop] < tab[j][prop]
            else :
                condition = tab[i][prop] > tab[j][prop]
            if(condition):
                box = tab[i]
                tab[i] = tab[j]
                tab[j] = box
    return tab

def recherche(n) :
    print("Si vous souhaitez rechercher en fonction de reference: taper 'ref'")
    print("Si vous souhaitez rechercher en fonction de nom: taper 'nom'")
    print("Si vous souhaitez rechercher en fonction de categorie: taper 'cat'")
    print("Si vous souhaitez rechercher en fonction de prix d'achat: taper 'achat'")
    print("Si vous souhaitez rechercher en fonction de vente: taper 'vente'")
    print("pour exiter le programme taper 'EXIT'")
    print("######################################")
    
    rechercheAction = input("choisissez le type de recherche : ")
    while not(rechercheAction == "ref" or rechercheAction == "nom" or rechercheAction == "cat" or rechercheAction == "achat" or rechercheAction == "vente"):
        rechercheAction = input("cette caracteristique n'existe pas retaper le type de recherche : ")
    print("-----------------------------------------")
    
    rech = input("Choisissez le  " + rechercheAction + " de produits que vous souhaitez afficher : ")
    for i in range(0, n):
        if(tab[i][rechercheAction] == rech):
            print(tab[i]["ref"])
            print(tab[i]["nom"])
            print(tab[i]["cat"])
            print(tab[i]["achat"])
            print(tab[i]["vente"])
            print("-----------------------------------------")
            
            

def afficher(n, tab):
    for i in range(0, n):
        print("-----------------------------------------")
        print(tab[i]["ref"])
        print(tab[i]["nom"])
        print(tab[i]["cat"])
        print(tab[i]["achat"])
        print(tab[i]["vente"])
        print("-----------------------------------------")


n = saisir()
tab = remplir(n)

exit = False

while(exit == False):
    print("pour afficher tout les produits taper AF")
    print("pour trier le produit croissant taper CR")
    print("pour trier le produit decroissant taper DCR")
    print("pour chercher dans les produits taper CHR")
    print("pour exit le programme taper Exit")
    print("-----------------------------------------")
    
    action = input("choisissez votre action : ")
    while not(action == "AF" or action == "CR" or action == "DCR" or action == "CHR" or action == "EXIT"):
        action = input("SLV !!, choisissez une action valide : ")
    print("######################################")
    
    if(action == "AF"):
        afficher(n, tab)
        
    elif (action == "CR"):
        print("pour trie en fonction de prix d'achat taper 'achat'")
        print("pour trie en fonction de prix de vente taper 'vente'")
        tr = input("taper 'achat' ou 'vente' --: ")
        
        while not(tr == "vente" or tr == "achat"):
            tr = input("cette action n'est pas valide!!! taper une action valide ('achat' ou 'vente') --: ")
        tab = trie(n, 1, tr)
        afficher(n, tab)
        
    elif (action == "DCR"):
        print("pour trie en fonction de prix d'achat taper 'achat'")
        print("pour trie en fonction de prix de vente taper 'vente'")
        tr = input("taper 'achat' ou 'vente' --: ")
        
        while not(tr == "vente" or tr == "achat"):
            tr = input("cette action n'est pas valide!!! taper une action valide ('achat' ou 'vente') --: ")
        tab = trie(n, -1, tr)
        afficher(n, tab)
        
    if(action == "CHR"):
        recherche(n)
        print("-----------------------------------------")
        
    if(action == "EXIT"):
        exit = True
            
    

        
