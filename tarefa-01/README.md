# Exercícios Propostos — Tipos de Dados e Identificadores

Este módulo apresenta a resolução dos exercícios teóricos e analíticos sobre a classificação de tipos primitivos de dados e as regras de validação para a criação de identificadores (variáveis) em algoritmos.

---

## 1. Classificação de Tipos de Dados

Classificação dos dados primitivos de acordo com sua natureza lúdica e representação em memória:
* **I** = Inteiro | **R** = Real | **L** = Literal (String) | **B** = Lógico (Booleano) | **N** = Não definido a priori

| Dado | Tipo | Justificativa / Observação |
| :--- | :---: | :--- |
| `0.21` | **R** | Valor numérico decimal. |
| `"0."` | **L** | Delimitado por aspas, tratado como texto. |
| `0,35` | **R** | Representação decimal (notação com vírgula). |
| `.T.` | **B** | Representação clássica de valor lógico Verdadeiro (*True*). |
| `"+3257"` | **L** | Sequência de caracteres numéricos gravada como texto devido às aspas. |
| `".F."` | **L** | Texto contendo os caracteres `.F.` (aspas delimitadoras). |
| `.V` | **N** | Sintaxe incompleta para operador ou valor lógico. |
| `C` | **N** | Caractere isolado sem delimitadores (pode ser uma variável não declarada). |
| `1` | **I** | Valor numérico inteiro positivo. |
| `1%` | **N** | Expressão incompleta ou caractere especial inválido para tipo primitivo puro. |
| `.F.` | **B** | Representação clássica de valor lógico Falso (*False*). |
| `+3257` | **I** | Valor numérico inteiro com sinal positivo explícito. |
| `± 3` | **I** | Indicação de valor numérico inteiro (considerando o valor absoluto). |
| `"abc"` | **L** | Cadeia de caracteres puramente textual. |
| `Maria` | **N** | Texto sem aspas; interpretado sintaticamente como um identificador. |
| `.V.` | **B** | Representação clássica de valor lógico Verdadeiro (*True*). |
| `"José"` | **L** | Cadeia de caracteres textual delimitada por aspas. |
| `-0.001` | **R** | Valor numérico real negativo. |
| `"a"` | **L** | Caractere individual delimitado por aspas. |
| `"-0.0"` | **L** | Cadeia de caracteres contendo valor numérico sob aspas. |
| `F` | **N** | Identificador ou caractere isolado sem delimitador de texto. |
| `+36` | **I** | Valor numérico inteiro positivo. |

---

## 2. Validação de Identificadores (Variáveis)

Análise de nomenclatura de variáveis com base nas regras de escopo algorítmico (Não iniciar com números, não conter espaços ou caracteres especiais exceto underline `_`).
* **C** = Correto | **I** = Incorreto

* `( C ) valor` — **Correto:** Inicia com letra e possui apenas caracteres alfanuméricos.
* `( C ) _b242` — **Correto:** O caractere *underline* (`_`) é permitido para iniciar identificadores.
* `( I ) nota*do*aluno` — **Incorreto:** O caractere especial asterisco (`*`) é um operador aritmético e é proibido.
* `( C ) a1b2c3` — **Correto:** Mescla letras e números iniciando por letra.
* `( I ) 3 x 4` — **Incorreto:** Inicia com número e contém espaços vazios no nome.
* `( C ) Maria` — **Correto:** Inicia com caractere alfabético válido.
* `( I ) km/h` — **Incorreto:** A barra (`/`) é um caractere especial reservado para operações de divisão.
* `( C ) xyz` — **Correto:** Identificador simples perfeitamente válido.
* `( I ) nome empresa` — **Incorreto:** Contém espaço em branco, o que quebra a leitura sintática do compilador.
* `( C ) sala_215` — **Correto:** Uso correto do *underline* para separar palavras em um identificador composto.
* `( I ) "nota"` — **Incorreto:** Uso de aspas transforma o identificador em um dado literal (String).
* `( I ) ah!` — **Incorreto:** O ponto de exclamação (`!`) é um caractere especial inválido para nomes de variáveis.
