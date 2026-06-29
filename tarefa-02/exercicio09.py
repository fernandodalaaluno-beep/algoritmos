forca = 0
deformacao = 0
falhou = False

while not falhou:
    forca += 100
    deformacao += forca * 0.0001
    print(f"Forca: {forca} N | Deformacao: {deformacao:.2f} mm")
    if deformacao > 5:
        falhou = True

print(f"\nPeca falhou com forca de {forca} N")
print(f"Deformacao final: {deformacao:.2f} mm")
