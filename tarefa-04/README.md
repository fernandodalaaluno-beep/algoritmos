# Tarefa 04 — Algoritmos Avançados e Análise de Sistemas de Engenharia

**Estudante:** Fernando Da Silva Dala  
**Matrícula:** 2610100511  
**Disciplina:** Algoritmos e Programação Aplicados à Engenharia  
**Professor:** Prof. Diego Luis Kreutz  
**Data de Entrega:** 10 de abril de 2026  

Este módulo apresenta a documentação detalhada e a implementação de lógica computacional para a resolução de problemas reais de engenharia, integrando pseudocódigos formais e scripts executáveis em Python. Clique em qualquer um dos links do menu para visualizar o conteúdo diretamente na tela.

---

## 📂 Índice Interativo (Clique para navegar)

* [➔ Exercício 1: Telemetria de Voo e Conversão de Tempo](#1-telemetria-de-voo-e-conversão-de-tempo)
* [➔ Exercício 2: Análise e Cálculo da Ponte de Wheatstone](#2-análise-e-cálculo-da-ponte-de-wheatstone)
* [➔ Exercício 3: Cálculo de Nota Fiscal com Tributos em Cascata](#3-cálculo-de-nota-fiscal-com-tributos-em-cascata)
* [➔ Exercício 4: Laudo Geotécnico e Classificação de Solos](#4-laudo-geotécnico-e-classificação-de-solos)
* [➔ Exercício 5: Inspeção de Solda e Velocidade de Esteira Eletrônica](#5-inspeção-de-solda-e-velocidade-de-esteira-eletrônica)

---

## 1. Telemetria de Voo e Conversão de Tempo

**Descrição:** Algoritmo focado no tratamento de dados temporais brutos capturados por sistemas de telemetria aeroespacial. O programa recebe o tempo total de missão expresso em segundos inteiros e realiza a decomposição matemática exata para o formato macroscópico de dias, horas, minutos e segundos restantes.

### 📝 Pseudocódigo Estruturado

dias <- t DIV 86400
resto1 <- t MOD 86400
horas <- resto1 DIV 3600
resto2 <- resto1 MOD 3600
minutos <- resto2 DIV 60
segundos <- resto2 MOD 60

ESCREVA dias, " dia(s), ", horas, "h:", minutos, "m:", segundos, "s"



### 💻 Código Python Equivalente
```python
def converter_telemetria():
    t = int(input("Digite o tempo total em segundos: "))
    
    dias = t // 86400
    resto1 = t % 86400
    horas = resto1 // 3600
    resto2 = resto1 % 3600
    minutos = resto2 // 60
    segundos = resto2 % 60
    
    print(f"\nResultado da Conversão:")
    print(f"{dias} dia(s), {horas:02d}:{minutos:02d}:{segundos:02d}")

if __name__ == "__main__":
    converter_telemetria()

## 2. Análise e Cálculo da Ponte de Wheatstone

### 📝 Pseudocódigo Estruturado

ALGORITMO PonteDeWheatstone
VARIÁVEIS
    R1, R2, R3, Rx, R_total, V_fonte, I_total, P_total: REAL
    Equilibrio: CARACTERE
INÍCIO
    LEIA R1, R2, R3, V_fonte
    
    SE R1 = 0 ENTÃO
        ESCREVA "ERRO: R1 não pode ser zero para o cálculo."
        PARE
    FIM_SE
    
    Rx <- (R3 * R2) / R1
    R_total <- ((R1 + Rx) * (R2 + R3)) / (R1 + Rx + R2 + R3)
    I_total <- V_fonte / R_total
    P_total <- V_fonte * I_total
    
    SE (R1 * Rx) = (R2 * R3) ENTÃO
        Equilibrio <- "SIM"
    SENÃO
        Equilibrio <- "NÃO"
    FIM_SE
    
    ESCREVA "Rx = ", Rx, " Ohms"
    ESCREVA "Resistência Total = ", R_total, " Ohms"
    ESCREVA "Corrente Total = ", I_total, " A"
    ESCREVA "Potência Total = ", P_total, " W"
    ESCREVA "Ponte em Equilíbrio: ", Equilibrio
FIM

### 💻 Código Python Equivalente

def analisar_ponte_wheatstone():
    try:
        r1 = float(input("Digite R1 (Ohms): "))
        r2 = float(input("Digite R2 (Ohms): "))
        r3 = float(input("Digite R3 (Ohms): "))
        v_fonte = float(input("Digite a tensão da fonte (V): "))
        
        if r1 == 0:
            print("ERRO: R1 não pode ser zero.")
            return
            
        rx = (r3 * r2) / r1
        r_total = ((r1 + rx) * (r2 + r3)) / (r1 + rx + r2 + r3)
        i_total = v_fonte / r_total
        p_total = v_fonte * i_total
        
        equilibrio = "SIM" if abs((r1 * rx) - (r2 * r3)) < 1e-5 else "NÃO"
        
        print(f"\n--- Relatório Técnico da Ponte ---")
        print(f"Rx calculado: {rx:.2f} Ω")
        print(f"Resistência Equivalente: {r_total:.2f} Ω")
        print(f"Corrente da Fonte: {i_total:.4f} A")
        print(f"Potência Ativa Total: {p_total:.2f} W")
        print(f"Ponte em Equilíbrio: {equilibrio}")
    except ValueError:
        print("Erro: Digite apenas valores numéricos válidos.")

if __name__ == "__main__":
    analisar_ponte_wheatstone()

## 3. Cálculo de Nota Fiscal com Tributos em Cascata
### 📝 Pseudocódigo Estruturado

ALGORITMO NotaFiscalTributos
VARIÁVEIS
    Preco_Fabrica, aliq_ipi, aliq_icms, aliq_pis_cofins: REAL
    ipi, base_icms, icms, base_pc, pis_cofins, Preco_final, Carga_total: REAL
INÍCIO
    LEIA Preco_Fabrica, aliq_ipi, aliq_icms, aliq_pis_cofins
    
    ipi <- Preco_Fabrica * (aliq_ipi / 100)
    base_icms <- Preco_Fabrica + ipi
    icms <- base_icms * (aliq_icms / 100)
    base_pc <- base_icms + icms
    pis_cofins <- base_pc * (aliq_pis_cofins / 100)
    Preco_final <- base_pc + pis_cofins
    Carga_total <- ((Preco_final - Preco_Fabrica) / Preco_Fabrica) * 100
    
    ESCREVA "Preço de Fábrica: R$ ", Preco_Fabrica
    ESCREVA "IPI: R$ ", ipi
    ESCREVA "Base ICMS: R$ ", base_icms
    ESCREVA "ICMS: R$ ", icms
    ESCREVA "PIS/COFINS: R$ ", pis_cofins
    ESCREVA "Preço Final de Venda: R$ ", Preco_final
    ESCREVA "Carga Tributária Total Adicionada: ", Carga_total, "%"
FIM

### 💻 Código Python Equivalente

def calcular_nota_fiscal():
    preco_fabrica = float(input("Preço de Fábrica (R$): "))
    aliq_ipi = float(input("Alíquota IPI (%): "))
    aliq_icms = float(input("Alíquota ICMS (%): "))
    aliq_pis_cofins = float(input("Alíquota PIS/COFINS (%): "))
    
    ipi = preco_fabrica * (aliq_ipi / 100)
    base_icms = preco_fabrica + ipi
    icms = base_icms * (aliq_icms / 100)
    base_pc = base_icms + icms
    pis_cofins = base_pc * (aliq_pis_cofins / 100)
    preco_final = base_pc + pis_cofins
    carga_total = ((preco_final - preco_fabrica) / preco_fabrica) * 100
    
    print(f"\n====== Memória de Cálculo Fiscal ======")
    print(f"Preço Base Fábrica : R$ {preco_fabrica:10.2f}")
    print(f"(+) Valor IPI      : R$ {ipi:10.2f}")
    print(f"(=) Base ICMS      : R$ {base_icms:10.2f}")
    print(f"(+) Valor ICMS     : R$ {icms:10.2f}")
    print(f"(+) Valor PIS/COF  : R$ {pis_cofins:10.2f}")
    print(f"---------------------------------------")
    print(f"(=) PREÇO CONSUMIDOR: R$ {preco_final:10.2f}")
    print(f"Impacto Tributário : {carga_total:.2f}% sobre a fábrica.")

if __name__ == "__main__":
    calcular_nota_fiscal()

## 4. Laudo Geotécnico e Classificação de Solos
### 📝 Pseudocódigo Estruturado

ALGORITMO LaudoGeotecnico
VARIÁVEIS
    spt: INTEIRO
    carga_cap: REAL
INÍCIO
    LEIA spt, carga_cap
    
    SE (spt <= 5) OU (carga_cap < 80) ENTÃO
        ESCREVA "LAUDO: Inapto. Solo excessivamente fraco - Reforço estrutural obrigatório."
    SENÃO SE (spt < 10) OU (carga_cap < 150) ENTÃO
        ESCREVA "LAUDO: Restrito. Fundação especial recomendada."
        SE spt < 10 ENTÃO
            ESCREVA "Motivo: Resistência Penetração (SPT) abaixo do limite mínimo (<10)."
        FIM_SE
        SE carga_cap < 150 ENTÃO
            ESCREVA "Motivo: Capacidade de carga abaixo do patamar de segurança (<150 kPa)."
        FIM_SE
    SENÃO SE (spt >= 30) E (carga_cap >= 300) ENTÃO
        ESCREVA "LAUDO: Excelente. Solo de altíssima capacidade portante."
    SENÃO
        ESCREVA "LAUDO: Adequado. Construção e fundação convencional viável."
    FIM_SE
FIM

### 💻 Código Python Equivalente

def gerar_laudo_geotecnico():
    spt = int(input("Digite o índice de penetração SPT: "))
    carga_cap = float(input("Digite a capacidade de carga do solo (kPa): "))
    
    print(f"\n--- Resultado da Análise de Solo ---")
    if spt <= 5 or carga_cap < 80:
        print("STATUS: INAPTO\nDiagnóstico: Solo muito instável. Intervenção de engenharia urgente.")
    elif spt < 10 or carga_cap < 150:
        print("STATUS: RESTRITO\nDiagnóstico: Exige fundações profundas/especiais.")
        if spt < 10:
            print(" -> Alerta: SPT crítico (< 10 golpes).")
        if carga_cap < 150:
            print(" -> Alerta: Capacidade de carga deficiente (< 150 kPa).")
    elif spt >= 30 and carga_cap >= 300:
        print("STATUS: EXCELENTE\nDiagnóstico: Solo de alta compacidade. Ideal para cargas elevadas.")
    else:
        print("STATUS: ADEQUADO\nDiagnóstico: Solo estável. Permite sapatas e fundações convencionais.")

if __name__ == "__main__":
    gerar_laudo_geotecnico()

## 5. Inspeção de Solda e Velocidade de Esteira Eletrônica
### 📝 Pseudocódigo Estruturado

ALGORITMO InspecaoLinhaDeProducao
VARIÁVEIS
    resistencia_nominal, resistencia_medida, tolerancia_abs, desvio, desvio_pct: REAL
    velocidade_alvo, velocidade_atual: REAL
INÍCIO
    // --- Módulo A: Controle de Qualidade Metalúrgica (Soldagem)
    LEIA resistencia_nominal, resistencia_medida
    tolerancia_abs <- resistencia_nominal * 0.08
    desvio <- resistencia_medida - resistencia_nominal
    desvio_pct <- (desvio / resistencia_nominal) * 100
    
    SE (desvio >= -tolerancia_abs) E (desvio <= tolerancia_abs) ENTÃO
        ESCREVA "Inspeção Concluída: Solda APROVADA no ensaio."
    SENÃO
        ESCREVA "Inspeção Concluída: Solda REPROVADA por desvio excessivo."
    FIM_SE
    ESCREVA "Desvio Registrado: ", desvio, " MPa (", desvio_pct, " %)"
    
    // --- Módulo B: Monitoramento de Velocidade da Esteira Transmissora
    LEIA velocidade_alvo, velocidade_atual
    
    SE velocidade_atual > (velocidade_alvo * 1.10) ENTÃO
        ESCREVA "ALERTA CINEMÁTICO: Velocidade ALTA - Risco severo de falha no posicionamento mecânico."
    SENÃO SE velocidade_atual < (velocidade_alvo * 0.90) ENTÃO
        ESCREVA "ALERTA CINEMÁTICO: Velocidade BAIXA - Formação de gargalo na linha de montagem."
    SENÃO
        ESCREVA "Sistema Estável: Velocidade Operacional Nominal (OK)."
    FIM_SE
FIM

### 💻 Código Python Equivalente

def inspecionar_linha_producao():
    print("=== MÓDULO DE SOLDAGEM ===")
    res_nominal = float(input("Resistência Nominal da Norma (MPa): "))
    res_medida = float(input("Resistência Medida no Ensaio (MPa): "))
    
    tolerancia = res_nominal * 0.08
    desvio = res_medida - res_nominal
    desvio_pct = (desvio / res_nominal) * 100
    
    print(f"\nResultado Metalúrgico:")
    if -tolerancia <= desvio <= tolerancia:
        print("-> SOLDA: APROVADA")
    else:
        print("-> SOLDA: REPROVADA")
    print(f"Desvio Técnico: {desvio:+.2f} MPa ({desvio_pct:+.2f}%)")
    
    print("\n=== MÓDULO DE TRANSPORTE (ESTEIRA) ===")
    vel_alvo = float(input("Velocidade de Projeto Alvo (m/s): "))
    vel_atual = float(input("Velocidade Atual do Sensor (m/s): "))
    
    print(f"\nResultado Cinemático:")
    if vel_atual > vel_alvo * 1.10:
        print("-> ALERTA: VELOCIDADE ALTA (Risco de erro posicional).")
    elif vel_atual < vel_alvo * 0.90:
        print("-> ALERTA: VELOCIDADE BAIXA (Gerando atrasos e gargalos).")
    else:
        print("-> ESTEIRA OPERANDO EM CONDIÇÕES IDEAIS (OK).")

if __name__ == "__main__":
    inspecionar_linha_producao()
