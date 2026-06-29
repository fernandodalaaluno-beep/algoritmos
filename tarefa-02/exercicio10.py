N = int(input("Digite o valor limite N: "))

if N < 2:
    print("Nao ha numeros primos ate este valor.")
else:
    primo = [True] * (N + 1)
    primo[0] = primo[1] = False
    
    for i in range(2, int(N ** 0.5) + 1):
        if primo[i]:
            for j in range(i * i, N + 1, i):
                primo[j] = False
                
    primos = [i for i in range(2, N + 1) if primo[i]]
    print(f"\nNumeros primos ate {N}:")
    print(primos)
    print(f"Total encontrado: {len(primos)}")
