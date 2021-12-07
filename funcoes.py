import os
import shutil
from extensoes import vExtensoes


def retornaDiretorioExtensao(vExtensao):
    '''
    Função para retornar o diretório correspondente da Extensão 

    Args:
        vExtensao (str): Extensão do Arquivo

    Return:
        (str) Nome do diretório
    '''
    vRetorno = "Outros"
    for vKey, vValue in vExtensoes.items():
        if vKey == str(vExtensao):
            return vValue

    return vRetorno
    
def moveArquivo(vPath, vFile, vNewFolder):
    '''
    Função para Mover um arquivo para outro diretório

    Args:
        vPath (str): Nome do diretório Raiz
        vFile (str): Nome do arquivo que será movido
        vNewFolder (str): Nome do diretório para onde o arquivo será movido

    Return:
        None
    '''
    vArquivo = vFile
    vDest    = vNewFolder+'\\'+vArquivo
    vArquivoOrigem = os.path.join(vPath, vArquivo)
    vArquivoDestino = os.path.join(vPath, vDest)
    shutil.move(vArquivoOrigem, vArquivoDestino)

def retornaExtensaoArquivo(vFile):
    '''
    Função para retornar a Extensão de um arquivo

    Args:
        vFile (str): Nome do arquivo 

    Return:
        (str) Extensão do arquivo
    '''
    vListExtensoes = vFile.split(".") #Cria lista com todas as possiveis extensões
    vTamanhoLista = len(vListExtensoes) #Descobre o tamanho da lista
    vExtensao = vListExtensoes[vTamanhoLista-1] #Retorna o ultimo elementom da lista
    vExtensao = vExtensao.lower().strip()
    return vExtensao

def retornaArquivosDiretorio (vPath):
    '''
    Função para uma lista com todos os arquivos de um diretório

    Args:
        vPath (str): Caminho do diretório 

    Return:
        ([List]) Listagem com todos os arquivos de um diretório 
    '''
    files = []
    for (dirpath, dirnames, filenames) in os.walk(vPath):
        files.extend(filenames)
        break
    return files

def criaDiretorio(vDiretorioRaiz, vDirName):
    vParentDir = vDiretorioRaiz
    vNewDir   = os.path.join(vParentDir, vDirName)     
    
    #CRIAÇÃO DO DIRETÓRIO DO TIPO (EX: CHAMADO, RDM , TAREFAS)
    if os.path.isdir(vNewDir) == False:
        try: 
            os.mkdir(vNewDir) 
        except OSError as error: 
            print(error)
