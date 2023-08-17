import datetime

tab = []

def saisir():
    n = int(input("saisir le nombre des articles"))
    while(n <= 0 or n > 100):
        n = int(input("choisir un nombre compris entre 0 et 100 pour fixer le nombre des articles"))
    return n




def remplir(n):
    for i in range(0, n):
        produit = {}
        produit["ref"] = input("--- Entrez la référence de votre article --: ")
        produit["nom"] = input("--- Entrez le nom de votre article --: ")
        produit["cat"] = input("--- Choisissez la catégorie de votre article --: ")
        produit["prix"] = int(input("--- Entrez le prix de votre article --: "))
        tab.append(produit)
        print("-----------------------------------------")
    return tab 



def supprimer(tab):
    sprNom = input("Veuillez saisir le nom du produit que vous souhaitez supprimer : ")
    x = 0
    newTab = []
    
    for i in range(0, len(tab)):
        if(tab[i]["nom"] != sprNom):
            newTab.append(tab[i])
            x += 1
    if(x <= 0):
        print("Ce produit n'existe pas")
    else :
        print("Suppression réussie.")
        tab = newTab
    
    return tab
            
            

def trie(direction, tab):
    for i in range(0, len(tab) - 1):
        for j in range(i + 1, len(tab)):
            if(direction == "CR"):
                if tab[i]["prix"] > tab[j]["prix"] :
                    box = tab[i]
                    tab[i] = tab[j]
                    tab[j] = box
            else :
                if (tab[i]["prix"] < tab[j]["prix"]):
                    box = tab[i]
                    tab[i] = tab[j]
                    tab[j] = box
    return tab








def recherche() :
    rech = input("Choisissez le nom de produits que vous souhaitez afficher : ")
    print("-----------------------------------------")
    x = 0
    for i in range(0, len(tab)):
        if(tab[i]["nom"] == rech):
            x += 1
            print("-----------------------------------------")
            print("- Référence : ", tab[i]["ref"])
            print("- Nom du produit : ", tab[i]["nom"])
            print("- Catégorie : ", tab[i]["cat"])
            print("- Prix : ", tab[i]["prix"])
            print("-----------------------------------------")
    if(x == 0):
        print("-----------------------------------------")
        print("ce produit n'existe pas !!!!!!!!!!")   
        print("-----------------------------------------")   
            




def afficher(tab):
    for i in range(0, len(tab)):
        print("-----------------------------------------")
        print("- Référence : ", tab[i]["ref"])
        print("- Nom du produit : ", tab[i]["nom"])
        print("- Catégorie : ", tab[i]["cat"])
        print("- Prix : ", tab[i]["prix"])
        print("-----------------------------------------")












n = saisir()
tab = remplir(n)

exit = False

while(exit == False):
                print("Pour afficher tous les produits, tapez AF : ")
                print("Pour ajouter des produits, tapez AJ : ")
                print("Pour trier les produits par ordre croissant, tapez CR : ")
                print("Pour trier les produits par ordre décroissant, tapez DCR : ")
                print("Pour rechercher dans les produits, tapez CHR : ")
                print("Pour supprimer des produits, tapez SPR : ")
                print("Pour quitter le programme, tapez EXIT : ")
                print("-----------------------------------------")

                action = input("--choisissez votre action : ")
                while not(action == "AF" or action == "AJ" or action == "CR" or action == "DCR" or action == "CHR" or action == "EXIT" or action == "SPR"):
                            action = input("SLV !!, choisissez une action valide : ")
                print("######################################")

                if(action == "AF"):
                            afficher(tab)
                elif(action == "AJ"):
                            nbrAjout = int(input("--- Saisir le nombre de produits que vous souhaitez ajouter : "))
                            tab = remplir(nbrAjout)
                elif (action == "CR" or action == "DCR"):
                            tab = trie(action, tab)
                            afficher(tab)
                if(action == "CHR"):
                            recherche()
                            print("-----------------------------------------")
                if(action == "SPR"):
                            print("-----------------------------------------")
                            tab = supprimer(tab)
                            print("-----------------------------------------")
                if(action == "EXIT"):
                            exit = True
            
    

        