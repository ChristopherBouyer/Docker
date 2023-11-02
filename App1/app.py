def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division par zéro n'est pas autorisée."
    return a / b

while True:
    print("Options:")
    print("Entrez 'add' pour effectuer une addition")
    print("Entrez 'sous' pour effectuer une soustraction")
    print("Entrez 'mult' pour effectuer une multiplication")
    print("Entrez 'div' pour effectuer une division")
    print("Entrez 'quit' pour quitter le programme")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "sous", "mult", "div"):
        num1 = float(input("Entrez le premier nombre: "))
        num2 = float(input("Entrez le deuxième nombre: "))

        if user_input == "add":
            print("Résultat:", addition(num1, num2))
        elif user_input == "sous":
            print("Résultat:", soustraction(num1, num2))
        elif user_input == "mult":
            print("Résultat:", multiplication(num1, num2))
        elif user_input == "div":
            print("Résultat:", division(num1, num2))
    else:
        print("Option invalide. Réessayez.")
