"""
    Trabalho de Comp 2
"""

# Etrutura de dados principal
db = []

def criar(item):
    "Cria um elemento em 'db' e retorna o que foi criado"
    index = len(db) -1
    db[index] = item
    return item

def buscar():
    "Busca e retorna todos elementos de 'db'"

    return db

def buscar_por_id(id):
    "Busca e retorna um elemento se o identificador existir em 'db', se não retorna None"

    for i in range(0, len(db), 1):
        item = db[i]
        if item["id"] == id:
            return item
    return None

def atualizar(id, novos_valores):
    "Busca, atualiza e retorna um elemento se o identificador existir em 'db', se não retorna None"

    index = None

    for i in range(0, len(db), 1):
        item = db[i]
        if item["id"] == id:
            index = i

    if index is None:
        return None
    
    item = db[index]

    item_atualizado = {**item, **novos_valores}

    db[index] = item_atualizado

    return item_atualizado

def remover(id):
    "Busca e remove um elemento se o identificador existir em 'db', se não retorna None"

    index = None


    for i in range(0, len(db), 1):
        item = db[i]
        if item["id"] == id:
            index = i

    if index is None:
        return None

    db[index] = None

    return "item removido com sucesso"