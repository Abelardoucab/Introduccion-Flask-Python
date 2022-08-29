
from flask import Flask,request
from flask import render_template
app = Flask(__name__)
@app.route('/')
def template():
    return render_template("form.html") 

@app.route('/saludo',methods=['POST'])  
def saludo():
    nombreUser=request.form['nombre']
    nac=request.form['nacido']
    return (f'Bienvenido {nombreUser} nacio en {nac}')
if __name__=='__main__':
    app.run(debug=True)