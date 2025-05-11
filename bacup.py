from flask import Flask, url_for, render_template

app = Flask(__name__)
@app.route("/")
def home():      
    return render_template("manu.html")  

@app.route('/manafi')  
def manafi():
    return render_template('manafi.html') 

@app.route("/sobre")
def pagina_sobre():
    return """
           #<b>Programador Python</b>: assita os videos no
         #  <a href="https://youtube.com/programadorpython">Canal no youtube</a>
"""

@app.route("/man")
def ola_mundo():
    return render_template("index.html")

# Lista e criação de rotas para manuais em desenvolvimento
def criar_rota_manual(nome):
    @app.route(f'/{nome}')
    def manual_em_desenvolvimento(nome=nome):
        return f"<h1>{nome.upper()} em desenvolvimento</h1>"

# Manuais ainda não implementados
manuals = [
    'mancan', 'mancom', 'mandoc', 'maneng', 'manate', 'mancate', 'mancot', 'manedu',
    'manexp', 'manaud', 'mancod', 'mandis', 'manenc', 'manfac', 'manfil', 'manjur',
    'manlog', 'manorg', 'manpes', 'mangov', 'manlic', 'manneg', 'manpar', 'manpla',
    'manint', 'manlig', 'manorc', 'manpat', 'manpoc', 'manpin', 'mansup', 'manseg',
    'mantic', 'manser', 'mantra'
]

for manual in manuals:
    criar_rota_manual(manual)


if __name__ == '__main__':
    app.run(debug=True)
