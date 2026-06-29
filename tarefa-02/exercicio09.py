forca = 0  
deformacao = 0  
falhou = False  

while not falhou:  
    forca += 100  
    deformacao += forca * 0.0001  
    print(f"Força: {forca} N | Deformação: {deformacao:.2f} mm")  
    if deformacao > 5:  
        falhou = True  

print(f"\nPeça falhou com força de {forca} N")  
print(f"Deformação final: {deformacao:.2f} mm")
