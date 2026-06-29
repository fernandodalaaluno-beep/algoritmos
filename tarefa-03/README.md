# Tarefa 03 — Geração e Análise Comparativa de Exercícios com LLMs

**Estudante:** Fernando Da Silva Dala  
**Matrícula:** 2610100511  
**Disciplina:** Algoritmos e Programação Aplicados à Engenharia  
**Professor:** Prof. Diego Luis Kreutz  
**Data de Entrega:** 10 de abril de 2026  

---

## 📂 Índice de Seções (Clique para navegar)

* [➔ 1. Prompts Utilizados](#1-prompts-utilizados)
* [➔ 2. Análise da Engenharia Elétrica](#2-análise-da-engenharia-elétrica)
* [➔ 3. Análise da Engenharia Mecânica](#3-análise-da-engenharia-mecânica)
* [➔ 4. Análise da Engenharia de Telecomunicações](#4-análise-da-engenharia-de-telecomunicações)
* [➔ 5. Quadro Comparativo e Conclusão](#5-quadro-comparativo-e-conclusão)

---

## 1. Prompts Utilizados

### 1.1 Prompt Principal (Idêntico para os 3 modelos)
> **Texto do prompt enviado a Claude, Gemini e DeepSeek:** > *Você é professor universitário especialista em algoritmos aplicados à engenharia. Gere uma lista com exatamente 10 exercícios de algoritmos distribuídos entre:* > * *Engenharia Elétrica: 4 exercícios* > * *Engenharia Mecânica: 3 exercícios* > * *Engenharia de Telecomunicações: 3 exercícios* >   
> *Para CADA exercício forneça obrigatoriamente:* > * *1. Enunciado: contextualizado em aplicação real de engenharia (2-4 frases).* > * *2. Pseudocódigo: em português, com ALGORITMO, VARIÁVEIS, INÍCIO, FIM, SE/SENÃO, ENQUANTO, PARA, LEIA, ESCREVA.* > * *3. Código Python: funcional, com funções nomeadas e chamada ao final.*

### 1.2 Modelos Testados
* **LLM 1:** Claude — Sonnet 4.6 (Anthropic) | claude.ai
* **LLM 2:** Gemini (Google DeepMind) | gemini.google.com
* **LLM 3:** DeepSeek (DeepSeek AI) | chat.deepseek.com

---

## 2. Análise da Engenharia Elétrica

Esta seção avalia os 4 problemas gerados voltados para sistemas de potência, dimensionamento de circuitos e análise de redes elétricas.

### Avaliação dos Modelos:
* **Claude (Sonnet 4.6):** Excelente na aplicação das fórmulas de queda de tensão e impedância. O código Python gerado respeitou todas as boas práticas, incluindo tratamento de exceções para divisões por zero em cálculos de curto-circuito.
* **Gemini:** Forneceu enunciados muito realistas sobre gerenciamento de carga residencial, porém o pseudocódigo pecou em não declarar rigidamente o tipo das variáveis elétricas (como `float` para correntes).
* **DeepSeek:** Seguiu estritamente o escopo técnico. Os códigos Python funcionaram de primeira, embora o pseudocódigo tenha utilizado uma sintaxe ligeiramente misturada com C++.

---

## 3. Análise da Engenharia Mecânica

Análise dos 3 exercícios práticos focados em termodinâmica, fadiga de materiais e dinâmica de fluidos.

### Avaliação dos Modelos:
* **Claude (Sonnet 4.6):** Propôs um excelente simulador de ensaio de tração com cálculo de deformação específica. O algoritmo utilizou matrizes de forma impecável para registrar as tensões.
* **Gemini:** Focou em transferência de calor. Apresentou lógica correta no uso de estruturas `ENQUANTO` para iterações de temperatura, mas omitiu os comentários explicativos exigidos de forma secundária.
* **DeepSeek:** Errou a lógica de iteração em uma das tentativas da simulação estrutural (invertendo o incremento do loop), exigindo um prompt de correção complementar.

---

## 4. Análise da Engenharia de Telecomunicações

Análise dos 3 exercícios abordando propagação de ondas, ganho de antenas e perda de pacotes em redes de dados.

### Avaliação dos Modelos:
* **Claude (Sonnet 4.6):** Mostrou-se superior ao modelar a atenuação em espaço livre com a fórmula de Friis. Código Python limpo, modular e de fácil leitura.
* **Gemini:** Estruturou muito bem a simulação estática de ganho em antenas Yagi, mas entregou uma função sem parâmetros no Python, quebrando o dinamismo da aplicação.
* **DeepSeek:** Forneceu ótimos enunciados de modulação de sinais, mas falhou na primeira tentativa ao esquecer de incluir a chamada final da função no bloco Python.

---

## 5. Quadro Comparativo e Conclusão

### Tabela de Desempenho

| Critério de Avaliação | Claude (Sonnet 4.6) | Gemini (Google) | DeepSeek AI |
| :--- | :---: | :---: | :---: |
| **Precisão Técnica (Engenharia)** | Excelente | Bom | Regular |
| **Sintaxe do Pseudocódigo** | Perfeita | Regular | Bom |
| **Estrutura do Código Python** | Perfeita | Bom | Regular (Omitiu chamadas) |
| **Aderência ao Prompt Original** | 100% | 90% | 80% (Inverteu iterações) |
| **Necessidade de Refinamento** | Nenhuma | Pouca | Alta |

### Conclusão Geral
O **Claude (Sonnet 4.6)** provou ser o modelo mais robusto para a engenharia de prompts acadêmica, entregando códigos limpos e pseudocódigos sem misturar sintaxes. O **Gemini** destaca-se pela excelente criatividade contextual dos enunciados, embora falte rigor técnico em algumas estruturas de código. O **DeepSeek** é altamente capaz, porém requer maior fiscalização por apresentar falhas lógicas e esquecimentos em loops e chamadas funcionais complexas.
