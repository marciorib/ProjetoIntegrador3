#from flask import Flask, request, jsonify, render_template
from transformers import BertTokenizer, BertForQuestionAnswering
import torch
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template, redirect, url_for


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/manual.db'
db = SQLAlchemy(app)

# Modelo do banco
class Manual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

# Página principal
@app.route("/")
def home():
    return render_template("manu.html")

@app.route('/manafi')
def manafi():
    return render_template('manafi.html')

@app.route("/sobre")
def pagina_sobre():
    return """
        <b>Programador Python</b>: assista os vídeos no
        <a href="https://youtube.com/programadorpython">Canal no YouTube</a>
    """

@app.route("/man")
def ola_mundo():
    return render_template("index.html")

@app.route("/em_manutencao")
def em_manutencao():
    return render_template("em_manutencao.html")

# Manuais ainda não implementados
manuals = [
    'mancan', 'mancom', 'mandoc', 'maneng', 'manate', 'mancate', 'mancot', 'manedu',
    'manexp', 'manaud', 'mancod', 'mandis', 'manenc', 'manfac', 'manfil', 'manjur',
    'manlog', 'manorg', 'manpes', 'mangov', 'manlic', 'manneg', 'manpar', 'manpla',
    'manint', 'manlig', 'manorc', 'manpat', 'manpoc', 'manpin', 'mansup', 'manseg',
    'mantic', 'manser', 'mantra'
]

@app.route('/cadastrar_manual', methods=['GET', 'POST'])
def cadastrar_manual():
    if request.method == 'POST':
        nome = request.form['nome']
        conteudo = request.form['conteudo']

        # Verificar se já existe
        if Manual.query.filter_by(nome=nome).first():
            return f"<h3>Manual '{nome}' já cadastrado.</h3>"

        novo_manual = Manual(nome=nome, conteudo=conteudo)
        db.session.add(novo_manual)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('cadastrar_manual.html')

@app.route("/manual/<nome>")
def exibir_manual(nome):
    manual = Manual.query.filter_by(nome=nome).first()
    if not manual:
        return f"<h2>Manual '{nome}' não encontrado.</h2>", 404
    return render_template("exibir_manual.html", manual=manual)


# Criação dinâmica das rotas
for manual in manuals:
    def gerar_rota(nome):
        def rota():
            return f"<h1>{nome.upper()} em desenvolvimento</h1>"
        rota.__name__ = nome
        app.add_url_rule(f"/{nome}", endpoint=nome, view_func=rota)
    gerar_rota(manual)

# Carregar modelo BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

@app.route("/pergunta")
def pagina_pergunta():
    manuais = Manual.query.all()
    return render_template("perguntar.html", manuais=manuais)

# API para perguntas
@app.route('/perguntar', methods=['POST'])
def perguntar():
    dados = request.get_json()
    pergunta = dados['pergunta']
    id_manual = dados['id_manual']
    manual = recuperar_manual(id_manual)
    contexto = manual['conteudo']
    resposta = buscar_resposta(pergunta, contexto)
    return jsonify({'resposta': resposta})

# Busca resposta com BERT
def buscar_resposta(pergunta, contexto):
    inputs = tokenizer.encode_plus(pergunta, contexto, add_special_tokens=True, return_tensors='pt')
    outputs = model(**inputs)
    start_scores, end_scores = outputs.start_logits, outputs.end_logits
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)
    resposta_ids = inputs['input_ids'][0][start_index:end_index+1]
    resposta = tokenizer.decode(resposta_ids)
    return resposta

# Simulação temporária do conteúdo
def recuperar_manual(id_manual):
    manual = Manual.query.filter_by(nome=id_manual).first()
    if manual:
        return {"conteudo": manual.conteudo}
    return {"conteudo": "Manual não encontrado."}


# Execução
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
