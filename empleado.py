
from flask import Flask,request
from flask import render_template
app = Flask(__name__)
@app.route('/')
def template():
 return render_template("empleado.html")
@app.route('/empleado',methods=['POST'])
def empleadon():
   emple=(request.form['emple']) 
   sue=int(request.form['sue']) 
   por=int(request.form['por']) 
   bono= sue*(por/100)
   tot=sue+por
   return render_template('mostrarempleado.html',emple=emple,sue=sue,bono=bono,tot=tot)
if __name__ == '__main__':
  app.run(debug=True,port=8000)