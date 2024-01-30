# Listas y acceso a ellas
# []
# list

frutas = list()

print(frutas)
print(type(frutas))

frutas.append('manzana')
frutas.append('platano')
frutas.append('sandia')
frutas.append('fresas')
frutas.append('cocos')
print(frutas)

# acceder al penultimo
# ['manzana', 'platano', 'sandia', 'fresas', 'cocos']
# [0, 1, 2, 3, 4]
# [4, 3, 2, 1, 0]

print(frutas[-3])