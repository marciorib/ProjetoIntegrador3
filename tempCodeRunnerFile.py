
@app.route("/sobre")
def pagina_sobre():
    return """
           <b>Programador Python</b>: assita os videos no
           <a href="https://youtube.com/programadorpython">Canal no youtube</a>
"""

@app.route("/man")
def ola_mundo():
    return render_template("index.html")