frutas=["aguacate","melon","tomate","berenjena","zanahoria"]

print(frutas)

print(len(frutas))

print(frutas[2])

frutas.append("papaya")
print(frutas)

frutas.append("sandía")
print(frutas)

frutas.sort()
print(frutas)

compra=input("Ingresa una fruta:")
frutas.append(compra)

print(frutas)