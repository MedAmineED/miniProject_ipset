import numpy as np
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
        produit["achat"] = int(input("--- Entrez le prix d'achat de votre article --: "))
        produit["vente"] = int(input("--- Entrez le prix de vente de votre article --: "))
        produit["date"] = datetime.datetime.now()
        tab.append(produit)
        print("-----------------------------------------")
    return tab 
            


def supprimer(tab):
    print("Pour supprimer un produit par son reference, saisissez 'ref' : ")
    print("Pour supprimer un produit par son nom, saisissez 'nom' : ")
    print( "Pour supprimer tous les produits d'une catégorie, tapez 'cat' : ")
    print("-----------------------------------------")
    sprOption = input( "Veuillez saisir votre choix de suppression : ")
    
    
    while not(sprOption == "ref" or sprOption == "nom" or sprOption == "cat"):
        sprOption = input( "SLP!!  Veuillez saisir votre choix de suppression. (ref ,nom or cat) : ")
    
    
    
    
    sprNom = input("Veuillez saisir la référence du produit que vous souhaitez supprimer : ")
    x = 0
    newTab = []
    
    for i in range(0, len(tab)):
        if(tab[i][sprOption] != sprNom):
            newTab.append(tab[i])
            x += 1
    if(x <= 0):
        print("Ce produit n'existe pas")
    else :
        print("Suppression réussie.")
        tab = newTab
    
    return tab
            
            
        
            
                
        
        
    
    
    
    







def trie(n, direction, tab):
    print("--- Pour trier par prix d'achat, tapez 'achat'.")
    print("--- Pour trier par prix de vente, tapez 'vente'.")
    print("--- Pour trier par date, tapez 'date'.")

    tr = input("------ taper 'achat' , 'vente' ou 'date' --: ")
    while not(tr == "vente" or tr == "achat" or tr == "date"):
        tr = input("Cette action n'est pas valide ! Veuillez saisir une action valide ('achat' ou 'vente') : ")
    
    for i in range(0, len(tab) - 1):
        for j in range(i + 1, len(tab)):
            condition = False
            if(direction == "CR"):
                condition = tab[i][tr] < tab[j][tr]
            else :
                condition = tab[i][tr] > tab[j][tr]
            if(condition):
                box = tab[i]
                tab[i] = tab[j]
                tab[j] = box
    return tab








def recherche(n) :
    print("--- Pour rechercher par référence, tapez 'ref' : ")
    print("--- Pour rechercher par nom, tapez 'nom' : ")
    print("--- Pour rechercher par catégorie, tapez 'cat' : ")
    print("--- Pour rechercher par prix d'achat, tapez 'achat' : ")
    print("--- Pour rechercher par prix de vente, tapez 'vente' : ")
    print("--- Pour quitter le programme, tapez 'EXIT' : ")

    print("######################################")
    
    rechercheAction = input("choisissez le type de recherche : ")
    while not(rechercheAction == "ref" or rechercheAction == "nom" or rechercheAction == "cat" or rechercheAction == "achat" or rechercheAction == "vente"):
        rechercheAction = input("Cette caractéristique n'existe pas. Veuillez saisir le type de recherche : ")
    print("-----------------------------------------")
    
    rech = input("Choisissez le  " + rechercheAction + " de produits que vous souhaitez afficher : ")
    print("-----------------------------------------")
    x = 0
    for i in range(0, n):
        if(tab[i][rechercheAction] == rech):
            x += 1
            print("-----------------------------------------")
            print("- Référence : ", tab[i]["ref"])
            print("- Nom du produit : ", tab[i]["nom"])
            print("- Catégorie : ", tab[i]["cat"])
            print("- Prix d'achat : ", tab[i]["achat"])
            print("- Prix de vente : ", tab[i]["vente"])
            print("- Date d'ajout : ", tab[i]["date"])
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
        print("- Prix d'achat : ", tab[i]["achat"])
        print("- Prix de vente : ", tab[i]["vente"])
        print("- Date d'ajout : ", tab[i]["date"])
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
                            tab = trie(n, action, tab)
                            afficher(tab)
                if(action == "CHR"):
                            recherche(n)
                            print("-----------------------------------------")
                if(action == "SPR"):
                            tab = supprimer(tab)
                if(action == "EXIT"):
                            exit = True
            
    

        
