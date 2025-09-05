import win32com.client as win32
import os

outlook = win32.Dispatch("outlook.application")

email = outlook.CreateItem(0)

conta = outlook.Session.Accounts["seu_segundo_email_outlook@gmail.com"]

email._oleobj_.Invoke(*(64209, 0, 8, 0, conta))

email.To = "seuemaildestino@hotmail.com"
email.Cc = "seuemailcopia@gmail.com;outroemailcopia@hotmail.com"
email.Bcc = "outroemailcopiaoculta@gmail.com"
email.Subject = "Email enviado pelo Outlook"
# email.Body = "Texto do email"
email.HTMLBody = """<p>Meu primeiro paragrafo</p>
<p>Outro paragrafo no email</p>
<img src='seu_link_imagem'
width=200>"""

caminho_codigo = os.getcwd()
arquivo_anexar = "anexos/kivy.png"
lista_arquivos = os.listdir("anexos")

for nome_arquivo in lista_arquivos:
    caminho_anexo = os.path.join(caminho_codigo, "anexos", nome_arquivo)
    email.Attachments.Add(caminho_anexo)

email.Send()