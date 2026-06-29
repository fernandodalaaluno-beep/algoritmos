corrente = float(input("Digite a corrente elétrica (A): "))  

if corrente <= 10:  
    secao = "1.5 mm²"  
elif corrente <= 16:  
    secao = "2.5 mm²"  
elif corrente <= 25:  
    secao = "4 mm²"  
elif corrente <= 35:  
    secao = "6 mm²" 
else:  
    secao = "consultar engenheiro"  

print(f"\nPara {corrente}A, a seção recomendada é: {secao}")
