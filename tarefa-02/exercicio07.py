import math  

x = float(input("Digite o valor de x: "))  
N = int(input("Digite o número de termos N: "))  

# Série e^x  
ex = 0  
for n in range(N):  
    ex += (x ** n) / math.factorial(n)  

# Série sin(x)  
sin_x = 0  
for n in range(N):  
    sin_x += ((-1) ** n) * (x ** (2*n + 1)) / math.factorial(2*n + 1)  

print(f"\ne^{x} ≈ {ex:.6f}")  
print(f"sin({x}) ≈ {sin_x:.6f}")  
print(f"Valor real e^{x}: {math.exp(x):.6f}")  
print(f"Valor real sin({x}): {math.sin(x):.6f}")
