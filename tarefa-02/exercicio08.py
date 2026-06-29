N = int(input("Quantos alunos? "))  
medias = []  

for i in range(N):  
    nome = input(f"\nNome do {i+1}º aluno: ")  
    notas = []  
    for j in range(4):  
        nota = float(input(f"Nota {j+1}: ")) 
        notas.append(nota)  
    media = sum(notas) / 4  
    medias.append(media)  
    
    if media >= 7:  
        situacao = "Aprovado"  
    elif media >= 5:  
        situacao = "Recuperação"  
    else:  
        situacao = "Reprovado"  
    print(f"{nome}: média {media:.1f} - {situacao}")  

media_turma = sum(medias) / N  
print(f"\nMédia da turma: {media_turma:.1f}")
