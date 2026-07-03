from pathlib import Path
from dataclasses import dataclass
from html import escape
from datetime import datetime
from collections import Counter
import json
import pandas as pd
import requests

# ==========================================
# CONFIGURAÇÃO DO SISTEMA
# ==========================================
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

COLUNAS = ["titulo", "categoria", "imagem", "legenda", "localizacao", "fonte"]

# ==========================================
# GERAÇÃO E MANIPULAÇÃO DE DADOS (CSV)
# ==========================================
def criar_csv_exemplo():
    """Gera um arquivo CSV inicial caso ele não exista."""
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
    pd.DataFrame(dados).to_csv(CFG.csv, index=False, encoding="utf-8")

def carregar_dados():
    """Carrega os dados do CSV e valida as colunas obrigatórias."""
    arquivo = Path(CFG.csv)
    if not arquivo.exists():
        criar_csv_exemplo()
        print("-> CSV de exemplo criado automaticamente.")
    
    df = pd.read_csv(arquivo)
    faltando = set(COLUNAS) - set(df.columns)
    if faltando:
        raise ValueError(f"Erro: O arquivo CSV está inválido. Colunas faltando: {faltando}")
    return df

# ==========================================
# DOWNLOAD ROBUSTO DE IMAGENS (CACHE LOCAL)
# ==========================================
def baixar_imagem(sessao, url, nome):
    """Realiza o download da imagem de forma segura ou reaproveita o cache local."""
    destino = Path(CFG.imagens) / f"{nome}.jpg"
    
    # Se a imagem já existe localmente, reaproveita (Cache)
    if destino.exists():
        return str(destino)
        
    # Se a URL fornecida já for um caminho de arquivo local válido
    if Path(url).exists():
        return url
        
    try:
        r = sessao.get(url, timeout=CFG.timeout)
        r.raise_for_status()
        
        # Garante que o conteúdo baixado é realmente uma imagem
        if "image" not in r.headers.get("Content-Type", "").lower():
            return url
            
        destino.write_bytes(r.content)
        return str(destino)
    except Exception:
        # Em caso de falha de conexão, mantém a URL original para o fallback do HTML
        return url

# ==========================================
# COMPONENTES E GERAÇÃO DA INTERFACE (HTML)
# ==========================================
def criar_card(item):
    """Gera a estrutura HTML de um card individual de conteúdo."""
    return f"""
    <div class="card" data-cat="{escape(str(item['categoria']))}">
        <img src="{item['arquivo']}" loading="lazy" onerror="this.src='https://picsum.photos/400/300?blur=2'">
        <div class="conteudo">
            <h3>{escape(str(item['titulo']))}</h3>
            <p>{escape(str(item['legenda']))}</p>
            <p>📍 {escape(str(item['localizacao']))}</p>
            <small>{escape(str(item['categoria']))}</small>
        </div>
    </div>
    """

def gerar_html(cards, categorias, total):
    """Monta a estrutura de página HTML com os filtros interativos em JavaScript."""
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    options = "".join(f"<option>{escape(c)}</option>" for c in categorias)
    
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo Digital – Alegrete-RS</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 30px; background-color: #f4f7f6; color: #333; }}
        h1 {{ color: #0d2d6e; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-top: 20px; }}
        .card {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.08); transition: transform 0.2s; }}
        .card:hover {{ transform: translateY(-4px); }}
        img {{ width: 100%; height: 230px; object-fit: cover; }}
        .conteudo {{ padding: 16px; }}
        .conteudo h3 {{ margin: 0 0 8px 0; color: #1a4a8a; }}
        .conteudo p {{ margin: 4px 0; font-size: 0.95rem; color: #555; }}
        .conteudo small {{ display: inline-block; margin-top: 8px; background: #e8f4fd; color: #1565c0; padding: 4px 8px; border-radius: 4px; font-weight: bold; }}
        .filtros {{ margin: 20px 0; background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }}
        input, select {{ padding: 10px; margin-right: 10px; border-radius: 6px; border: 1px solid #ccc; font-size: 0.95rem; }}
        input {{ width: 250px; }}
    </style>
</head>
<body>
    <h1>Catálogo Digital – Alegrete-RS</h1>
    <p><strong>Total de itens:</strong> {total} | <strong>Atualizado em:</strong> {data}</p>
    
    <div class="filtros">
        <input id="busca" placeholder="Buscar por título ou descrição...">
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
            const termo = busca.value.toLowerCase();
            const catSelecionada = categoria.value;
            
            document.querySelectorAll(".card").forEach(card => {{
                const texto = card.innerText.toLowerCase();
                const catCard = card.dataset.cat;
                
                const okBusca = texto.includes(termo);
                const okCat = catSelecionada === "Todas" || catCard === catSelecionada;
                
                card.style.display = (okBusca && okCat) ? "block" : "none";
            }});
        }}
        
        busca.addEventListener("input", filtrar);
        categoria.addEventListener("change", filtrar);
    </script>
</body>
</html>"""

# ==========================================
# FLUXO PRINCIPAL DE EXECUÇÃO
# ==========================================
def executar():
    print("Iniciando processamento do catálogo...")
    df = carregar_dados()
    resultado = []
    
    with requests.Session() as sessao:
        for i, row in df.iterrows():
            print(f"-> Processando item {i+1}/{len(df)}: {row['titulo']}")
            item = row.to_dict()
            item["arquivo"] = baixar_imagem(sessao, item["imagem"], i)
            resultado.append(item)
            
    cards = [criar_card(i) for i in resultado]
    categorias = sorted(Counter(str(i["categoria"]) for i in resultado))
    
    # Escrita dos arquivos de saída
    Path(CFG.html).write_text(gerar_html(cards, categorias, len(resultado)), encoding="utf-8")
    Path(CFG.json_file).write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    
    # Geração do log/relatório txt
    Path(CFG.relatorio).write_text(
        f"PROJETO CONCLUÍDO\n"
        f"Itens processados: {len(resultado)}\n"
        f"Categorias mapeadas: {len(categorias)}\n"
        f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n", 
        encoding="utf-8"
    )
    print("\n[Sucesso] Execução finalizada. Artefatos gerados com sucesso!")

if __name__ == "__main__":
    executar()
