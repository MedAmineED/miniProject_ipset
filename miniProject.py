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
        produit["ref"] = input("choisir la reference de votre article --: ")
        produit["nom"] = input("choisir le nom de votre article --: ")
        produit["cat"] = input("choisir la categorie de votre article --: ")
        produit["achat"] = int(input("choisir le prix d'achat de votre article --: "))
        produit["vente"] = int(input("choisir le prix de vente de votre article --: "))
        produit["date"] = datetime.datetime.now()
        tab.append(produit)
        print("-----------------------------------------")
    return tab 
            


def suprimer(tab):
    print("Pour supprimer un produit par son reference, saisissez 'ref'.")
    print("Pour supprimer un produit par son nom, saisissez 'nom'.")
    print( "Pour supprimer tous les produits d'une catégorie, tapez 'cat'.")
    print("-----------------------------------------")
    sprOption = input( "Veuillez saisir votre choix de suppression.")
    while not(sprOption == "ref" or sprOption == "nom" or sprOption == "cat"):
        sprOption = input( "SLP!!  Veuillez saisir votre choix de suppression. (delr , deln or delc)")
        
    for i in range(0, len(tab)):
        
        
    
    
    
    







def trie(n, direction):
    print("--- pour trie en fonction de prix d'achat taper 'achat'")
    print("--- pour trie en fonction de prix de vente taper 'vente'")
    print("--- pour trie en fonction de prix de date taper 'date'")
    tr = input("------------ taper 'achat' , 'vente' ou 'date' --: ")
    while not(tr == "vente" or tr == "achat" or tr == "date"):
            tr = input("cette action n'est pas valide!!! taper une action valide ('achat' ou 'vente') --: ")
    
    for i in range(0, n - 1):
        for j in range(i + 1, n):
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
    print("-----------------------------------------")
    for i in range(0, n):
        if(tab[i][rechercheAction] == rech):
            print(tab[i]["ref"])
            print(tab[i]["nom"])
            print(tab[i]["cat"])
            print(tab[i]["achat"])
            print(tab[i]["vente"])
            print("-----------------------------------------")
            
            




def afficher(tab):
    for i in range(0, len(tab)):
        print("-----------------------------------------")
        print("- reference : ",tab[i]["ref"])
        print("- nom de produit : ",tab[i]["nom"])
        print("- categorie : ",tab[i]["cat"])
        print("- prix d'achat : ",tab[i]["achat"])
        print("- prix de vente : ",tab[i]["vente"])
        print("date d'ajout : ", tab[i]["date"])
        print("-----------------------------------------")












n = saisir()
tab = remplir(n)

exit = False

while(exit == False):
                print("pour afficher tout les produits taper AF")
                print("pour ajouter des produits taper AJ")
                print("pour trier le produit croissant taper CR")
                print("pour trier le produit decroissant taper DCR")
                print("pour chercher dans les produits taper CHR")
                print("pour exit le programme taper EXIt")
                print("-----------------------------------------")

                action = input("choisissez votre action : ")
                while not(action == "AF" or action == "AJ" or action == "CR" or action == "DCR" or action == "CHR" or action == "EXIT"):
                            action = input("SLV !!, choisissez une action valide : ")
                print("######################################")

                if(action == "AF"):
                            afficher(tab)
                elif(action == "AJ"):
                            nbrAjout = int(input("saisir le nombre des produits que vous voulez ajouter"))
                            tab = remplir(nbrAjout)
                elif (action == "CR" or action == "DCR"):
                            tab = trie(n, action)
                            afficher(tab)
                if(action == "CHR"):
                            recherche(n)
                            print("-----------------------------------------")
                if(action == "EXIT"):
                            exit = True
            
    

        
