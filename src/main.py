from flask import Flask, render_template, request, jsonify
from flasgger import Swagger
import random

import animals

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/api-docs.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api-docs/"
}


swagger = Swagger(app, config=swagger_config)

@app.route('/')
def home():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'url': rule.rule
        })
    return render_template('index.html', routes=routes)


@app.route('/get_animal', methods=['POST'])
def get_animal():
    """
    Get an animal by type and name
    ---
    parameters:
      - name: type
        in: body
        type: string
        required: true
        description: The type of the animal
      - name: name
        in: body
        type: string
        required: true
        description: The name of the animal
    responses:
      200:
        description: A successful response
        schema:
          id: Animal
          properties:
            name:
              type: string
              description: The name of the animal
            speak:
              type: string
              description: The sound the animal makes
      400:
        description: Invalid input
    """
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

# Existing imports and app setup...

@app.route('/get_random_animal', methods=['GET'])
def get_random_animal():
    """
    Get a random animal
    ---
    responses:
      200:
        description: A successful response
        schema:
          id: RandomAnimal
          properties:
            type:
              type: string
              description: The type of the animal
            name:
              type: string
              description: The name of the animal
            speak:
              type: string
              description: The sound the animal makes
    """
    animal_list = [animals.Dog('Rex'), animals.Cat('Whiskers'), animals.Gerbil('Gerry'), animals.Cow('Cody'), animals.Pig('Porky')]
    animal = random.choice(animal_list)
    
    return jsonify({
        'type': animal.__class__.__name__.lower(),
        'name': animal.name,
        'speak': animal.speak()
    })

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint
    ---
    responses:
      200:
        description: A successful response
        schema:
          id: Health
          properties:
            status:
              type: string
              description: The health status
    """
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)