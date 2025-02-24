# Jour 1 - Syntaxe et Variables
## 1. Syntaxe de base

Python utilise l’indentation pour structurer le code et ne nécessite pas de point-virgule à la fin des lignes.

Exemple :

    - Un commentaire commence par #
    - L'affichage se fait avec print()

## 2. Variables et types de données

Python est dynamiquement typé, ce qui signifie qu'on n’a pas besoin de déclarer le type des variables.

Types de base :

    - Entiers : 30
    - Flottants : 19.99
    - Chaînes de caractères : "Alice"
    - Booléens : True / False

Conversions de types possibles :

    - int(), float(), str()

## 3. Opérations de base

Quelques opérations courantes :

    - Addition : +
    - Soustraction : -
    - Multiplication : *
    - Division : / (résultat flottant)
    - Division entière : //
    - Modulo : %
    - Puissance : **

## 4. Entrée utilisateur

On utilise input() pour demander une saisie utilisateur.

Exemple :

    - nom = input("Quel est votre nom ? ")
    - age = int(input("Quel est votre âge ? "))

## 5. Exercice

Créer un programme qui :

Demande à l’utilisateur son prénom et son âge.
Convertit l’âge en entier.
Affiche un message sous la forme : "Bonjour Alice, tu as 25 ans."