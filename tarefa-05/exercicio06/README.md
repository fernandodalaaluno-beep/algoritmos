#### 📁 `exercicio06/README.md`
```markdown
# Exercício 06: Análise de Tráfego e Pacotes Jumbo

```python
buffer = [64, 1500, 9000, 512, 1024, 1518, 64, 128, 1500, 1400]
total_pacotes = len(buffer)
total_bytes = sum(buffer)

jumbo = 0
for tamanho in buffer:
    if tamanho > 1500:
        jumbo += 1

porcentagem_jumbo = (jumbo / total_pacotes) * 100

print(f"Total de pacotes recebidos: {total_pacotes}")
print(f"Tamanho total em bytes: {total_bytes}")
print(f"Porcentagem de pacotes jumbo: {porcentagem_jumbo:.1f}%")
