import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline


def aplicar_filtros(imagem, posicao):
    match posicao:
        case 0:
            return imagem
        case 1:
            return inverter(imagem)
        case 2:
            return preto_branco(imagem)
        case 3:
            return cores_frias(imagem)
        case 4:
            return cores_quentes(imagem)
        case 5:
            return clareamento(imagem, 60)
        case 6:
            return sepia(imagem)
        case 7:
            return saturacao(imagem)
        case 8:
            return nitidez(imagem)
        case 9:
            return lapis_cinza(imagem)
        case 10:
            return lapis_colorido(imagem)


def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))


def cores_frias(imagem):
    aumentar_LookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    diminuir_LookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    azul, verde, vermelho = cv2.split(imagem)
    vermelho = cv2.LUT(vermelho, diminuir_LookupTable).astype(np.uint8)
    azul = cv2.LUT(azul, aumentar_LookupTable).astype(np.uint8)
    win = cv2.merge((azul, verde, vermelho))

    return win


def cores_quentes(imagem):
    aumentar_LookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    diminuir_LookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    azul, verde, vermelho = cv2.split(imagem)
    vermelho = cv2.LUT(vermelho, aumentar_LookupTable).astype(np.uint8)
    azul = cv2.LUT(azul, diminuir_LookupTable).astype(np.uint8)
    sum = cv2.merge((azul, verde, vermelho))
    return sum


def inverter(imagem):
    inv = cv2.bitwise_not(imagem)
    return inv


def saturacao(imagem):
    hdr = cv2.detailEnhance(imagem, sigma_s=12, sigma_r=0.15)
    return hdr


def lapis_colorido(imagem):
    sk_gray, sk_color = cv2.pencilSketch(imagem, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_color


def lapis_cinza(imagem):
    sk_gray, sk_color = cv2.pencilSketch(imagem, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_gray


def sepia(imagem):
    imagem_sepia = np.array(imagem, dtype=np.float64)
    imagem_sepia = cv2.transform(imagem_sepia,
                              np.matrix([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]))
    imagem_sepia[np.where(imagem_sepia > 255)] = 255
    imagem_sepia = np.array(imagem_sepia, dtype=np.uint8)
    return imagem_sepia


def nitidez(imagem):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    imagem_nitida = cv2.filter2D(imagem, -1, kernel)
    return imagem_nitida


def clareamento(imagem, beta_value):
    imagem_clara = cv2.convertScaleAbs(imagem, beta=beta_value)
    return imagem_clara


def preto_branco(imagem):
    imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return imagem_pb
