import numpy as np


def aplica_sticker(fundo, sobreposicao, pos_x, pos_y):
    largura = fundo.shape[1]
    altura = fundo.shape[0]

    if pos_x >= largura or pos_y >= altura:
        return fundo

    alt, lar = sobreposicao.shape[0], sobreposicao.shape[1]

    if pos_x + lar > largura:
        lar = largura - pos_x
        sobreposicao = sobreposicao[:, :lar]

    if pos_y + alt > altura:
        alt = altura - pos_y
        sobreposicao = sobreposicao[:alt]

    if sobreposicao.shape[2] < 4:
        sobreposicao = np.concatenate([sobreposicao, np.ones((sobreposicao.shape[0], sobreposicao.shape[1], 1), dtype=sobreposicao.dtype) * 255],
                                      axis=2, )

    imagem_sobreposta = sobreposicao[..., :3]
    mascara = sobreposicao[..., 3:] / 255.0

    fundo[pos_y:pos_y + alt, pos_x:pos_x + lar] = (1.0 - mascara) * fundo[pos_y:pos_y + alt, pos_x:pos_x + lar] + mascara * imagem_sobreposta

    return fundo
