quantidade_passos = int(input())

passos = 0

if quantidade_passos > 0 :
  passos+=quantidade_passos
  
elif quantidade_passos <= 0 :
  print("Nenhum passo dado na floresta.")

for i in range(1, quantidade_passos + 1):
    print(f"Explorador: {i} passo{'s' if i > 1 else ''}")