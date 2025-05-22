from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modules')
def modules():
    course_modules = [
        "Introdução ao pão caseiro",
        "Tipos de farinha e ingredientes",
        "Fermentação e leveduras",
        "Técnicas de amassar",
        "Modelagem e fermentação final",
        "Assando o pão perfeito",
        "Receitas especiais: pão integral, ciabatta e mais"
    ]
    return render_template('modules.html', modules=course_modules)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
