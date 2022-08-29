from flask import Flask
from flask import render_template
app = Flask(__name__) #decorador
@app.route('/') # ruta
def index():
   # return '<h1>Hola Chamo - pepe</h1>'
   return render_template('index.html')
if __name__ == '__main__':
  app.run(debug=True,port=5000)
    
    

