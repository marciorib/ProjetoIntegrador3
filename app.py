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
    return #"""
           #<b>Programador Python</b>: assita os videos no
         #  <a href="https://youtube.com/programadorpython">Canal no youtube</a>
#"""

@app.route("/man")
def ola_mundo():
    return render_template("index.html")

 

if __name__ == '__main__':
    app.run(debug=True)
