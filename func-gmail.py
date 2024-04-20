import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
email = "seugmail@gmail.com"
senha = "sua-senha"
# é impotante obsevar que se tratando de google, voce necessita d configurar em sua conta uma senha de aplicativo, para poder autentificar o script
smtp = "smtp.gmail.com"
porta = 587

# Criar a mensagem
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = "gmail-destinario@gmail.com"
msg['Subject'] = "Assunto"
mensagem = "Texto"
msg.attach(MIMEText(mensagem, 'plain'))

# Conectar e enviar o email
try:
    server = smtplib.SMTP(smtp, porta)
    server.starttls()
    server.login(email, senha)
    texto = msg.as_string()
    server.sendmail(email, "gmail-destinario@gmail.com", texto)
    server.quit()
    print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o email: {e}")