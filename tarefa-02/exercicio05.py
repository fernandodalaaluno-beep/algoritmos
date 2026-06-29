print("Tabela ASCII (32 a 126):")  
print("-" * 40)  
print("Código | Caractere | Tipo")  
print("-" * 40)  

for codigo in range(32, 127):  
    caractere = chr(codigo)  
    if caractere.isalpha():  
        tipo = "Letra"  
    elif caractere.isdigit():  
        tipo = "Dígito"  
    else:  
        tipo = "Símbolo"  
    print(f"{codigo:6d} | {caractere:^9} | {tipo}")
