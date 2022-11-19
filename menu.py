from tkinter import *
from tkinter import filedialog
from principal import camera, arquivo


def pesquisar_arquivos():
    nome_arquivo = filedialog.askopenfilename(initialdir="/", title="Escolha uma imagem",
                                          filetypes=(("Todos formatos", "*.*"), ("PNG", "*.png*"),("JPEG", "*.jpeg*"), ("JPG", "*.jpg*")))
    if(nome_arquivo):
        rotulo_arquivo.configure(text="Arquivo aberto: " + nome_arquivo)
        arquivo(nome_arquivo)

window = Tk()
window.title('Menu')
window.geometry("706x300")
window.config(background = "white")
rotulo_arquivo = Label(window, text ="Nenhum arquivo selecionado", width = 100, height = 4, fg ="blue")

botao_camera = Button(window, text="Webcam", command=camera)


botao_arquivo = Button(window, text="Selecionar Arquivo", command=pesquisar_arquivos)


botao_sair = Button(window, text="Sair", command=window.quit)


botao_camera.grid(column = 1, row = 1)
rotulo_arquivo.grid(column = 1, row = 2)
botao_arquivo.grid(column = 1, row = 4)
botao_sair.grid(column = 1,row = 6)

window.mainloop()
