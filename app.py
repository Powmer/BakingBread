from flask import Flask, render_template_string, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_simples'

with open('index.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/inscricao', methods=['POST'])
def inscricao():
    nome = request.form.get('nome')
    email = request.form.get('email')
    mensagem = request.form.get('mensagem')

    if not nome or not email:
        flash('Por favor, preencha nome e e-mail.')
        return redirect('/')

    print(f'Inscrição recebida: {nome}, {email}, {mensagem}')
    flash('Inscrição enviada com sucesso!')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
