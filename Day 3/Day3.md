# Jour 3 - Fonctions et Portée des Variables

## 1. Définition et appel d’une fonction

Une fonction permet de regrouper du code réutilisable.
Syntaxe :

- `def nom_de_la_fonction(parametre1, parametre2):`
- `return` permet de renvoyer une valeur

Exemple :

- Une fonction qui affiche un message :
    - `def saluer(nom): print("Bonjour", nom)`
- Une fonction qui retourne un calcul :
    - `def addition(a, b): return a + b`

## 2. Valeurs par défaut et arguments nommés
Une fonction peut avoir des valeurs par défaut.

Exemple :

- `def dire_bonjour(nom="utilisateur"):`

## 3. Portée des variables

- Une variable locale est définie dans une fonction et n'existe qu'à l'intérieur.
- Une variable globale est définie en dehors des fonctions et accessible partout.

Exemple :

- `global nom_de_variable` permet de modifier une variable globale à l'intérieur d'une fonction.

## 4. Fonctions lambda

Les fonctions lambda sont des fonctions anonymes simples.

Exemple :

- `carre = lambda x: x ** 2`

Utilisation avec `map()` :
- `list(map(lambda x: x ** 2, [1, 2, 3]))`

## 5. Exercice du jour

Créer deux fonctions :

- `est_pair(nombre)`, qui retourne `True`si le nombre est pair, sinon `False`.
- `compter_pairs(liste)`, qui utilise `est_pair` pour compter les nombres pairs dans une liste.