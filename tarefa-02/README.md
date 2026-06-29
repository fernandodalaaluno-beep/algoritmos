# Tarefa 02 — Estruturas Condicionais e de Decisão

Este módulo documenta a resolução prática de problemas utilizando estruturas de fluxo condicional (`if`, `elif`, `else`) na linguagem Python.

---

## 📋 Enunciado do Problema
Desenvolver algoritmos que permitam ao sistema tomar decisões lógicas automáticas com base em dados de entrada fornecidos pelo usuário. Os exercícios cobrem validações numéricas, intervalos de dados e testes de condições lógicas compostas.

## 💡 Ideia da Solução
A solução foi estruturada utilizando a sintaxe nativa do Python para desvios condicionais:
1. **Entrada de Dados:** Captura dos valores através da função `input()` e conversão para os tipos adequados (`int` ou `float`).
2. **Processamento Sintático:** Aplicação de blocos condicionais encadeados para testar múltiplas variáveis de forma otimizada, evitando redundâncias em memória.
3. **Saída:** Retorno claro ao usuário final sobre a condição validada.

## 💻 Exemplo de Implementação Estrutural
```python
# Estrutura base utilizada nas resoluções
valor = float(input("Digite um número: "))

if valor > 0:
    print("O valor inserido é Positivo.")
elif valor < 0:
    print("O valor inserido é Negativo.")
else:
    print("O valor inserido é Nulo (Zero).")
