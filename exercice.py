# a = 1
# b = 2
# c = 3
# d = 4
# e = 5

# tab = [1, 2, 3, 4, 5]

# lenthTab = len(tab)

# for i in range (0, lenthTab):
#     print(tab[i])

# print(tab[12])
# print(lenthTab)
# from numpy import array, empty

# tab = empty(100, dtype=dict)


# n = int(input("langeur de tab "))
# for i in range (0,n):
#     tab[i]={}
#     tab[i]["nom"] = input("nom emploiyeur ")
#     tab[i]["salaire"] = int(input("salaire emploiyeur "))
#     tab[i]["age"]=int(input("age emploiyeur "))

# print("############")


# for i in range (0,len(tab)): 
#    print(tab[i]["nom"])
#    print(tab[i]["salaire"])
#    print("------------------------")



# func = lambda x :  x

# print(func(2))

# for num in range (1, 5):
#     print(num)

# x = 0

# while (x < 10):
#     x = x + 1
# print(x)














# n = int(input("9adech bech tzid men karahab (toul el tableau) : "))

# for i in range(0, n):
#     tab[i] = {}
#     tab[i]['marque'] = input("naw3 el karahab : ")
#     tab[i]['prix'] = int(input("soum el karahab : "))
#     tab[i]['color'] = input('loun el karahba : ')
#     print('---------------------')
    
    
# for i in range(0, len(tab)):
#     print('############  ', "affichage", '  #################"')
#     print(tab[i]["marque"])
#     print(tab[i]["prix"])
#     print(tab[i]["color"])
#     print('-------------')












# tab = [
#     { 'marque': 'BMW X5', 
#       'color': 'black', 
#       'drive_type' :  "X-drive",
#       'chv' : "40" 
#     },
#     { 'marque': 'Mercedess', 
#      'color': 'white', 
#      'drive_type' :  "X-drive",
#      'chv' : "48" 
#     },
#      {'marque': 'bentley', 
#        'color': 'gray', 
#        'drive_type' :  "X-drive",
#        'chv' : "60" 
#     }
    
# ]


# lenthTab = len(tab)
# for i in range(0,lenthTab):
#     print(tab[i]["marque"])
#     print(tab[i]["color"])
#     print(tab[i]["drive_type"])
#     print(tab[i]["chv"])
#     print("#############")
    



# print( "car1", tab[0]["marque"])
# print( "car2",tab[1]["marque"])
# print( "chv car3",tab[2]["chv"])







# for key in car3:
#     print(key)


# print(tab[])

# print("resultat :", tab[0]+tab[1]+tab[2]+tab[3]+tab[4])





# print("marque de car1---- :: ", car1["marque"])
# print("couleur de car1---- :: ", car1["color"])
# print("drive type de car1---- :: ", car1["drive_type"])
# print("chv car1---- :: " + car1["chv"] + "CV")

# print("###################")


# print("marque de car2---- :: ", car2["marque"])
# print("couleur de car2---- :: ", car2["color"])
# print("drive type de car2---- :: ", car2["drive_type"])
# print("chv car2---- :: " + car2["chv"] +  " CV")







# tab = []

# def chessboard (n):
#     for i in range(0, n):
#         row = []
#         for j in range(0, n):
#             if(i % 2 == 0):
#                 if(j % 2 == 0):
#                     row.append("1")
#                 else:
#                     row.append("0")
#             elif(i % 2 != 0):
#                 if(j % 2 == 0):
#                     row.append("0")
#                 else:
#                     row.append("1")
#         tab.append(row)
    
#     for i in range(0, n):
#         result = ""
#         for j in range(0, n):
#             result = result + tab[i][j]
#         print(result)
            
            
            
# n = int(input("saisir un entier"))
# chessboard(n)







# matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

# def increases (row, col):
#     for i in range(0, 3):
#         for j in range(0, 3):
#             if(i == row - 1 and j == col - 1):
#                 matrix[i][j] = matrix[i][j] + 1
#     return matrix


# def show(mtrx):
#     for i in range(0, 3):
#         row = ""
#         for j in range(0, 3):
#             row += str(mtrx[i][j])
#         print(row)



# show(matrix)

# row = int(input("saisir le numero de la lingne"))
# col = int(input("saisir le nombre de colonne"))

# matrix = increases(row=row, col=col)

# show(matrix)










# tab = [["a", "b", "c"], ["e", "f", "g"], ["h", "k", "l"], ["m", "n", "o"]]

# print(tab[0][2])













# profile = {
#     "nom" : "farouk",
#     "age" : 24 
# }

# print(profile["nom"])
# print(profile["age"])






# print(tab[2])










# def jama3(a, b):
#     s = a + b
#     print(s)


    


    
    


