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
    logging.warn("Connection to MySQL DB successful")
  except Error as e:
    logging.error(e)
  return connection

def insert_planet(connection, planet):
  id = re.search(r'/planets/(\d+)/', planet['url']).group(1)
  sql = "INSERT INTO test_planet ( id, name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population, created_date, updated_date, url ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
  val = ( id, planet['name'], planet['rotation_period'], planet['orbital_period'], planet['diameter'], planet['climate'], planet['gravity'], planet['terrain'], planet['surface_water'], planet['population'], planet['created'], planet['edited'], planet['url'] )

  cursor = connection.cursor()
  cursor.execute(sql, val)
  connection.commit()

def get_some_planets(url):
  return requests.get(url, verify=False).json()

def main():
  connection = create_connection(config.DB_HOSTNAME, config.DB_LOGIN, config.DB_PASSWORD, config.DB_NAME)

  requests_counter = 0
  next_url = "https://swapi.dev/api/planets/"
  while next_url and requests_counter < REQUESTS_LIMIT:
    planets_json = get_some_planets(next_url)
    requests_counter += 1
    for planet in planets_json['results']:
      insert_planet(connection, planet)
    next_url = planets_json['next']

if __name__ == "__main__":
  main()
    