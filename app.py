
# tutaj dodaj import metody request
from flask import Flask, request

# utwórz obiekt app 
app = Flask(__name__)

# skopiuj poprzednie podstrony aplikacji 

@app.route('/')
def say_hello():
    return "Hello World"

@app.route('/julia')
def julia():
    return "To jest moja strona"
        
if __name__ == '__main__':
    app.run() # domyślnie ustawia localhost i port 5000
    # app.run(host='0.0.0.0', port=8000)

# tutaj dodaj kod nowej podstrony /hello

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get("name", "")
    if(name):
        return "Hello {}".format(name)
    else:
        return "Hello"

# Create an API end point
@app.route('/api/v1.0/predict')
def predict():
    dictionary = {
        'prediction': 0
    }
    a = request.args.get("a", "", float)
    b = request.args.get("b", "", float)
    dictionary['features'] = f'a={a}, b={b}'
    if(a+b > 5.8):
        dictionary['prediction'] = 1
    return dictionary

if __name__ == '__main__':
    app.run() # domyślnie ustawia localhost i port 5000
    # app.run(host='0.0.0.0', port=8000)