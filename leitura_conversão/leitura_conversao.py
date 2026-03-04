import cv2


def ajuste_brilho_contraste(imagem, alpha=1.0, beta=0):
    """
    alpha => controla o contraste da imagem.
    beta => controla o brilho da imagem.
    Equação aplicada: nova_imagem = alpha * imagem + beta
    """
    return cv2.convertScaleAbs(imagem, alpha=alpha, beta=beta)


def equalizar_imagem(imagem):
    """
    Melhora o contraste global redistribuindo a intensidade dos pixels.
    """
    return cv2.equalizeHist(imagem)


def calcular_metricas(imagem):
    """
    Retorna brilho médio e contraste (desvio padrão).
    """
    brilho = imagem.mean()
    contraste = imagem.std()
    return brilho, contraste
