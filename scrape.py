#!/home/ttosto_estag/Thiago/Projetos/Globosat/Scrapy/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess
from intercambio_spider import *
from scrapy.utils.project import get_project_settings
import json
from send_email import *
from template_parser import *
from parse_cadastros import *
from log_generator import *
#import boto3



def load_json(file):
	with open(file) as json_file:
		return json.load(json_file)

#recebe duas listas e retorna o elemento diferente
def diff(lista1, lista2):
	for lo in lista1:
		teste = False
		for li in lista2:
			if lo['text'] == li['text']:
				teste = True
		if not teste:
			return lo['text'].encode('utf-8')

	return False

#carregando json com ultima atualização
try:
	last = load_json('result.json')
except:
	raise

with open('result.json', 'w') as result:
	result.write('')

settings = get_project_settings()
settings.overrides['FEED_FORMAT'] = 'json'
settings.overrides['FEED_URI'] = 'result.json'

process = CrawlerProcess(settings)


process.crawl(IntercambioSpider)
process.start() # the script will block here until the crawling is finished

try:
	current = load_json('result.json')


	if current == last:
		log_generator('miss')


	new = diff(current, last)

	if new:
		cadastrados = parse_cadastros('cadastros/cadastrados.txt')

		for cadastro in cadastrados:
			send_email(cadastro['email'] ,{'subject':'alerta nova publicação', 'body': template_parser({'nome': cadastro['nome'], 'msg': new}, 'templates/alerta.txt')})

		log_generator('hit', "%s" % new)

except:
	raise

#def lambda_handler(event, context):
#    return 'Hello from Lambda'
