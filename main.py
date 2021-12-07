from funcoes import *

def main():
    vUsuario=os.getlogin() #Descobrir o nome do usuárop
    path = r'C:\\Users\\'+vUsuario+'\\Downloads'

    # 1º - Criação dos diretórios
    for vKey, vValue in vExtensoes.items():
        if vValue != '':
            criaDiretorio(path, vValue) #Criação dos diretórios com base no arquivo Json contido no arquivo extensoes.py

    # 2° - Leitura dos arquivos do diretório
    vFiles = retornaArquivosDiretorio(path) #Chamada da função para retonar uma lista com todos os arquivos do dirório

    # 3º - Mover os arquivos da raiz para o diretório correspondente
    for vArquivo in vFiles:
        vExtensao = retornaExtensaoArquivo(vArquivo) #Descobre a extensão do arquivo
        vDiretorioNew = retornaDiretorioExtensao(vExtensao) #Descobre o diretório da Extensão
        moveArquivo(path, vArquivo, vDiretorioNew) #Mover o arquivo para o diretório da Extensão

main()
