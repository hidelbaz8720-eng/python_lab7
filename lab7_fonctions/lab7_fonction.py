def saluer():
    print("Bonjour depuis une fonction !")
    print("Ravi de te voir")


def bonjour(prenom):
    print(f"Salut {prenom} !")

def presentation(nom, age):
    print(f"Je m'appelle {nom}et j'ai {age}ans ")

def additionner(a, b):
    total = a + b
    print(total)

def calcul_ttc(prix_ht, taux=0.2):
    prix_ttc = prix_ht * (1 + taux)
    return prix_ttc
def afficher_message(message, prefix="[INFO]"):
    print (prefix,message)


def somme(*args):
    total = 0
    for valeur in args:
        total += valeur
    return total

def  produit(*args):
    resultat = 1
    for valeur in args:
        resultat *= valeur
    return resultat

compteur = 0

def incrementer(valeur):
    return valeur + 1

compteur = incrementer(compteur)


print(somme(1, 2))
print(somme(1, 2, 3, 4))


afficher_message("Connexion etablie")
afficher_message("Erreur", prefix="[ERREUR]")
print(calcul_ttc(100))          
print(calcul_ttc(100, 0.055))    
print(calcul_ttc(prix_ht=50, taux=0.1)) 

print("le type est ",type(additionner(3,5)))
resultat = additionner(3, 5)
print("Résultat :", resultat)


presentation("hamza" ,19)
presentation("ahmad",20)

saluer()
saluer()
bonjour("Alice")
bonjour("Mohamed")


incrementer()
incrementer()
print(compteur)  # 2

