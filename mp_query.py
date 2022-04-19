 
from matplotlib.colors import cnames
import mysql.connector

class Query:
  def __init__(self):
    self.cnx = mysql.connector.connect(user='root', password='root', database='musclepedia')
    self.cursor = self.cnx.cursor()

# Queries to Exercise tables
  def selectAllEx(self):
    result = ''
    query = ("SELECT ex_Name FROM exercises")
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    return result

  def selectMusclesFromGroup(self, group):
    result = ''
    query = ("SELECT m_Name FROM muscles WHERE g_Name = '"+group+"'")
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    return result

  def selectExercise(self, exercise):
    result = ''
    query = ("SELECT ex_Name, eq_Name, ex_Description FROM exercises WHERE ex_Name = '"+exercise+"'")
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    return result

  def muscleTargetsOfExercise(self, exercise):
    result = ''
    query = ("SELECT m_Name FROM exercisetargets WHERE ex_Name = '"+exercise+"'")
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    return result

# App run to disconnect from DB
  def kill(self):
    self.cursor.close()
    self.cnx.close()

