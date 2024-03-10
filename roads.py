import os
import osmnx as ox
from datetime import datetime

# AQUI VOCÊ ESCOLHE A QUALIDADE/RESOLUÇÃO DO MAPA
dpi_out = 1200

# AQUI VOCÊ PODE MUDAR A COR DA VIA DE ACORDO COM SEU COMPRIMENTO (em metros)(ver função get_road_color)
road_colors = {
    'short': '#000000',
    'medium': '#000000',
    'long': '#000000',
    'very_long': '#000000',
    'default': '#000000'
}

bgcolor = "#ffffff"

# AQUI VOCÊ PODE MODIFICAR A LARGURA DA VIA DE ACORDO COM SEU COMPRIMENTO (em metros)
def get_linewidth(length):
    if length <= 100:
        return 0.25
    elif 100 < length <= 200:
        return 0.35
    elif 200 < length <= 400:
        return 0.35
    elif 400 < length <= 800:
        return 0.35
    else:
        return 0.45

# DEFINIÇÕES DE COMPRIMENTO DAS VIAS DE ACORDO COM SUAS METRAGENS
def get_road_color(length):
    if length <= 100:
        return road_colors['short']
    elif 100 < length <= 200:
        return road_colors['medium']
    elif 200 < length <= 400:
        return road_colors['long']
    elif 400 < length <= 800:
        return road_colors['very_long']
    else:
        return road_colors['default']


point = (-23.268706, -47.297528)
# G = ox.graph_from_point(point, dist=5000, retain_all=True, simplify=True, network_type='all')
G = ox.graph_from_place('Itu, Brazil')


roadColors = []
roadWidths = []

# APLICA AS MODIFICAÇÕES
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    # Calcula a largura da linha
    linewidth = get_linewidth(ddata.get("length", 0))
    # Obtém a cor da estrada
    color = get_road_color(ddata.get("length", 0))
    
    roadColors.append(color)
    roadWidths.append(linewidth)

# PLOTA O MAPA
fig, ax = ox.plot_graph(G, node_size=0, figsize=(27, 40), dpi=300,
                        bgcolor=bgcolor, save=False,
                        edge_color=roadColors, edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)

# Obtém a data e hora atual
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# SALVA O ARQUIVO NA PASTA IMGS (se a pasta não existir, cria - importante dizer que a pasta está no gitignore,)
# portanto as imagens não estão sendo salvas no Git. Se quiser que sejam, tire-as do gitignore.
folder_name = "imgs"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
file_path = os.path.join(folder_name, f"roadMap_{current_time}.pdf")
fig.savefig(file_path, dpi=dpi_out, bbox_inches='tight', format="pdf", facecolor=fig.get_facecolor(), transparent=False)
