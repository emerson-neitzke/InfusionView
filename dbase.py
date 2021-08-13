# -*- iso-8859-1 -*-

"""Modulo Dbase
"""

from tinydb import TinyDB, Query
from tinydb import where

"""Classe Dbase
"""

db = TinyDB('db.json')
dbLeitos = Query()

if len(db) == 0:
    """ Leito 1
    """
    db.insert({'leito':'1', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 2
    """               
    db.insert({'leito':'2', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 3
    """               
    db.insert({'leito':'3', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 4
    """
    db.insert({'leito':'4', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 5
    """               
    db.insert({'leito':'5', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 6
    """               
    db.insert({'leito':'6', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 7
    """
    db.insert({'leito':'7', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 8
    """               
    db.insert({'leito':'8', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 9
    """               
    db.insert({'leito':'9', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 10
    """
    db.insert({'leito':'10', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 11
    """               
    db.insert({'leito':'11', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 12
    """               
    db.insert({'leito':'12', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 13
    """               
    db.insert({'leito':'13', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 14
    """
    db.insert({'leito':'14', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 15
    """               
    db.insert({'leito':'15', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
    """ Leito 16
    """
    db.insert({'leito':'16', 
               'nome':'-1', 
               'prontuario':'-1', 
               'data_entrada':'-1', 
               'cpf':'-1',
               'telefone':'-1', 
               'genero':'-1', 
               'data_de_nascimento':'-1', 
               'dispositiv_1':'-1',
               'dispositiv_2':'-1',
               'dispositiv_3':'-1',
               'dispositiv_4':'-1',
               'tipo_sanguineo':'-1',
               'medico':'-1',
               'flag':'false'})
else:
    print db.all()

"""metodos
"""

def dbParse(results, field):
    result = [r[field] for r in results]
    for field in result:
        return field


# Codigo de inicializacao
print "Inicializando modulo dbase..."
