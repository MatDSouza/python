# Lista para armazenar os itens
itens = []

i = 0
while i < 3:
    item = input(i+1)
    itens.append(item)
    i += 1

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")