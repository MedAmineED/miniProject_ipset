import numpy as np
import datetime
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QListView
from PyQt5.QtGui import QStandardItem, QStandardItemModel


app = QApplication([])
f = uic.loadUi("interface.ui")
tab = [
    {
        "ref" : "ph001",
        "nom" : "iphone 4",
        "cat" : "phone",
        "achat" : 200,
        "vente" : 250,
        "date" : "21-06-2023",
        "quantite" : 300
    },
    {
        "ref" : "ph002",
        "nom" : "samsung",
        "cat" : "phone",
        "achat" : 600,
        "vente" : 850,
        "date" : "21-06-2023",
        "quantite" : 252
    },
    {
        "ref" : "pc001",
        "nom" : "hp",
        "cat" : "pc",
        "achat" : 1800,
        "vente" : 2400,
        "date" : "21-06-2023",
        "quantite" : 140
    },
    {
        "ref" : "ph003",
        "nom" : "iphoneX",
        "cat" : "phone",
        "achat" : 1500,
        "vente" : 1800,
        "date" : "21-06-2023",
        "quantite" : 163
    },
    {
        "ref" : "ph001",
        "nom" : "oppo",
        "cat" : "phone",
        "achat" : 645,
        "vente" : 890,
        "date" : "21-06-2023",
        "quantite" : 270
    },
    {
        "ref" : "ph001",
        "nom" : "dell",
        "cat" : "pc",
        "achat" : 1400,
        "vente" : 2000,
        "date" : "21-06-2023",
        "quantite" : 40
    },
    {
        "ref" : "ph001",
        "nom" : "apple watch",
        "cat" : "watch",
        "achat" : 800,
        "vente" : 1200,
        "date" : "21-06-2023",
        "quantite" : 120
    },
]


aj = None
md = None
sp = None
st = None
notExist = None


# def testF(itmes):
#     for i in range(0, len(itmes)):
#         print(itmes[i])



#les fonctions d'affichage
def afficher(tab):
        list_view = f.findChild(QListView, "resPr")
        model = QStandardItemModel()

        for prd in tab:
            item = QStandardItem(f"Reference : {prd['ref']} || Nom: {prd['nom']} || categorie: {prd['cat']} || prix d'achat: {prd['achat']}DT || prix de vente: {prd['vente']}DT || quantite : {prd['quantite']} || date d'ajout: {prd['date']}")
            separation = QStandardItem("---------------------------------------------------------------------------------------------")
            model.appendRow(item)
            model.appendRow(separation)
        list_view.setModel(model)

def afficherTout():
    afficher(tab=tab)
    
def afficherStcCat():
    tabCategorie = separerCtegories()
    
    list_view = st.findChild(QListView, "stqCat")
    model = QStandardItemModel()
    nbrCatStock = QStandardItem(f"Nombre de categorie : {len(tabCategorie)}")
    model.appendRow(nbrCatStock)
    model.appendRow(QStandardItem(f"-------------------------"))
    
    # print("test stock", tabCategorie[0]["stock"])
    
    for prd in tabCategorie:
        nomItem = QStandardItem(f"Nom: {prd['nom']}")
        nbrItem = QStandardItem(f"Nombre d'article : {prd['nbrArticle']} ")
        stockItem = QStandardItem(f"Stock : {prd['stock']} ")
        separation = QStandardItem("---------------------------------------------------------------------------------------------")
        model.appendRow(nomItem)
        model.appendRow(nbrItem)
        model.appendRow(stockItem)
        model.appendRow(separation)
    list_view.setModel(model)
        

def afficherStatistiqueArticle():
    #L'article le plus cher à l'achat
    articlePAchat = touverArticlePlusCher("achat", tab=tab)
    st.pAchatNom.setText(articlePAchat["nom"])
    st.pAchatCat.setText(articlePAchat["cat"])
    st.pAchatPAchat.setText(str(articlePAchat["achat"]) + " DT")
    st.pAchatPVente.setText(str(articlePAchat["vente"]) + " DT")
    
    prixAchat = articlePAchat["achat"]
    prixVente = articlePAchat["vente"]
    gain = prixVente - prixAchat
    
    gainPrc = calCulerPorcentage(prixAchat, gain=gain)
    
    st.pAchatGain.setText(str(gainPrc) + "%")
    
    stockTotal = calculStockTotal()
    stockArticle = articlePAchat["quantite"]
    
    stockPrc = calCulerPorcentage(stockTotal, stockArticle)
    st.pAchatStock.setText(str(stockPrc) + "%")
    
    etatStock = etatDeStock(stockArticle)
    
    st.pAchatEtat.setText(etatStock)
    
    #L'article le plus cher à vente
    articleVente = touverArticlePlusCher("vente", tab=tab)
    st.pVenteNom.setText(articleVente["nom"])
    st.pVenteCat.setText(articleVente["cat"])
    st.pVentePAchat.setText(str(articleVente["achat"]) + " DT")
    st.pVentePVente.setText(str(articleVente["vente"]) + " DT")
    
    prixAchat = articleVente["achat"]
    prixVente = articleVente["vente"]
    gain = prixVente - prixAchat
    
    gainPrc = calCulerPorcentage(prixAchat, gain=gain)
    st.pVenteGain.setText(str(gainPrc) + "%")
    
    stockTotal = calculStockTotal()
    stockArticle = articleVente["quantite"]
    
    stockPrc = calCulerPorcentage(stockTotal, stockArticle)
    st.pVenteStock.setText(str(stockPrc) + "%")
    
    etatStock = etatDeStock(stockArticle)
    
    st.pVenteEtat.setText(etatStock)
    
    #êAfficher les statistique de tout les produits
    list_view = st.findChild(QListView, "statArticle")
    model = QStandardItemModel()
    nbrCatStock = QStandardItem(f"Stock total : {stockTotal}")
    model.appendRow(nbrCatStock)
    model.appendRow(QStandardItem(f"-------------------------"))
    
    for prd in tab:
        nomItem = QStandardItem(f"Nom d'article: {prd['nom']}")
        catItem = QStandardItem(f"Categorie: {prd['cat']}")
        achatItem = QStandardItem(f"prix d'achat : {prd['achat']} ")
        venteItem = QStandardItem(f"prix de vente : {prd['vente']} ")
        
        
        achat = prd["achat"]
        vente = prd["vente"]
        gainPrd = vente - achat
        
        prdGainPrc = calCulerPorcentage(achat=achat, gain= gainPrd)
        
        gainItem = QStandardItem(f"Gain : {str(prdGainPrc)} %")
        
        prdStockPrc = calCulerPorcentage(stockTotal, prd['quantite'])
        stockItem = QStandardItem(f"Stock : {str(prdStockPrc)} %")
        
        
        prdStockEtat = etatDeStock(prd["quantite"])
        etatItem = QStandardItem(f"Stock : {str(prdStockEtat)} ")
        
        
        
        separation = QStandardItem("---------------------------------------------------------------------------------------------")
        model.appendRow(nomItem)
        model.appendRow(catItem)
        model.appendRow(achatItem)
        model.appendRow(venteItem)
        model.appendRow(gainItem)
        model.appendRow(stockItem)
        model.appendRow(etatItem)
        model.appendRow(separation)
    list_view.setModel(model)


#les fonctions d'ouvrir et fermeture des fenetres
def ouvrirAjouter ():
    global aj
    aj = uic.loadUi("ajouter.ui")
    aj.show()
    aj.ajBtn.clicked.connect(remplir)
    aj.cnl.clicked.connect(fermerAjouter)
    
def fermerAjouter():
    aj.close()


def ouvrirModifier():
    global md
    md = uic.loadUi("intModifier.ui")
    md.show()
    md.okBtn.clicked.connect(modifier)
    md.cnl.clicked.connect(fermerModifier)

def fermerModifier():
    md.close()
    
    
    
def ouvrirSupprimer():
    global sp
    sp = uic.loadUi("supprimer.ui")
    sp.show()
    sp.okBtn.clicked.connect(supprimer)
    sp.cnl.clicked.connect(fermerSupprimer)

def fermerSupprimer():
    sp.close()


def ouvrirNotExist():
    global notExist
    notExist = uic.loadUi("notification.ui")
    notExist.show()
    notExist.OKBtn.clicked.connect(fermerNotExist)
    
def fermerNotExist():
    notExist.close()

def ouvrirStatistique():
    global st
    st = uic.loadUi("statistiques.ui")
    st.show()
    st.nbrTotal.setText(str(len(tab)))
    
    #Afficher prix d'achat et prix de vente(Total)
    achatTotal = calculPrixTotal("achat")
    venteTotal = calculPrixTotal("vente")
    st.achatTotal.setText(f"{achatTotal:,d} DT")
    st.venteTotal.setText(f"{venteTotal:,d} DT")
    
    #Afficher le gain (Total)
    gain = venteTotal - achatTotal
    st.gainTotal.setText(f"{gain:,d} DT")
    
    #Afficher la porcentage de gain (Total)
    gainPrc = (gain * 100 / achatTotal)
    gainPrc = "{:.2f}".format(gainPrc)
    st.gainTotalPercent.setText(f"{gainPrc} %")
    
    #afficher les statistique des categories
    afficherStcCat()
    
    #afficher les satatistiques des articles
    afficherStatistiqueArticle()
    
    
    
    
    



#les CRUD
#ajouter des articles
def remplir():
    produit = {}
    produit["ref"] = aj.ref.text()
    produit["nom"] = aj.nom.text()
    produit["cat"] = aj.cat.text()
    produit["achat"] = int(aj.achat.text())
    produit["vente"] = int(aj.vente.text())
    produit["quantite"] = int(aj.quantite.text())
    produit["date"] = datetime.datetime.now()
    tab.append(produit)
    afficher(tab=tab)
    fermerAjouter()
    nombreTotalArticles()
    


        

# Trier les articles selon l'ordre de votre choix.
# -- Si la valeur du parametre "direction" est 1, le tri s'effectue par ordre croissant.
# -- Sinon, il s'effectue par ordre décroissant.
# -----------------------
# Le parametre "ctr" permet de choisir le critere de tri : prix de vente ou prix d'achat.
def trie(direction, tab, ctr):
    for i in range(0, len(tab) - 1):
        for j in range(i + 1, len(tab)):
            condition = False
            if(direction == 1):
                condition = tab[i][ctr] > tab[j][ctr]
            else :
                condition = tab[i][ctr] < tab[j][ctr]
            if(condition):
                box = tab[i]
                tab[i] = tab[j]
                tab[j] = box
    afficher(tab=tab)
    
      
def achatCroissant():
    ctr = "achat"
    trie(1, tab=tab, ctr = ctr)
    
def achatDecroissant():
    ctr = "achat"
    trie(-1, tab=tab, ctr = ctr) 
    
def venteCroissant():
    ctr = "vente"
    trie(1, tab=tab, ctr = ctr)
    
def venteDecroissant():
    ctr = "vente"
    trie(-1, tab=tab, ctr = ctr) 
      
      
      
      


def recherche() :
    tableOptions = [
        {"opt" : f.nom, "name" : "nom"},
        {"opt" : f.categorie, "name" : "cat"},
    ]
    
    sprOption = ""
    rechTab = []
    
    for i in range(0, len(tableOptions)):
        if tableOptions[i]["opt"].isChecked():
               sprOption = tableOptions[i]["name"]
    
    rech = f.inputRech.text()
    
    for i in range(0, len(tab)):
        if(tab[i][sprOption] == rech):
            rechTab.append(tab[i])
            
    if(len(rechTab) == 0):
        ouvrirNotExist()
    else : 
        afficher(rechTab)




def modifier():
    mdNom = md.mdNom.text()
    x = 0
    index = 0
    for i in range(0, len(tab)):
        if(tab[i]["nom"] == mdNom):
            md.ref.setText(tab[i]["ref"])
            md.nom.setText(tab[i]["nom"])
            md.cat.setText(tab[i]["cat"])
            md.achat.setText(str(tab[i]["achat"]))
            md.vente.setText(str(tab[i]["vente"]))
            md.quantite.setText(str(tab[i]["quantite"]))
            x += 1
            index = i
            break
    if(x > 0):
        def enregistrer():
            tab[index] = {
                "ref" : md.ref.text(),
                "nom" : md.nom.text(),
                "cat" : md.cat.text(),
                "achat" : int(md.achat.text()),
                "vente" : int(md.vente.text()),
                "quantite" : int(md.quantite.text()),
                "date" : tab[index]["date"],
            }
            afficher(tab=tab)
            md.close()
        md.enregistrer.clicked.connect(enregistrer)
    else :
        ouvrirNotExist()
  
  
  
  
  
def taraitementDeSuppression(tab, sprOption, sprNom):
        newTab = []
        for i in range(0, len(tab)):
            if(tab[i][sprOption] != sprNom):
                newTab.append(tab[i])
        tab = newTab
        afficher(tab=tab) 
        return tab        


def supprimer():
    tableOptions = [
        {"opt" : sp.productRdio,  "name" : "nom"},
        {"opt" : sp.catRadio, "name" : "cat"},
    ]
    
    sprOption = ""
    rechTab = []
    
    for i in range(0, len(tableOptions)):
        if tableOptions[i]["opt"].isChecked():
                sprOption = tableOptions[i]["name"]
    
    sprNom = sp.sprNom.text()
    list_view = sp.findChild(QListView, "sprList")
    model = QStandardItemModel()
    
    
    for prd in tab:
        if prd[sprOption] == sprNom:
            item = QStandardItem(f"Reference : {prd['ref']} || Nom: {prd['nom']} || categorie: {prd['cat']} || prix d'achat: {prd['achat']}DT || prix de vente: {prd['vente']}DT || quantite : {prd['quantite']} || date d'ajout: {prd['date']}")
            separation = QStandardItem("---------------------------------------------------------------------------------------------")
            model.appendRow(item)
            model.appendRow(separation)
            rechTab.append(prd)
            
    list_view.setModel(model)
    
    if(len(rechTab) > 0):
            def appliquerLaSuppression():
                    global tab
                    tab = taraitementDeSuppression(tab=tab, sprOption=sprOption, sprNom=sprNom)
                    nombreTotalArticles()
                    fermerSupprimer()
            sp.appSuppression.clicked.connect(appliquerLaSuppression)
    else :
        ouvrirNotExist()



#les fonctions des statistiques

def nombreTotalArticles():
    f.nbrTotal.setText(f"Nombre total d'articles : {len(tab)}")  
    
    
def calculPrixTotal(crt):
        total = 0
        for i in range (0, len(tab)):
             total += (int(tab[i][crt]) * int(tab[i]["quantite"]))
        return  total


def calculStockTotal():
        stockTotal = 0
        for i in range(0, len(tab)):
            stockTotal += int(tab[i]["quantite"])
        return stockTotal
        
        
def etatDeStock(stock):
    etat = ""
    if(int(stock) >= 100):
            etat = "eleve"
    else:
        etat = "faible"
    return etat


def calCulerPorcentage(achat, gain):
        prc = ((gain * 100) / achat)
        prc = "{:.2f}".format(prc)
        return prc

 
 
def separerCtegories():
        catTab = []
        for i in range(0, len(tab)):
            exist = False
            for j in range(0, len(catTab)):
                if tab[i]["cat"] == catTab[j]["nom"]:
                    exist = True
            if not(exist):
                nomCategorie = tab[i]["cat"]
                nbrArticle = calculerNbrArtDeCategorie(nomCategorie)
                stock = calculerPorcentageCatStock(nomCategorie)
                categorieEng = {
                    "nom" : nomCategorie,
                    "nbrArticle" : nbrArticle,
                    "stock" : "{:.2f}%".format(stock)
                }
                catTab.append(categorieEng)
                # testF([catTab])
        return catTab
    
# print("test", separerCtegories())
def calculerNbrArtDeCategorie(cat):
            nbr = 0
            for i in range(0, len(tab)):
                if(tab[i]["cat"] == cat):
                    nbr += 1
            return nbr


def calculerPorcentageCatStock(cat):
        stockCategorie = calculerStockCat(cat=cat)
        stockTotal = calculStockTotal()
            
        stockCatPorcentage = (stockCategorie / stockTotal) * 100
        return stockCatPorcentage




    
            
def calculerStockCat(cat):
        stockCat = 0
        for i in range(0, len(tab)):
            if(tab[i]["cat"] == cat):
                stockCat += int(tab[i]["quantite"])
        return stockCat   
    
def touverArticlePlusCher(crt, tab):
      article = {}
      maxValeur = 0
      for i in range(0, len(tab)):
            if (int(tab[i][crt]) > maxValeur):
                maxValeur = int(tab[i][crt])
                article = tab[i]
      #print("test article : ", article)
      return article
            
            
 



 


#programme principale
afficher(tab=tab)
nombreTotalArticles()
f.show()
f.afficher.clicked.connect(afficherTout)
f.ajouter.clicked.connect(ouvrirAjouter)
f.supp.clicked.connect(ouvrirSupprimer)
f.modiferBtn.clicked.connect(ouvrirModifier)
f.rechButton.clicked.connect(recherche)
f.crAchat.clicked.connect(achatCroissant)
f.dcrAchat.clicked.connect(achatDecroissant)
f.crVente.clicked.connect(venteCroissant)
f.dcrVente.clicked.connect(venteDecroissant)
f.stat.clicked.connect(ouvrirStatistique)
app.exec_()







