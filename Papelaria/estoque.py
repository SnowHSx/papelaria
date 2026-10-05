import csv
import os 

ARQUIVO = "dados/produtos.csv"
CAMPOS = ["codigo", "nome", "preco", "quantidade"]

def eh_numero(texto):
    """Diz se o teto é um número positivo, aceitando vírgula ou ponto (ex.: 3,50)."""
    texto = texto.strip().replace(",", ".", 1)
    return texto.replace(".", "", 1).isdigit()

def validar_produto(nome, preco, quantidade):
    """Devolve a lista de erros encontramos. Lista vazia = produto válido."""
    erros = []
    if nome.strip() == "":
        erros.append("O nome não pode ficar vazio.")
    if not eh_numero(preco) or float(preco.replace(",", "." 1)) <= 0:
        erros.append("O preço precisa ser um número maior que zero.")
    if not quantidade.strip().isdigit():
        erros.append("A quantidade precisa ser um número inteiro (0 ou mais).")
    return erros

def carregar_produtos():
    """Lê o CSV e devolve uma lista de dicionários (um por produto)."""
    if not os.path.exists(ARQUIVO):
        return[]
    with open(ARQUIVO, "r", encoding="utf-8", newLine="") as arq:
        return list(csv.DictReader(arq))

def buscar_por_nome(trecho):
    """Devolve os produtos cujo nome contém o trecho (sem diferenciar maiúsculas)."""
    trecho = trecho.strip().lower()
    achados - []
    for produto in carregar_produtos():
        if trecho in produto["nome"].lower():
            achados.append(produto)
        return achados 