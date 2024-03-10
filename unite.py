from PIL import Image
## CRIADO PELO CHATGPT

# Abre as duas imagens
imagem1 = Image.open("road.png")
imagem2 = Image.open("water.png")

# Cria uma nova imagem do mesmo tamanho que as duas imagens
imagem_completa = Image.new("RGBA", imagem1.size)

# Coloca a imagem 1 na nova imagem
imagem_completa.paste(imagem1, (0, 0), imagem1)

# Define as coordenadas onde a imagem 2 será colada (movida para cima)
posicao_x = -17  # Posição x da imagem 2 (sem movimento horizontal)
posicao_y = -38  # Mova a imagem 2 para cima em 50 pixels (ajuste conforme necessário)

# Coloca a imagem 2 na nova imagem (movida para cima)
imagem_completa.paste(imagem2, (posicao_x, posicao_y), imagem2)

# Salva a imagem resultante
imagem_completa.save("imagem_unida.png")
