# -*- coding: utf-8 -*-

#função recebe um arquivo de cadastro e devolve uma lista de dicionarios com cada cadastro
def parse_cadastros(cadastros_file):
    cadastros_list = []

    with open(cadastros_file, 'r') as arquivo:
        cadastros_raw = arquivo.readlines()

        for cadastro in cadastros_raw:
            cadastros_list.append({'nome': cadastro.split(': ')[0], 'email': cadastro.split(': ')[1]})

    return cadastros_list
