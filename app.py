import os
import mimetypes
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request

# CORREÇÃO DO BUG DO WINDOWS
mimetypes.add_type('text/css', '.css')

pasta_projeto = os.path.dirname(os.path.abspath(__file__))
pasta_static = os.path.join(pasta_projeto, 'static')
pasta_templates = os.path.join(pasta_projeto, 'templates')

app = Flask(__name__, static_folder=pasta_static, template_folder=pasta_templates)

@app.route('/')
def home():
    meus_projetos = [
        {
            "nome": "Seven Developers", 
            "tecnologia": "Desenvolvimento Web / Agência",
            "descricao": "Plataforma oficial da minha agência de desenvolvimento e soluções digitais.",
            "link": "https://seven-developers-site.netlify.app/"
        },
        {
            "nome": "Sistemas para Academias", 
            "tecnologia": "Sistema de Gestão",
            "descricao": "Aplicação completa voltada para a gestão e acompanhamento de academias.",
            "link": "https://exemplo-academia.netlify.app/"
        },
        {
            "nome": "Automação de Notificações", 
            "tecnologia": "Python / SMTP & Back-end",
            "descricao": "Script inteligente integrado ao Back-end para capturar leads do formulário e disparar alertas por e-mail em tempo real.",
            "link": "#contato"
        }
    ]
    return render_template('index.html', projetos=meus_projetos)

@app.route('/enviar-mensagem', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    email_cliente = request.form.get('email')
    mensagem_cliente = request.form.get('mensagem')
    
    # ==========================================
    # LÓGICA DE BACK-END: ENVIO DE E-MAIL
    # ==========================================
    
    MEU_EMAIL = "7sevendevelopers@gmail.com"
    SENHA_APP = "thyz cvsj blum ygnm" # Cole a senha de 16 letras gerada no Google aqui!
    
    try:
        # Criando a estrutura do e-mail
        msg = MIMEMultipart()
        msg['From'] = MEU_EMAIL
        msg['To'] = MEU_EMAIL
        msg['Subject'] = f"🚀 Novo Lead no Portfólio: {nome}"
        
        corpo_email = f"""
        Parabéns, Daniel! Você recebeu um novo contato pelo seu portfólio.
        
        DADOS DO CLIENTE:
        Nome: {nome}
        E-mail: {email_cliente}
        
        MENSAGEM:
        {mensagem_cliente}
        """
        
        msg.attach(MIMEText(corpo_email, 'plain'))
        
        # Conectando ao servidor do Google e enviando
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(MEU_EMAIL, SENHA_APP)
        servidor.send_message(msg)
        servidor.quit()

        # TELA DE SUCESSO ESTILO "TERMINAL" PARA O CLIENTE
        return f"""
        <div style="background: #0f172a; color: #f8fafc; font-family: monospace; padding: 40px; min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="border: 1px solid #10b981; padding: 20px; border-radius: 10px; max-width: 600px; width: 100%;">
                <h2 style="color: #10b981; margin-bottom: 20px;">> Automação Executada com Sucesso!</h2>
                <p style="color: #94a3b8;">[DEBUG] Iniciando processo de captura de lead...</p>
                <p>> Extraindo nome: <span style="color: #fbbf24;">{nome}</span></p>
                <p>> Validando canal de contato: <span style="color: #fbbf24;">{email_cliente}</span></p>
                <p>> Conectando ao Servidor SMTP Gmail...</p>
                <p style="color: #10b981;">> Notificação enviada para Daniel Barros em tempo real.</p>
                <hr style="border: 0; border-top: 1px solid #334155; margin: 20px 0;">
                <p style="color: #f8fafc;">Daniel recebeu seu contato e te responderá em breve!</p>
                <br>
                <a href="/" style="color: #3b82f6; text-decoration: none; font-weight: bold;">[ Voltar ao Portfólio ]</a>
            </div>
        </div>
        """
        
    except Exception as e:
        print(f"Erro no Back-end ao enviar e-mail: {e}")
        return f"<h3>Erro no servidor ao processar a automação. Por favor, me chame no WhatsApp: (61) 99616-6201</h3> <a href='/'>Voltar ao site</a>"

if __name__ == '__main__':
    app.run(debug=True)