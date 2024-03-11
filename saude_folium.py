import folium

# Criar um mapa centrado em Itu
mapa = folium.Map(location=[-23.2640, -47.2990], zoom_start=10)

# Adicionar marcadores para hospitais (azuis)
folium.Marker([-23.2727503, -47.2920541], popup='Hospital Municipal\nConvenção 550, Vila Nova, CEP - 13309-000', icon=folium.Icon(color='blue')).add_to(mapa)
folium.Marker([-23.2703353, -47.2978269], popup='Hospital da Criança\nRua Joaquim Bernardes Borges, 372, Centro', icon=folium.Icon(color='blue')).add_to(mapa)

# Adicionar marcadores para UPAs (verdes)
folium.Marker([-23.2562686, -47.3152772], popup='UPA\nAvenida Nove de Julho, 691, Nossa Senhora Aparecida', icon=folium.Icon(color='green')).add_to(mapa)

# Adicionar marcadores para PAMs (amarelos)
folium.Marker([-23.3894356, -47.3477858], popup='PAM “Mario Moraes Bourguignon”\nRua Itagiba Vilassa, s/nº, Vila Martins', icon=folium.Icon(color='purple')).add_to(mapa)

# Adicionar marcadores para UBSs (vermelhos)
ubss = [
    {"name": "UBS 01 - Dr Carlos Vasconcelos Prado", "location": [-23.262809, -47.312068], "address": "R. Nahor Leite Gomes, 300 - Jardim Convencao, Itu - SP, 13311-190"},
    {"name": "UBS 02 - José Maria Vicente", "location": [-23.38852, -47.347519], "address": "R. Fiovo de Bernandin, 35 - Conj. Hab. Uniao, Itu - SP, 13308-183"},
    {"name": "UBS 03 - Maria Cecília Meneghini", "location": [23.285894, -47.274857], "address": "Av. Dr. Ulisses de Moraes, 236 - Nucleo Hab. Sao Judas Tadeu, Itu - SP, 13304-770"},
    {"name": "UBS 04 - Dr. Alcides Rodrigues", "location": [-23.282073, -47.297964], "address": "R. Jasmim, 59 - Vila Roma, Itu - SP, 13310-481"},
    {"name": "UBS 05 - Tristão Bauer", "location": [-23.284741, -47.290118], "address": "Av. Francisco E. Favero, s/nº - Jardim do Estadio, Itu - SP, 13309-290"},
    {"name": "UBS 06 - Agostinho Neto", "location": [-23.250922, -47.314804], "address": "R. Monsenhor Ezequias Galvão, 485 - Vila Padre Bento, Itu - SP, 13313-113"},
    {"name": "UBS 07 - Dr. Sebastião de Moraes", "location": [-23.277526, -47.305348], "address": "R. e, 130 - Vila Sao Jose, Itu - SP, 13310-160"},
    {"name": "UBS 08 - Dr. Cid Ferraz do Amaral", "location": [-23.267523, -47.295222], "address": "Praça Conde de Parnaiba, 44 - Centro, Itu - SP, 13301-370"},
    {"name": "UBS 09 - Maria de Lourdes Pinheiro Passos", "location": [-23.268729, -47.281986], "address": "R. Juvenal Emanoelli, S/N - São Luiz, Itu - SP, 13304-260"},
    {"name": "UBS 10", "location": [-23.238547, -47.326053], "address": "R. Ilydia Dias Furtado, 158 - Cantagalo, Itu - SP, 13328-300"},
    {"name": "UBS 11 - Frei Pascasio Hettler", "location": [-23.386084, -47.338174], "address": "Rua Osasco, s/nº Bairro - Cidade Nova I, Itu - SP, 13308-093"},
    {"name": "UBS 12 - Dr. Emílio Chierighini", "location": [-23.394705, -47.334307], "address": "Av. Sol - Jardim Novo Mundo, Itu - SP, 13308-430"},
    {"name": "UBS 13", "location": [-23.406797, -47.35131], "address": "R. Geceney Cabreira, 198 - Portal do Éden, Itu - SP, 13308-531"},
    {"name": "UBS 14 - Santo Campos", "location": [-23.280912, -47.269687], "address": "R. Prof. Alfredo Gomes - Jardim Aeroporto, Itu - SP, 13304-730"},
    {"name": "UBS 15 - Dr. Hélio Chierighini", "location": [-23.257753, -47.351413], "address": "R. Armênia - Parque Res. Potiguara, Itu - SP, 13312-733"},
    {"name": "UBS 16 - José Roberto da Cruz", "location": [-23.29017, -47.312452], "address": "R. Benedito Ramos da Silva, Bairro - São Camilo, Itu - SP, 13309-815"}
]

for ubs in ubss:
    folium.Marker(location=ubs["location"], popup=f'{ubs["name"]}\n{ubs["address"]}', icon=folium.Icon(color='red')).add_to(mapa)

# Salvar o mapa como um arquivo HTML
mapa.save("mapa_de_saude.html")
