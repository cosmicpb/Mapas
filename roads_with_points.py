import os
import osmnx as ox
import matplotlib.pyplot as plt
from datetime import datetime

location = "Itu, Brazil"
dpi_out = 1200
format = "png"
road_colors = {
    'short': '#000000',
    'medium': '#000000',
    'long': '#000000',
    'very_long': '#000000',
    'default': '#000000'
}
bgcolor = "#ffffff"

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

G = ox.graph_from_place(location)

roadColors = []
roadWidths = []

for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    linewidth = get_linewidth(ddata.get("length", 0))
    color = get_road_color(ddata.get("length", 0))
    
    roadColors.append(color)
    roadWidths.append(linewidth)

fig, ax = ox.plot_graph(G, node_size=0, figsize=(16.53,11.69), dpi=300,
                        bgcolor=bgcolor, save=False,
                        edge_color=roadColors, edge_linewidth=roadWidths, edge_alpha=1, show=False)

# Pontos
hospitais = [(-23.2727503,-47.2920541), (-23.2703353,-47.2978269)]
upa = [(-23.2562686,-47.3152772)]
pam = [(-23.3894356,-47.3477858)]
ubs = [(-23.262809,-47.312068), (-23.38852,-47.347519), (23.285894,-47.274857), (-23.282073,-47.297964), (-23.284741,-47.290118), (-23.250922,-47.314804), (-23.277526,-47.305348), (-23.267523,-47.295222), (-23.268729,-47.281986), (-23.238547,-47.326053), (-23.386084,-47.338174), (-23.394705,-47.334307), (-23.406797,-47.35131), (-23.280912,-47.269687), (-23.257753,-47.351413), (-23.29017,-47.312452)]

# Adiciona os pontos ao mapa
for points, color in zip([hospitais, upa, pam, ubs], ['blue', 'green', 'yellow', 'red']):
    x, y = zip(*points)
    ax.scatter(y, x, c=color, s=5, zorder=5)

fig.tight_layout(pad=0)

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

folder_name = "imgs_roads"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
file_path = os.path.join(folder_name, f"roadMap_{current_time}.{format}")
fig.savefig(file_path, dpi=dpi_out, bbox_inches='tight', format=format, facecolor=fig.get_facecolor(), transparent=False)
print(f"roadMap_{current_time} was created.")
