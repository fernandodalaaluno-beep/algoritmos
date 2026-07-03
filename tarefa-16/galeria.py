from pathlib import Path
from dataclasses import dataclass
from html import escape
from datetime import datetime
from collections import Counter
import json
import pandas as pd
import requests

# =========================
# CONFIGURAÇÃO
# =========================
@dataclass
class Config:
    csv: str = "fotos_alegrete.csv"
    html: str = "portal_alegrete.html"
    json_file: str = "catalogo.json"
    relatorio: str = "relatorio_execucao.txt"
    imagens: str = "imagens"
    timeout: int = 10

CFG = Config()
Path(CFG.imagens).mkdir(exist_ok=True)

COLUNAS = [
    "titulo",
    "categoria",
    "imagem",
    "legenda",
    "localizacao",
    "fonte"
]

# =========================
# CSV
# =========================
def criar_csv_exemplo():
    dados = [
        {
            "titulo": "Praça Getúlio Vargas",
            "categoria": "Turismo",
            "imagem": "https://picsum.photos/900/500?1",
            "legenda": "Ponto central de Alegrete",
            "localizacao": "Alegrete-RS",
            "fonte": "https://picsum.photos"
        }
    ]
    pd.DataFrame(dados).to_csv(
        CFG.csv, index=False, encoding="utf-8"
    )

def carregar_dados():
    arquivo = Path(CFG.csv)
    if not arquivo.exists():
        criar_csv_exemplo()
        print("CSV criado automaticamente.")
    df = pd.read_csv(arquivo)
    faltando = set(COLUNAS) - set(df.columns)
    if faltando:
        raise ValueError(f"CSV inválido. Colunas faltando: {faltando}")
    return df

# =========================
# IMAGENS (ROBUSTO)
# =========================
def baixar_imagem(sessao, url, nome):
    destino = Path(CFG.imagens) / f"{nome}.jpg"
    # cache local
    if destino.exists():
        return str(destino)
    # arquivo local direto
    if Path(url).exists():
        return url
    try:
        r = sessao.get(url, timeout=CFG.timeout)
        r.raise_for_status()
        if "image" not in r.headers.get("Content-Type", ""):
            return url
        destino.write_bytes(r.content)
        return str(destino)
    except Exception:
        return url

# =========================
# HTML
# =========================
def criar_card(item):
    return f"""
    <div class="card" data-cat="{escape(item['categoria'])}">
        <img src="{item['arquivo']}" loading="lazy" onerror="this.src='https://picsum.photos/400/300?blur=2'">
        <div class="conteudo">
            <h3>{escape(item['titulo'])}</h3>
            <p>{escape(item['legenda'])}</p>
            <p>📍 {escape(item['localizacao'])}</p>
            <small>{escape(item['categoria'])}</small>
        </div>
    </div>
    """

def gerar_html(cards, categorias, total):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    options = "".join(f"<option>{c}</option>" for c in categorias)
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Catálogo Alegrete</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 30px; background-color: #f4f7f6; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }}
        .card {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.1); }}
        img {{ width: 100%; height: 250px; object-fit: cover; }}
        .conteudo {{ padding: 16px; }}
        .filtros {{ margin: 20px 0; }}
        input, select {{ padding: 8px; margin-right: 10px; border-radius: 6px; border: 1px solid #ccc; }}
    </style>
</head>
<body>
    <h1>Catálogo Digital – Alegrete-RS</h1>
    <p>Total de itens: {total}</p>
    <p>Atualizado em: {data}</p>
    
    <div class="filtros">
        <input id="busca" placeholder="Buscar...">
        <select id="categoria">
            <option>Todas</option>
            {options}
        </select>
    </div>

    <div class="grid">
        {"".join(cards)}
    </div>

    <script>
        const busca = document.getElementById("busca");
        const categoria = document.getElementById("categoria");
        
        function filtrar() {{
            document.querySelectorAll(".card").forEach(card => {{
                const texto = card.innerText.toLowerCase();
                const okBusca = texto.includes(busca.value.toLowerCase());
                const okCat = categoria.value === "Todas" || card.dataset.cat === categoria.value;
                card.style.display = (okBusca && okCat) ? "block" : "none";
            }});
        }}
        
        busca.addEventListener("input", filtrar);
        categoria.addEventListener("change", filtrar);
    </script>
</body>
</html>"""

# =========================
# EXECUÇÃO
# =========================
def executar():
    df = carregar_dados()
    resultado = []
    with requests.Session() as sessao:
        for i, row in df.iterrows():
            print(f"Processando {i+1}/{len(df)}")
            item = row.to_dict()
            item["arquivo"] = baixar_imagem(sessao, item["imagem"], i)
            resultado.append(item)
            
    cards = [criar_card(i) for i in resultado]
    categorias = sorted(Counter(i["categoria"] for i in resultado))
    
    Path(CFG.html).write_text(
        gerar_html(cards, categorias, len(resultado)), encoding="utf-8"
    )
    Path(CFG.json_file).write_text(
        json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    Path(CFG.relatorio).write_text(
        f"PROJETO CONCLUÍDO\nItens: {len(resultado)}\nCategorias: {len(categorias)}\nData: {datetime.now()}\n", 
        encoding="utf-8"
    )
    print("\nExecução finalizada com sucesso.")

if __name__ == "__main__":
    executar()
