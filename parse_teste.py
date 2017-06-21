from send_email import *
from template_parser import *
from parse_cadastros import *


cadastrados = parse_cadastros('cadastros/cadastrados.txt')

'''
for cadastro in cadastrados:
    send_email(cadastro['email'] ,{'subject':'boas vindas', 'body': template_parser(cadastro['nome'], 'templates/boas_vindas.txt')})
'''

send_email('thiagotosto@gmail.com', {'subject':'boas vindas!', 'body': template_parser({'nome': cadastrados[2]['nome']},  'templates/boas_vindas.txt')})
