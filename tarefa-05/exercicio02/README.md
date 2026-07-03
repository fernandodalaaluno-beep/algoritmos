#### 📁 `exercicio02/README.md`
```markdown
# Exercício 02: Análise de Tolerância em Resistências

```python
nominal = [47.0, 100.0, 220.0, 33.0, 68.0]
simulacao = [47.0, 95.0, 220.0, 33.0, 64.0]

equivalente_nominal = sum(nominal)
equivalente_simulada = sum(simulacao)
diferenca = equivalente_nominal - equivalente_simulada

print("Lista nominal:", nominal)
print("Lista simulada:", simulacao)
print(f"Resistência equivalente nominal: {equivalente_nominal:.1f} Ω")
print(f"Resistência equivalente simulada: {equivalente_simulada:.1f} Ω")
print(f"Diferença entre os casos: {diferenca:.1f} Ω")
