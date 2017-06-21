import datetime

def log_generator(log_type, element=None):
    if log_type == 'hit':
        log_msg = "%s Novo elemento encontrado: %s" % (datetime.datetime.now(), element)

        with open('log/scrape.log', 'a') as log:
            log.write(log_msg + '\n')

    if log_type == 'teste':
        log_msg = "%s Teste realizado" % (datetime.datetime.now())

        with open('log/scrape.log', 'a') as log:
            log.write(log_msg + '\n')

    if log_type == 'miss':
        log_msg = "%s Nada Mudado" % (datetime.datetime.now())

        with open('log/scrape.log', 'a') as log:
            log.write(log_msg + '\n')
