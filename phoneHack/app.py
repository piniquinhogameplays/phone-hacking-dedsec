from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_action():
    action = request.form.get('action')  # Recebe o valor 'action' do POST
    if not action:
        return "Nenhuma ação recebida!", 400

    if action == "abrir_arquivo":
        os.system('notepad')  # Abre o Bloco de Notas
        return "Bloco de Notas aberto com sucesso!"
    elif action == "rodar_bat":
        os.system(r'C:\caminho\do\arquivo.bat')  # Certifique-se de ajustar o caminho correto
        return "Arquivo BAT executado com sucesso!"
    else:
        return f"Ação inválida: {action}", 400  # Exibe qual foi a ação recebida

if __name__ == '__main__':
    app.run(debug=True)
