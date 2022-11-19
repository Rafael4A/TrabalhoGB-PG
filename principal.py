import cv2
import time

from aplica_sticker import aplica_sticker
from filtros import aplicar_filtros


def nothing(_):
    pass

def on_click(event, x, y, _flags, _param):
    global imagem
    if event == cv2.EVENT_LBUTTONDBLCLK:
        match posicaoSticker:
            case 1:
                imagem = aplica_sticker(imagem, sticker_amando, x, y)
            case 2:
                imagem = aplica_sticker(imagem, sticker_certo, x, y)
            case 3:
                imagem = aplica_sticker(imagem, sticker_observando, x, y)
            case 4:
                imagem = aplica_sticker(imagem, sticker_pensando, x, y)
            case 5:
                imagem = aplica_sticker(imagem, sticker_triste, x, y)

    elif event == cv2.EVENT_MBUTTONDBLCLK:
        cv2.imwrite("./imagens/"+ str(time.time()) + ".png", imagem)

sticker_amando = cv2.resize(cv2.imread("stickers/amando.png", cv2.IMREAD_UNCHANGED), (100, 100))
sticker_certo = cv2.resize(cv2.imread("stickers/certo.png", cv2.IMREAD_UNCHANGED), (125, 125))
sticker_observando = cv2.resize(cv2.imread("stickers/observando.png", cv2.IMREAD_UNCHANGED), (100, 100))
sticker_pensando = cv2.resize(cv2.imread("stickers/pensando.png", cv2.IMREAD_UNCHANGED), (100, 100))
sticker_triste = cv2.resize(cv2.imread("stickers/triste.png", cv2.IMREAD_UNCHANGED), (100, 100))


def camera():
    fonte = cv2.VideoCapture(0)
    if not fonte.isOpened():
        print("Não foi possível abrir a câmera")
        exit()
    trackbarMouseCb()
    global imagem
    while True:
        ret, frame = fonte.read()
        imagem = frame
        if not ret:
            print("Erro ao ler frame")
            break
        posicao = cv2.getTrackbarPos('Efeitos', 'Comandos')
        global posicaoSticker
        imagem = aplicar_filtros(imagem, posicao)
        posicaoSticker = cv2.getTrackbarPos('Stickers', 'Comandos')
        cv2.imshow('Imagem', imagem)
        if cv2.waitKey(10) == ord('q'):
            break
    cv2.destroyAllWindows()

def arquivo(caminho):
    fonte = cv2.imread(caminho, 1)
    fonte = cv2.resize(fonte, (1280, 720))
    global imagem
    imagem = fonte
    trackbarMouseCb()
    while True:
        posicaoEfeitos = cv2.getTrackbarPos('Efeitos', 'Comandos')
        global posicaoSticker
        posicaoSticker = cv2.getTrackbarPos('Stickers', 'Comandos')
        imagem = aplicar_filtros(fonte, posicaoEfeitos)
        cv2.imshow('Imagem', imagem)
        if cv2.waitKey(10) == ord('q'):
            break
    cv2.destroyAllWindows()


def trackbarMouseCb():
    cv2.namedWindow('Comandos', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Comandos', 600, 10)
    cv2.namedWindow("Imagem")
    cv2.createTrackbar('Stickers', 'Comandos', 1, 5, nothing)
    cv2.createTrackbar('Efeitos', 'Comandos', 0, 10, nothing)
    cv2.setMouseCallback('Imagem', on_click)