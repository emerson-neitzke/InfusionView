# -*- iso-8859-1 -*-

"""Modulo Dbase
"""

from tinydb import TinyDB, Query

"""Classe Dbase
"""

db = TinyDB('db.json')

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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})   
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})                   
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})
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
               'medico':'-1'})                
else:
    print db.all()


# Codigo de inicializacao
print "Inicializando modulo dbase..."
