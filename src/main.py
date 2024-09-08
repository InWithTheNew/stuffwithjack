from flask import Flask, render_template, request, jsonify
from flasgger import Swagger
import random
import os

import animals

app = Flask(__name__)

@app.route('/')
def home():
    branch_name = '-' + os.getenv('BRANCH_NAME', '')
    domain_name = os.getenv('DOMAIN_NAME', '')
    return render_template('index.html')

@app.route('/get_animal', methods=['POST'])
def get_animal():
    data = request.json
    animal_type = data.get('type')
    name = data.get('name')
    
    if animal_type.lower() == 'dog':
        animal = animals.Dog(name)
    elif animal_type.lower() == 'cat':
        animal = animals.Cat(name)
    elif animal_type.lower() == 'cow':
        animal = animals.Cow(name)
    elif animal_type.lower() == 'gerbil':
        animal = animals.Gerbil(name)
    elif animal_type.lower() == 'pig':
        animal = animals.Pig(name)  
    else:
        return jsonify({'error': 'Animal type not supported'}), 400
    
    return jsonify({
        'name': animal.name,
        'speak': animal.speak()
    })

@app.route('/get_random_animal', methods=['GET'])
def get_random_animal():
    animal_list = [animals.Dog('Rex'), animals.Cat('Whiskers'), animals.Gerbil('Gerry'), animals.Cow('Cody'), animals.Pig('Porky')]
    animal = random.choice(animal_list)
    
    return jsonify({
        'type': animal.__class__.__name__.lower(),
        'name': animal.name,
        'speak': animal.speak()
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)