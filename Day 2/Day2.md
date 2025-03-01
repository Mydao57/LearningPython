# Jour 2 - Structures de Contrôle (Conditions et Boucles)

## 1. Conditions (`if`, `elif`, `else`)

Python permet d’exécuter des blocs de code en fonction de conditions.

Exemple :

- `if condition`: -> Exécute si la condition est vraie
- `elif autre_condition`: -> Teste une autre condition
- `else`: -> Exécute si aucune condition précédente n’est vraie

## 2. Opérateurs de comparaison et logiques

Opérateurs de comparaison

- `==` : Égal à
- `!=` : Différent de
- `<, >, <=, >=` : Inférieur, supérieur, etc.

Opérateurs logiques
- `and` : Les deux conditions doivent être vraies
- `or` : Au moins une condition doit être vraie
- `not` : Inverse la condition

## 3. Les boucles (while, for)

Boucle `while`
Répète un bloc tant qu’une condition est vraie.

Exemple :

- `while condition`: -> Continue tant que la condition est vraie

Boucle for
Parcourt une séquence comme range() ou une liste.

Exemple :

- `for i in range(n)`: -> Répète n fois
- `for élément in liste`: -> Parcourt chaque élément

## 4. break et continue

- `break` : Interrompt une boucle
- `continue` : Passe à l’itération suivante

## 5. Exercice du jour

Créer un programme qui :

1. Demande un nombre à l’utilisateur.
2. Affiche s’il est positif, négatif ou nul.
3. Affiche ensuite tous les nombres de 0 à ce nombre inclus.