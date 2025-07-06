from estruturas_dados.fila import Fila

print("🧪 Testando Fila:")
fila = Fila()

fila.enfileirar("Primeiro")
fila.enfileirar("Segundo")
fila.enfileirar("Terceiro")

print(f"Fila atual: {fila}")
print("Desenfileirando:", fila.desenfileirar())  # Primeiro
print("Fila atual:", fila)
print("Está vazia?", fila.esta_vazia())         # False
fila.desenfileirar()
fila.desenfileirar()
print("Está vazia agora?", fila.esta_vazia())   # True
