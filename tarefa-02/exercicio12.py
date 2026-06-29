import math

N = int(input("Quantos pontos? "))
pontos = []

for i in range(N):
    print(f"Ponto {i+1}:")
    x = float(input(" x: "))
    y = float(input(" y: "))
    pontos.append((x, y))

distancias = []
maior_dist_origem = 0
ponto_mais_distante = None

for i, (x, y) in enumerate(pontos):
    dist_origem = math.sqrt(x**2 + y**2)
    if dist_origem > maior_dist_origem:
        maior_dist_origem = dist_origem
        ponto_mais_distante = (x, y)

for i in range(N):
    x1, y1 = pontos[i]
    x2, y2 = pontos[(i + 1) % N]
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distancias.append(dist)

dist_media = sum(distancias) / N
perimetro = sum(distancias)

print(f"\nDistancia media entre pontos consecutivos: {dist_media:.2f}")
print(f"Ponto mais distante da origem: {ponto_mais_distante} (distancia: {maior_dist_origem:.2f})")
print(f"Perimetro total do poligono: {perimetro:.2f}")
