from leitura_conversão.leitura_conversao import (
    ajuste_brilho_contraste,
    calcular_metricas,
    equalizar_imagem,
)
import cv2
import matplotlib.pyplot as plt


# ===============================
# CARREGANDO IMAGEM
# ===============================

imagem = cv2.imread(r"image\transferir.jpg", cv2.IMREAD_GRAYSCALE)

# ===============================
# AJUSTE DE BRILHO E CONTRASTE
# ===============================

ajuste = ajuste_brilho_contraste(imagem, alpha=1.3, beta=3.0)

brilho_ajuste, contraste_ajuste = calcular_metricas(ajuste)

print("Após ajuste:")
print("Brilho médio:", brilho_ajuste)
print("Contraste:", contraste_ajuste)

# ===============================
# EQUALIZAÇÃO
# ===============================

equalizada = equalizar_imagem(ajuste)

brilho_eq, contraste_eq = calcular_metricas(equalizada)

print("\nApós equalização:")
print("Brilho médio:", brilho_eq)
print("Contraste:", contraste_eq)

# Carrega imagem em escala de cinza
imagem = cv2.imread("image/transferir.jpg", cv2.IMREAD_GRAYSCALE)

# Calcula histograma
hist = cv2.calcHist([imagem], [0], None, [256], [0, 256])

# Plota
plt.plot(hist)
plt.title("Histograma da Imagem")
plt.xlabel("Intensidade de Pixel")
plt.ylabel("Quantidade de Pixels")
plt.xlim([0, 256])
plt.show()


# ===============================
# MOSTRAR IMAGENS
# ===============================

cv2.imshow("Original", imagem)
cv2.imshow("Ajuste Brilho/Contraste", ajuste)
cv2.imshow("Equalizada", equalizada)

cv2.waitKey(0)
cv2.destroyAllWindows()
