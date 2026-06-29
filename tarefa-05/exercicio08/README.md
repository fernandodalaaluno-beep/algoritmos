#### 📁 `exercicio08/README.md`
```markdown
# Exercício 08: Monitorização e Filtro de Voltagem de Sensores

```python
amostras_entrada = [12.0, 11.5, 13.5, 10.5, 12.5]
leituras = []

for valor in amostras_entrada:
    leituras.append(valor)

media = sum(leituras) / len(leituras)
print(f"Média das leituras: {media:.2f} V")

for leitura in leituras:
    if leitura < 10.8 or leitura > 13.2:
        print(f"Alerta: leitura fora da faixa -> {leitura:.1f} V")
