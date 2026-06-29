# Exercício 01: Sincronização de Roteamento

```python
tabela_atual = ['10.0.0.0/8', '172.16.0.0/12', '192.168.1.0/24', '203.0.113.0/24', '198.51.100.0/24']
nova_tabela = ['10.0.0.0/8', '172.16.0.0/12', '192.168.2.0/24', '198.51.100.0/24']

rotas_removidas = []
rotas_adicionadas = []

for rota in tabela_atual:
    if rota not in nova_tabela:
        rotas_removidas.append(rota)

for rota in nova_tabela:
    if rota not in tabela_atual:
        rotas_adicionadas.append(rota)

print("Tabela antiga:", tabela_atual)
print("Tabela nova:", nova_tabela)
print("Rotas removidas:", rotas_removidas)
print("Rotas adicionadas:", rotas_adicionadas)
