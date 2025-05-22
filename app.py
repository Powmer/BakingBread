import sqlite3
from flask import Flask, render_template_string, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'Senhanadagenerica123'

with open('index.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

DB_NAME = 'alunos.db'

def criar_tabela():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS inscricoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            mensagem TEXT
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

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

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO inscricoes (nome, email, mensagem) VALUES (?, ?, ?)', (nome, email, mensagem))
    conn.commit()
    conn.close()

    flash('Inscrição enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
