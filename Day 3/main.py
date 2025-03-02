def est_pair(nombre):
    return nombre % 2 == 0  # Retourne directement True ou False
    
    
def compter_pairs(liste):
    nombre_pairs = sum(1 for i in liste if est_pair(i))  # Utilisation d'une compréhension de liste
    return nombre_pairs

print(est_pair(2)) # True
print(est_pair(3)) # False

print(compter_pairs([10, 3, 8, 7, 6, 2])) # 4