import win32com.client as win32
import os

outlook = win32.Dispatch("outlook.application") #faz conexão com outlook

caixas_email = outlook.GetNamespace("MAPI") #recebe e busca emails na caixa de entrada, virando nossa caixa de email

# for pasta in caixas_email.Folders:
#     print(pasta)

pasta_python = caixas_email.Folders.Item(2) #nos da a segunda pasta da caixa de email

# for subpasta in pasta_python.Folders:
#     print(subpasta)

caixa_entrada = pasta_python.Folders.Item(1) #essa e nossa caixa de entrada da pasta de python

lista_emails = caixa_entrada.Items # lista todos os itens/emails que temos nessa caixa de entrada

print(len(lista_emails)) #printa a qtd de email

for email in lista_emails:
    anexos = email.Attachments
    if email.To == "seuemaildestino@hotmail.com" and len(anexos) > 0: #se email igual esse passado e se tem anexo no email
        print(email.Subject)
        print(email.Cc)
        print(email.Body)
        for anexo in anexos: #para cada anexo
            print(anexo.FileName) #printa o nome do anexo
            caminho_codigo = os.getcwd() #caminho ate o arquivo do nosso codigo
            caminho_anexo_salvar = os.path.join(caminho_codigo, anexo.filename) #salva o anexo no caminho passaod entre () que é a junção do caminho do codigo com o nome de cada arquivo
print("Fim do código")