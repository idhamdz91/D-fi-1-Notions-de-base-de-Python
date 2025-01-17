# D-fi-1-Notions-de-base-de-Python
#Objectif : Pratiquer votre compréhension des bases de Python, des variables, des opérateurs et des conditions.


# Exercice 01 :
x= int(input("Veulliez introduire la valeur de x: "))
y= int(input("Veuillez introduire la valeur de y: "))

x = x + y  # x devient la somme de x et y
y = x - y  # y devient l'ancienne valeur de x
x = x - y  # x devient l'ancienne valeur de y

if x > y:
    print("x est supérieur à y.")
elif x < y:
    print("x est inférieur à y.")
else:
    print("x et y sont égaux.")


#Exercice 2 :

num1 = int(input("Veueillez introduire une valeur : "))
num2 = int(input("Veuillez introduire une seconde valeur: "))

while True:
    print("Menu :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Veuillez choisir le type d'opération que vous voullez effectuer : ")
    if choix == '1':
        print("Résultat :", num1 + num2)
        break
    elif choix == '2':
        print("Résultat :", num1 - num2)
        break
    elif choix == '3':
        print("Résultat :", num1 * num2)
        break
    elif choix == '4':
        if num2 != 0:
            print("Résultat :", num1 / num2)
        else:
            print("Erreur : Division par zéro, veuillez introduire un autre numéro.")
            break
    elif choix == '5':
        break
else:
    print("Choix invalide, réessayez.")


# Exercice 3
temperature = float(input("Entrez la température en Celsius : "))
while True:
    print("Menu de conversion :")
    print("1. Convertir Celsius en Fahrenheit")
    print("2. Convertir Celsius en Kelvin")
    print("3. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == '1':
        fahrenheit = (temperature * 9/5) + 32
        print("La température en Fahrenheit est: ", fahrenheit , "°F")
        print("Merci d'avoir utilisé le convertisseur de température. Au revoir !")
        break
    elif choix == '2':
        kelvin = temperature + 273.15
        print("La température en Kelvin est: ", kelvin, "K")
        print("Merci d'avoir utilisé le convertisseur de température. Au revoir !")
        break
    elif choix == '3':
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez essayer à nouveau.")


# Exercice 4
number = int(input("veuillez introduire un nombre :"))
if number % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

# Exercie 05:
password = input("Veuillez saisir votre mot de passe de 8 caractères avec une majuscule et un symbole : ")
if (len(password) >= 8 and 
    any(char.isdigit() for char in password) and 
    any(char.isalpha() for char in password) and 
    any(char.isalnum() for char in password)):
    print("Mot de passe fort.")
elif len(password) < 8:
    print("Veuillez respecter la taille du mot de passe !")
else:
    print("Mot de passe erroné, veuillez saisir à nouveau !")
    
