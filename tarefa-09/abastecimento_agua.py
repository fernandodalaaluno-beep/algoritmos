"""
=============================================================
  SISTEMA DE ANÁLISE DE ABASTECIMENTO DE ÁGUA
  Problema 02 - Análise de Estabilidade e Custo
=============================================================
  Autor  : Gerado por Claude (Anthropic)
  Versão : 1.0
  Data   : 2026
=============================================================
"""

import random
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from tabulate import tabulate

# ─────────────────────────────────────────────────────────────
#  CONSTANTES
# ─────────────────────────────────────────────────────────────
DIAS_SIMULACAO = 7
VARIACAO_DEMANDA = 0.20          # ±20%
LIMIAR_CRITICO_M3 = 0.0          # reservatório zerado = crítico

# Limiares de autonomia (dias)
AUTONOMIA_BAIXO = 3
AUTONOMIA_MEDIO = 1

# Paleta de cores do projeto
COR_DEMANDA   = "#2196F3"
COR_ENTREGUE  = "#4CAF50"
COR_PERDIDO   = "#FF5722"
COR_CUSTO     = "#9C27B0"
COR_BAIXO     = "#4CAF50"
COR_MEDIO     = "#FFC107"
COR_ALTO      = "#F44336"


# ─────────────────────────────────────────────────────────────
#  VALIDAÇÃO DE ENTRADA
# ─────────────────────────────────────────────────────────────
def ler_inteiro_positivo(mensagem: str) -> int:
    """Solicita um inteiro positivo (>= 1) ao usuário."""
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor < 1:
                print("  ⚠  O valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("  ⚠  Entrada inválida. Digite um número inteiro.")


def ler_float_positivo(mensagem: str, permite_zero: bool = False) -> float:
    """Solicita um número real positivo ao usuário."""
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
            if not permite_zero and valor <= 0:
                print("  ⚠  O valor deve ser maior que zero. Tente novamente.")
                continue
            if permite_zero and valor < 0:
                print("  ⚠  O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("  ⚠  Entrada inválida. Digite um número real (ex.: 3.5).")


def ler_percentual(mensagem: str) -> float:
    """Solicita um percentual entre 0 e 100."""
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
            if valor < 0 or valor > 100:
                print("  ⚠  Percentual deve estar entre 0 e 100.")
                continue
            return valor
        except ValueError:
            print("  ⚠  Entrada inválida. Digite um número real (ex.: 15.5).")


def ler_nome(mensagem: str) -> str:
    """Solicita um nome não vazio."""
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("  ⚠  O nome não pode ser vazio.")


# ─────────────────────────────────────────────────────────────
#  COLETA DE DADOS
# ─────────────────────────────────────────────────────────────
def coletar_dados_bairros(n: int) -> list[dict]:
    """Coleta os dados de N bairros e retorna lista de dicionários."""
    bairros = []
    print()
    for i in range(1, n + 1):
        print(f"  {'─'*40}")
        print(f"  Bairro {i} de {n}")
        print(f"  {'─'*40}")
        b = {}
        b["nome"]         = ler_nome(f"  Nome do bairro            : ")
        b["demanda"]      = ler_float_positivo(f"  Demanda diária (m³)       : ")
        b["capacidade"]   = ler_float_positivo(f"  Capacidade do reservatório (m³): ")
        b["vol_inicial"]  = ler_float_positivo(
            f"  Volume inicial disponível (m³) [0 a {b['capacidade']:.1f}]: ",
            permite_zero=True
        )
        # Garante que volume inicial não excede capacidade
        if b["vol_inicial"] > b["capacidade"]:
            print(f"  ⚠  Volume inicial ajustado para a capacidade máxima ({b['capacidade']:.2f} m³).")
            b["vol_inicial"] = b["capacidade"]

        b["perda_pct"]    = ler_percentual(f"  Perda na tubulação (%)    : ")
        b["custo_m3"]     = ler_float_positivo(f"  Custo de bombeamento (R$/m³): ")
        bairros.append(b)
    return bairros


# ─────────────────────────────────────────────────────────────
#  CÁLCULOS DIÁRIOS
# ─────────────────────────────────────────────────────────────
def calcular_metricas(bairro: dict, demanda_dia: float | None = None) -> dict:
    """
    Calcula as métricas para um bairro em um dia.

    Se demanda_dia for None, usa a demanda informada pelo usuário.
    Retorna dicionário com os resultados calculados.
    """
    demanda = demanda_dia if demanda_dia is not None else bairro["demanda"]

    fator_perda    = bairro["perda_pct"] / 100.0
    vol_perdido    = demanda * fator_perda
    vol_entregue   = demanda * (1 - fator_perda)
    custo_diario   = demanda * bairro["custo_m3"]

    # Autonomia: quantos dias o reservatório aguenta com o volume atual
    vol_disponivel = bairro.get("vol_atual", bairro["vol_inicial"])
    if vol_entregue > 0:
        autonomia = vol_disponivel / vol_entregue
    else:
        autonomia = float("inf")  # sem consumo → sem limite

    # Classificação de risco
    if autonomia > AUTONOMIA_BAIXO:
        risco = "Baixo"
    elif autonomia >= AUTONOMIA_MEDIO:
        risco = "Médio"
    else:
        risco = "Alto"

    return {
        "vol_entregue" : vol_entregue,
        "vol_perdido"  : vol_perdido,
        "custo_diario" : custo_diario,
        "autonomia"    : autonomia,
        "risco"        : risco,
        "demanda_efetiva": demanda,
    }


# ─────────────────────────────────────────────────────────────
#  EXIBIÇÃO DE TABELA
# ─────────────────────────────────────────────────────────────
def exibir_tabela(bairros: list[dict], metricas: list[dict]) -> None:
    """Imprime tabela formatada com os resultados."""
    cabecalho = [
        "Bairro",
        "Demanda\n(m³/dia)",
        "Vol. Entregue\n(m³/dia)",
        "Vol. Perdido\n(m³/dia)",
        "Custo Diário\n(R$)",
        "Autonomia\n(dias)",
        "Risco",
    ]

    linhas = []
    for b, m in zip(bairros, metricas):
        aut = f"{m['autonomia']:.2f}" if m["autonomia"] != float("inf") else "∞"
        linhas.append([
            b["nome"],
            f"{b['demanda']:.2f}",
            f"{m['vol_entregue']:.2f}",
            f"{m['vol_perdido']:.2f}",
            f"R$ {m['custo_diario']:.2f}",
            aut,
            m["risco"],
        ])

    print("\n" + "="*70)
    print("  RESULTADO DA ANÁLISE — DIA INICIAL")
    print("="*70)
    print(tabulate(linhas, headers=cabecalho, tablefmt="rounded_outline",
                   stralign="center", numalign="center"))


def identificar_bairro_critico(bairros: list[dict], metricas: list[dict]) -> None:
    """Identifica e exibe o bairro mais crítico (menor autonomia)."""
    idx_critico = min(range(len(metricas)), key=lambda i: metricas[i]["autonomia"])
    b = bairros[idx_critico]
    m = metricas[idx_critico]
    aut = f"{m['autonomia']:.2f} dias" if m["autonomia"] != float("inf") else "∞"

    print("\n" + "─"*70)
    print("  🔴  BAIRRO MAIS CRÍTICO")
    print("─"*70)
    print(f"  Nome       : {b['nome']}")
    print(f"  Autonomia  : {aut}")
    print(f"  Nível de risco: {m['risco']}")
    print("─"*70 + "\n")


# ─────────────────────────────────────────────────────────────
#  GRÁFICOS — ANÁLISE INICIAL
# ─────────────────────────────────────────────────────────────
def plotar_graficos_analise(bairros: list[dict], metricas: list[dict]) -> None:
    """Gera os três gráficos da análise inicial (dia base)."""
    nomes   = [b["nome"] for b in bairros]
    n       = len(nomes)
    x       = np.arange(n)
    largura = 0.35

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("Sistema de Abastecimento de Água — Análise Inicial",
                 fontsize=15, fontweight="bold", y=1.01)

    # ── Gráfico 1: Demanda vs Volume Entregue ──────────────────
    ax1 = axes[0]
    demandas   = [b["demanda"] for b in bairros]
    entregues  = [m["vol_entregue"] for m in metricas]
    bar1 = ax1.bar(x - largura/2, demandas,  largura, label="Demanda",        color=COR_DEMANDA,  alpha=0.85)
    bar2 = ax1.bar(x + largura/2, entregues, largura, label="Vol. Entregue",  color=COR_ENTREGUE, alpha=0.85)
    ax1.set_title("Demanda vs Volume Entregue", fontweight="bold")
    ax1.set_xlabel("Bairros")
    ax1.set_ylabel("Volume (m³/dia)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(nomes, rotation=30, ha="right")
    ax1.legend()
    ax1.grid(axis="y", linestyle="--", alpha=0.5)
    _rotular_barras(ax1, bar1)
    _rotular_barras(ax1, bar2)

    # ── Gráfico 2: Custo Diário ────────────────────────────────
    ax2 = axes[1]
    custos = [m["custo_diario"] for m in metricas]
    bars   = ax2.bar(nomes, custos, color=COR_CUSTO, alpha=0.85)
    ax2.set_title("Custo Diário de Bombeamento", fontweight="bold")
    ax2.set_xlabel("Bairros")
    ax2.set_ylabel("Custo (R$)")
    ax2.set_xticks(range(len(nomes)))
    ax2.set_xticklabels(nomes, rotation=30, ha="right")
    ax2.grid(axis="y", linestyle="--", alpha=0.5)
    _rotular_barras(ax2, bars, prefixo="R$")

    # ── Gráfico 3: Distribuição de Risco ──────────────────────
    ax3 = axes[2]
    contagem = {"Baixo": 0, "Médio": 0, "Alto": 0}
    for m in metricas:
        contagem[m["risco"]] += 1

    labels_risco = [k for k, v in contagem.items() if v > 0]
    valores_risco = [v for v in contagem.values() if v > 0]
    cores_risco   = []
    for k in labels_risco:
        if k == "Baixo":  cores_risco.append(COR_BAIXO)
        elif k == "Médio": cores_risco.append(COR_MEDIO)
        else:             cores_risco.append(COR_ALTO)

    if len(labels_risco) == 1:
        # Apenas um nível → gráfico de barra simples
        ax3.bar(labels_risco, valores_risco, color=cores_risco, alpha=0.85)
        ax3.set_ylabel("Quantidade de bairros")
    else:
        wedges, texts, autotexts = ax3.pie(
            valores_risco,
            labels=labels_risco,
            colors=cores_risco,
            autopct="%1.0f%%",
            startangle=90,
            wedgeprops=dict(edgecolor="white", linewidth=1.5),
        )
        for at in autotexts:
            at.set_fontweight("bold")

    ax3.set_title("Distribuição de Níveis de Risco", fontweight="bold")

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/grafico_analise_inicial.png",
                dpi=150, bbox_inches="tight")
    print("  📊  Gráfico salvo: grafico_analise_inicial.png")
    plt.show()


def _rotular_barras(ax, bars, prefixo: str = "") -> None:
    """Adiciona rótulos acima de cada barra."""
    for bar in bars:
        h = bar.get_height()
        label = f"{prefixo}{h:.1f}" if not prefixo else f"{prefixo} {h:.1f}"
        ax.text(
            bar.get_x() + bar.get_width() / 2.0, h * 1.01,
            label, ha="center", va="bottom", fontsize=8
        )


# ─────────────────────────────────────────────────────────────
#  SIMULAÇÃO DE 7 DIAS
# ─────────────────────────────────────────────────────────────
def simular_7_dias(bairros: list[dict]) -> tuple[list[list[float]], list[list[str]]]:
    """
    Simula o sistema por DIAS_SIMULACAO dias com demanda variável (±20%).

    Retorna:
        historico_volumes : lista[bairro][dia] com o volume disponível ao fim de cada dia
        historico_riscos  : lista[bairro][dia] com o nível de risco de cada dia
    """
    # Inicializa volumes
    volumes_atuais = [b["vol_inicial"] for b in bairros]

    historico_volumes = [[] for _ in bairros]
    historico_riscos  = [[] for _ in bairros]

    print("\n" + "="*70)
    print("  SIMULAÇÃO DE 7 DIAS")
    print("="*70)

    for dia in range(1, DIAS_SIMULACAO + 1):
        alertas_dia = []
        print(f"\n  Dia {dia}:")

        for i, bairro in enumerate(bairros):
            # Demanda com variação aleatória ±20%
            fator      = 1 + random.uniform(-VARIACAO_DEMANDA, VARIACAO_DEMANDA)
            demanda_d  = bairro["demanda"] * fator

            # Volume disponível atual (atualizado dia a dia)
            bairro["vol_atual"] = volumes_atuais[i]

            m = calcular_metricas(bairro, demanda_dia=demanda_d)

            # Atualiza volume: subtrai o que foi retirado do reservatório
            # Assume-se que o reservatório abastece a demanda diária
            novo_volume = volumes_atuais[i] - m["vol_entregue"]
            novo_volume = max(0.0, novo_volume)   # não pode ser negativo
            novo_volume = min(novo_volume, bairro["capacidade"])  # não supera capacidade
            volumes_atuais[i] = novo_volume

            historico_volumes[i].append(novo_volume)
            historico_riscos[i].append(m["risco"])

            situacao = "🔴 CRÍTICO" if novo_volume <= 0 else f"  vol={novo_volume:.1f} m³"
            print(f"    {bairro['nome']:20s}  dem={demanda_d:.1f} m³  {situacao}  risco={m['risco']}")

            if novo_volume <= 0:
                alertas_dia.append(bairro["nome"])

        if alertas_dia:
            print(f"\n  ⚠  Bairros em situação CRÍTICA no Dia {dia}: {', '.join(alertas_dia)}")

    return historico_volumes, historico_riscos


def plotar_simulacao(bairros: list[dict], historico_volumes: list[list[float]]) -> None:
    """Gráfico de linhas com a evolução dos volumes ao longo dos 7 dias."""
    dias = list(range(1, DIAS_SIMULACAO + 1))
    cmap = plt.get_cmap("tab10")

    fig, ax = plt.subplots(figsize=(12, 6))
    for i, bairro in enumerate(bairros):
        ax.plot(dias, historico_volumes[i],
                marker="o", linewidth=2, markersize=6,
                label=bairro["nome"], color=cmap(i % 10))

        # Marca com X quando o volume zera
        for d, v in enumerate(historico_volumes[i]):
            if v <= 0:
                ax.scatter(dias[d], 0, color="red", marker="X", s=120, zorder=5)

    ax.axhline(0, color="red", linewidth=1.2, linestyle="--", label="Volume zero (crítico)")
    ax.set_title("Evolução do Volume dos Reservatórios — 7 Dias", fontsize=14, fontweight="bold")
    ax.set_xlabel("Dia")
    ax.set_ylabel("Volume disponível (m³)")
    ax.set_xticks(dias)
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/grafico_simulacao_7dias.png",
                dpi=150, bbox_inches="tight")
    print("\n  📊  Gráfico salvo: grafico_simulacao_7dias.png")
    plt.show()


# ─────────────────────────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────────────────────
def main() -> None:
    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   SISTEMA DE ANÁLISE DE ABASTECIMENTO DE ÁGUA            ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()

    # ── 1. Número de bairros ────────────────────────────────────
    n = ler_inteiro_positivo("  Informe o número de bairros a analisar: ")

    # ── 2. Coleta de dados ─────────────────────────────────────
    bairros = coletar_dados_bairros(n)

    # ── 3. Cálculo inicial (usando demanda informada) ──────────
    metricas = [calcular_metricas(b) for b in bairros]

    # ── 4. Tabela de resultados ────────────────────────────────
    exibir_tabela(bairros, metricas)

    # ── 5. Bairro mais crítico ─────────────────────────────────
    identificar_bairro_critico(bairros, metricas)

    # ── 6. Gráficos da análise inicial ────────────────────────
    print("  Gerando gráficos da análise inicial...")
    plotar_graficos_analise(bairros, metricas)

    # ── 7. Simulação de 7 dias ─────────────────────────────────
    resposta = input("  Deseja executar a simulação de 7 dias? [s/n]: ").strip().lower()
    if resposta in ("s", "sim", "y", "yes"):
        historico_volumes, _ = simular_7_dias(bairros)
        plotar_simulacao(bairros, historico_volumes)
    else:
        print("  Simulação ignorada.")

    print("\n  ✅  Análise concluída. Até logo!\n")


if __name__ == "__main__":
    # Verifica dependências
    try:
        import tabulate  # noqa: F401
    except ImportError:
        print("  Instalando dependência 'tabulate'...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate", "-q"])

    main()
