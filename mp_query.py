 
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

  def selectMuscle(self, muscle):
    result = ''
    query = "SELECT * FROM muscles WHERE m_Name = '"+muscle+"'"
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    return result

  def addExerciseWithEquip(self, equipList, muscList):
    result = ''
    query = "SELECT * FROM ( SELECT ex_Name FROM exercises WHERE "
    temp = ""
    for i, eq in enumerate(equipList):
      if i==0 and  eq == "Bodyweight":
        temp +=  ("eq_Name = null")
      elif i==0:
        temp += "eq_Name = '" + eq + "'"
      elif eq == "Bodyweight":
        temp += (" OR eq_Name = null")
      else:
        temp += (" OR eq_Name = '" + eq + "'")
    query += temp
    query += ") sub NATURAL JOIN ( SELECT DISTINCT ex_Name FROM exercisetargets t WHERE "

    temp = ""
    for j, musc in enumerate(muscList):
      if j == 0:
        temp += "t.ex_Name IN (SELECT ex_Name FROM exercisetargets WHERE m_Name = '"+musc+"')"
      else:
        temp += " OR t.ex_Name IN (SELECT ex_Name FROM exercisetargets WHERE m_Name = '"+musc+"')"

    query += temp
    query += " ) subTwo;"
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    return result

  def addExercise(self, name, equip, desc, muscles):
      result = ''
      query = "use Musclepedia; INSERT INTO exercises VALUES ('"
      if equip == 'Bodyweight':
        query += (name +"', null, '[Placholder Image]', '"+desc+"'); ")
      else:
        query += (name +"', '"+equip+"', '[Placholder Image]', '"+desc+"'); ")
      query += "INSERT INTO exercisetargets VALUES "
      for i, m in enumerate(muscles):
        if i == (len(muscles) - 1):
          query += ("('"+name+"', '"+m+"');")
        else:
          query += ("('"+name+"', '"+m+"'), ")
      print(query)
      self.cursor.execute(query)
      result = (self.cursor.fetchall())
      return result
  def deleteExercise(self, name):
    query = ("DELETE FROM exercises WHERE ex_Name = '"+name+"'; ")
    query += ("DELETE FROM exercisetargets WHERE ex_Name = '"+name+"';")
    print(query)
    self.cursor.execute(query)
    result = (self.cursor.fetchall())
    print(result)
    return result

# App run to disconnect from DB
  def kill(self):
    self.cursor.close()
    self.cnx.close()

