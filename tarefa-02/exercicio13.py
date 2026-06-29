tensao_inicial = float(input("Tensao inicial (V): "))
distancia_total = float(input("Distancia total (km): "))
tensao = tensao_inicial

print(f"\nDistancia (km) | Tensao (V) | Status")
print("-" * 45)

for km in range(1, int(distancia_total) + 1):
    tensao *= 0.995
    if tensao < tensao_inicial * 0.90:
        status = "CRITICO (<90%)"
    elif tensao < tensao_inicial * 0.95:
        status = "ALERTA (<95%)"
    else:
        status = "Normal"
    print(f"{km:13d} | {tensao:9.2f} | {status}")

print(f"\nTensao final: {tensao:.2f} V")
print(f"Perda total: {(1 - tensao/tensao_inicial)*100:.1f}%")
