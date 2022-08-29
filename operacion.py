
from flask import Flask,request
from flask import render_template
app = Flask(__name__)
@app.route('/')
def template():
 return render_template("operacion.html")
@app.route('/operan',methods=['POST'])
def operan():
    alt=int(request.form['ope']) 
    num1=int(request.form['num1']) 
    num2=int(request.form['num2']) 
    if alt ==1:
       ope="+"
       res=num1+num2
    if alt==2:
       ope="-"
       res=num1-num2 
    if alt==3:
       ope="x"
       res=num1*num2
    if alt==4:
       ope="/"
       if num2==0:
         res="No se puede dividir por cero"
       if num2!=0:
           res=float(num1/num2)
    if alt<1 or alt>4:
          res="Fuera de rango la operación"    
         
   #return (f'{num1} {ope} {num2} = {res}')    
    return render_template('oper.html',ope=ope,num1=num1,num2=num2,res=res)
if __name__ == '__main__':
  app.run(debug=True,port=8000)