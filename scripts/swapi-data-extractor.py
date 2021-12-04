import requests
import json
import logging
import config
import mysql.connector
from mysql.connector import Error
import re

REQUESTS_LIMIT = 2
connection = None

def create_connection(host_name, user_name, user_password, db_name):
  connection = None
  try:
    connection = mysql.connector.connect(
      host = host_name,
      user = user_name,
      passwd = user_password,
      database = db_name
    )
    logging.info("Connection to MySQL DB successful")
  except Error as e:
    logging.error(e)
  return connection

def get_json(url):
  return requests.get(url, verify=False).json()
  
def insert_planet(planet):
  id = re.search(r'/planets/(\d+)/', planet['url']).group(1)
  
  sql = "INSERT INTO test_planet ( id, name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population, created_date, updated_date, url ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
  val = ( id, planet['name'], planet['rotation_period'], planet['orbital_period'], planet['diameter'], planet['climate'], planet['gravity'], planet['terrain'], planet['surface_water'], planet['population'], planet['created'], planet['edited'], planet['url'] )

  cursor = connection.cursor()
  cursor.execute(sql, val)
  connection.commit()
  
def insert_person(person):
  id = re.search(r'/people/(\d+)/', person['url']).group(1)
  planet_id = re.search(r'/planets/(\d+)/', person['homeworld']).group(1)
  mass = person['mass'].replace(',', '')
  
  sql = "INSERT INTO test_people ( id, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, planet_id, created_date, updated_date, url ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
  val = ( id, person['name'], person['height'], mass, person['hair_color'], person['skin_color'], person['eye_color'], person['birth_year'], person['gender'], planet_id, person['created'], person['edited'], person['url'] ) 
  
  cursor = connection.cursor()
  cursor.execute(sql, val)
  connection.commit()

def parse_planets():  
  requests_counter = 0
  next_url = "https://swapi.dev/api/planets/"
  while next_url and requests_counter < REQUESTS_LIMIT:
    planets_json = get_json(next_url)
    requests_counter += 1
    for planet in planets_json['results']:
      insert_planet(planet)
    next_url = planets_json['next']

def parse_people():
  requests_counter = 0
  next_url = "https://swapi.dev/api/people/"
  while next_url and requests_counter < REQUESTS_LIMIT:
    people_json = get_json(next_url)
    requests_counter += 1
    for person in people_json['results']:
      insert_person(person)
    next_url = people_json['next']
    
def main():
  global connection
  connection = create_connection(config.DB_HOSTNAME, config.DB_LOGIN, config.DB_PASSWORD, config.DB_NAME)
  #parse_planets()
  parse_people()

if __name__ == "__main__":
  main()
