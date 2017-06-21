from template_parser  import *
from send_email import *

send_email('thiagotosto@gmail.com', {'subject': 'boas vindas!', 'body': template_parser({'nome': 'Amanda Cortez'}, 'templates/boas_vindas.txt')})
