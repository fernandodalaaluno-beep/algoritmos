#### 📁 `exercicio04/README.md`
```markdown
# Exercício 04: Monitorização de Interferência em Canais RF

```python
canais = [850, 900, 950, 1800, 2100, 2600]
interferencia = {850: -65, 900: -80, 950: -75, 1800: -50, 2100: -72, 2600: -55}
limiar = -70

ativos = canais.copy()
for canal in canais:
    if interferencia[canal] > limiar:
        ativos.remove(canal)
        print(f"Canal desativado: {canal} MHz")

print("Canais restantes:", ativos)
