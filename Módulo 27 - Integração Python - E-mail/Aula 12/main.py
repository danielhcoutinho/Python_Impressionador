# API

# - Requisições (requests, get, post, patch, delete)

# - Biblioteca (sendgrid)

chave_api_sendgrid = "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"

from sendgrid import SendGridAPIClient #o que loga a nosa conta no twilio
from sendgrid.helpers.mail import Mail # o que cria nosso email

conta_sendgrid = SendGridAPIClient(chave_api_sendgrid) #faz conexão com nossa conta atarves da api

email = Mail(from_email="danihh1310@gmail.com", to_emails='daniel.hcoutinho00@gmail.com', 
             subject="Email enviado pelo Sendgrid no Python", 
             html_content="<p>Email enviado com sucesso, seja bem vindo</p><p>Abraços e até o próximo e-mail.</p>") #constroi nosos email, veja que os parametros ja constroi automaticamente nosso email

resposta = conta_sendgrid.send(email)
print(resposta.status_code)


