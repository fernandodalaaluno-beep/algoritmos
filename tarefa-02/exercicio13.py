N = int(input("Quantos movimentos? "))
saldo = 0
movimentos = []

for i in range(N):
    print(f"\nMovimento {i+1}:")
    tipo = input("Tipo (entrada/saida): ").lower()
    quantidade = float(input("Quantidade: "))
    
    if tipo == "entrada":
        saldo += quantidade
        movimentos.append(("ENTRADA", quantidade))
    elif tipo == "saida":
        if quantidade > saldo:
            print("ERRO: Quantidade maior que o saldo!")
            continue
        saldo -= quantidade
        movimentos.append(("SAIDA", quantidade))
    else:
        print("Tipo invalido!")
        continue
        
    print(f"Saldo atual: {saldo:.0f}")
    if saldo < 10:
        print("ALERTA: Estoque abaixo de 10 unidades!")

print("\nRELATORIO FINAL")
print("-" * 30)
for i, (tipo, qtd) in enumerate(movimentos):
    print(f"{i+1:2d}. {tipo:7s}: {qtd:6.0f}")
print("-" * 30)
print(f"Saldo final: {saldo:.0f} unidades")
