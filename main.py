from flask import Flask, request, jsonify
import random

from animals.dog import Dog
from animals.cat import Cat
from animals.gerbil import Gerbil
from animals.cow import Cow
from animals.pig import Pig

app = Flask(__name__)

@app.route('/get_animal', methods=['POST'])
def get_animal():
    data = request.json
    animal_type = data.get('type')
    name = data.get('name')
    
    if animal_type.lower() == 'dog':
        animal = Dog(name)
    elif animal_type.lower() == 'cat':
        animal = Cat(name)
    else:
        return jsonify({'error': 'Animal type not supported'}), 400
    
    return jsonify({
        'name': animal.name,
        'speak': animal.speak()
    })

# Existing imports and app setup...

@app.route('/get_random_animal', methods=['GET'])
def get_random_animal():
    animals = [Dog('Rex'), Cat('Whiskers'), Gerbil('Gerry'), Cow('Cooh'), Pig('Porky')]
    animal = random.choice(animals)
    
    return jsonify({
        'type': animal.__class__.__name__.lower(),
        'name': animal.name,
        'speak': animal.speak()
    })

# The rest of your Flask app...

if __name__ == '__main__':
    app.run(debug=True)