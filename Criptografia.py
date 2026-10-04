import os
import random
import unicodedata

pasta_programa = os.path.dirname(os.path.abspath(__file__))

caminho_arquivo = os.path.join(pasta_programa, "mensagem_criptografada.txt")

def obter_caracteres_unicode():
    caracteres = []

    for codigo in range(0x110000):
        caractere = chr(codigo)

        if unicodedata.category(caractere)[0] != "C":
            caracteres.append(caractere)

    return caracteres


def gerar_codigo(caracteres, tamanho):
    return "".join(random.sample(caracteres, tamanho))


def criptografar(mensagem, tamanho, embaralhar, multiplas_codificacoes):
    caracteres_unicode = obter_caracteres_unicode()

    tabela = {}

    if embaralhar:
        lista = list(mensagem)
        random.shuffle(lista)
        mensagem = "".join(lista)

    resultado = ""

    for caractere in mensagem:
        if multiplas_codificacoes:
            codigos = gerar_codigo(caracteres_unicode, tamanho)

        else:
            if caractere in tabela:
                codigos = tabela[caractere]

            else: 
                codigos = gerar_codigo(caracteres_unicode, tamanho)
                tabela[caractere] = codigos


        resultado += codigos

    return resultado


mensagem = input("Digite a mensagem: ")

tamanho = int(input("Qual o tamanho de cada codificação? "))

embaralhar = input("Deseja embaralhar a mensagem? (s/n): ").lower() 

if embaralhar == "s":
    embaralhar = True

else:
    embaralhar = False

multiplas_codificacoes = input("Deseja ativar múltiplas codificações? (s/n): ").lower()

if multiplas_codificacoes == "s":
    multiplas_codificacoes = True

else:
    multiplas_codificacoes = False

resultado = criptografar(mensagem, tamanho, embaralhar, multiplas_codificacoes)

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(resultado)

print("\nMensagem criptografada!")
print(os.path.abspath("mensagem_criptografada.txt"))

