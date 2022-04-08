 
from matplotlib.colors import cnames
import mysql.connector

class Query:
  def __init__(self):
    self.cnx = mysql.connector.connect(user='root', password='root', database='musclepedia')
    self.cursor = self.cnx.cursor()

# Queries to Exercise tables
  def selectEx(self):
    result = ''
    query = ("SELECT ex_Name FROM exercises")
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    return result



# App run to disconnect from DB
  def kill(self):
    self.cursor.close()
    self.cnx.close()
