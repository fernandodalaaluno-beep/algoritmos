# Tarefa 02 — Estruturas de Controlo, Repetição e Simulações

**Estudante:** Fernando Da Silva Dala  
**Matrícula:** 2610100511  

Este módulo apresenta a resolução prática de 11 algoritmos aplicados a problemas lógicos, simulações de Engenharia e Estruturas de Dados utilizando a linguagem Python. Os blocos abaixo contêm o código-fonte vivo e copiável de cada aplicação.

---

## 5. Gerador de Tabela ASCII
**Descrição:** Algoritmo que percorre os códigos decimais de 32 a 126 na tabela ASCII, convertendo-os em caracteres legíveis e classificando-os dinamicamente entre letras, dígitos ou símbolos.

```python
print("Tabela ASCII (32 a 126):")  
print("-" * 40)  
print("Código | Caractere | Tipo")  
print("-" * 40)  

for codigo in range(32, 127):  
    caractere = chr(codigo)  
    if caractere.isalpha():  
        tipo = "Letra"  
    elif caractere.isdigit():  
        tipo = "Dígito"  
    else:  
        tipo = "Símbolo"  
    print(f"{codigo:6d} | {caractere:^9} | {tipo}")


