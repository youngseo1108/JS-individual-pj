# flask --app app run
from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href='/animals/dogs'>Dogs</a></li>
    <li><a href='/animals/cats'>Cats</a></li>
    <li><a href='/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'''
  <h1>List of {pet_type}</h1>
  <ul>
  '''  
  for pet_id, pet in enumerate(pets[pet_type]):
    html += '<li><a href="/animals/{0}/{1}">{2}</a></li>'.format(pet_type, pet_id, pet['name'])
  html += '</ul>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return '''
  <h1>{0}</h1>
  <img src="{1}" />
  <p>{2}</p>
  <ul>
    <li>{3}</li>
    <li>{4}</li>
  </ul>
  '''.format(pet['name'], pet['url'], pet['description'], pet['breed'], pet['age'])