custo_fixo = float(input("Custo fixo (R$): "))  
custo_variavel = float(input("Custo variável por unidade (R$): ")) 
preco_venda = float(input("Preço de venda por unidade (R$): ")) 
N = int(input("Número máximo de unidades: "))  
ponto_equilibrio = None  

print("\nUnidades | Lucro/Prejuízo | Situação")  
print("-" * 45)  

for unidades in range(0, N + 1):  
    lucro = (preco_venda - custo_variavel) * unidades - custo_fixo  
    if lucro < 0:  
        situacao = "PREJUÍZO"  
    elif lucro == 0:  
        situacao = "EQUILÍBRIO"  
        if ponto_equilibrio is None:  
            ponto_equilibrio = unidades  
    else:  
        situacao = "LUCRO" 
    print(f"{unidades:8d} | R$ {lucro:10.2f} | {situacao}")  

if ponto_equilibrio is not None:  
    print(f"\nPonto de equilíbrio: {ponto_equilibrio} unidades") 
else:  
    print(f"\nPonto de equilíbrio: {custo_fixo / (preco_venda - custo_variavel):.0f} unidades")
