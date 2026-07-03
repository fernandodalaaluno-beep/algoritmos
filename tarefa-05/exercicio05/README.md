#### 📁 `exercicio05/README.md`
```markdown
# Exercício 05: Filtragem de Ruído em Sinais de Vibração

```python
vibracao = [0.12, 0.34, 999.0, 999.8, 0.28, 0.91, 1.42, 0.67]

while 999.0 in vibracao: vibracao.remove(999.0)
while 999.8 in vibracao: vibracao.remove(999.8)

print("Lista limpa:", vibracao)
print("Quantidade de leituras válidas:", len(vibracao))
