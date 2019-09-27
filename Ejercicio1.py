from flask import Flask
app=Flask(__name__)  #variable llamada "app" 
@app.route('/') #tiene que coincidir con el nombre que se le pone arriba. '/' define la ruta 
def hola():     
    return "Hola soy yo, la gueb"
if __name__=='__main__': 
    app.run(debug=True)