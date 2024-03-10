import os
import networkx as nx
import osmnx as ox
from datetime import datetime

format = "png"
# Get data for places


location = ["Boituva, Brazil"]
G1 = ox.graph_from_place(location, retain_all=True, simplify = False, custom_filter='["natural"~"water"]')
G2 = ox.graph_from_place(location, retain_all=True, simplify = False,custom_filter='["waterway"~"river"]')
Gwater = nx.compose(G1, G2)

Gwater = nx.compose(G1, G2)


u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in Gwater.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)    


# List to store colors
roadColors = []
roadWidths = []

# #72b1b1
# #5dc1b9
for item in data:
    if "name" in item.keys():
        if item["length"] > 400: 
            color = "#72b1b1"
            linewidth = 2
        else:
            color = "#72b1b1"
            linewidth = 0.8
    else:
        color = "#72b1b1"
        linewidth = 0.5
    roadColors.append(color)    
    roadWidths.append(linewidth)



fig, ax = ox.plot_graph(Gwater, node_size=0,figsize=(27, 40), 
                        dpi = 400, save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

fig.tight_layout(pad=0)

# Obtém a data e hora atual
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# SALVA O ARQUIVO NA PASTA IMGS (se a pasta não existir, cria - importante dizer que a pasta está no gitignore,)
# portanto as imagens não estão sendo salvas no Git. Se quiser que sejam, tire-as do gitignore.
folder_name = "imgs_waters"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
file_path = os.path.join(folder_name, f"roadMap_{current_time}.{format}")

fig.savefig(file_path, dpi=400, bbox_inches='tight', format="png", 
            facecolor=fig.get_facecolor(), transparent=True)