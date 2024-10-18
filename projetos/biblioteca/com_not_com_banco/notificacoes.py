# notificacoes.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Notificador:
    def __init__(self, servidor_smtp, porta, email_remetente, senha):
        self.servidor_smtp = servidor_smtp
        self.porta = porta
        self.email_remetente = email_remetente
        self.senha = senha

    def enviar_email(self, email_destinatario, assunto, mensagem):
        try:
            # Configurando a mensagem
            msg = MIMEMultipart()
            msg['From'] = self.email_remetente
            msg['To'] = email_destinatario
            msg['Subject'] = assunto

            msg.attach(MIMEText(mensagem, 'plain'))

            # Conectando ao servidor SMTP
            servidor = smtplib.SMTP(self.servidor_smtp, self.porta)
            servidor.starttls()
            servidor.login(self.email_remetente, self.senha)

            # Enviando o email
            texto = msg.as_string()
            servidor.sendmail(self.email_remetente, email_destinatario, texto)
            servidor.quit()

            print(f"Email enviado para {email_destinatario} com sucesso.")
        except Exception as e:
            print(f"Falha ao enviar email para {email_destinatario}. Erro: {e}")
