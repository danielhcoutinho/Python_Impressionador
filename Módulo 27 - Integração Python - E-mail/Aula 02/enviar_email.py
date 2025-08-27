# SMTP

import smtplib
import email.message

def enviar_email():
    msg = email.message.Message() #parametro/instancia para criar uma mensagem de e-mail
    msg = ["Subject"] = "Email enviado com Python" #assunto
    msg = ['From'] = 'danihh1310@gmail.com' #email remetente
    msg = ['To'] = 'daniel.hcoutinho00@gmail.com' #email destinatario
    msg = ['Cc'] = 'danihh1310+copia@gmail.com' #Email copia 
    msg = ['Bcc'] = 'gaby.lopes314@gmail.com'

    #caso necessario mais de um email colocamos ; para separar os emails (isso dentro da aspas)

    corpo_email = """<p>Boa noite</p>
     <p> Esse é um email enviado com Python </p> """
    
    corpo_email = corpo_email.encode('utf-8') #transforma o corpo do email no padrão BR
    
    msg.add_header('Content-Type', 'text/html') #add esse cabeçalho padrão
    msg.set_payload(corpo_email) #add o corpo do e-mail

    servidor = smtplib.SMTP('smtp.gmail.com', 587) #passamos o endereço do servidor e a porta
    servidor.starttls() #cod que assegura o email (obrigatorio sempre)
    servidor.login(msg = ['From'], "zgpx gmrb uvzj xoyc" ) #passamos o usuario e senha (nao a pessoal e sim a senha de app nas config do google)
    servidor.send_message(msg) #envia a mensagem de email
    print('Email enviado')

enviar_email()
