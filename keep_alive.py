from flask import Flask
from threading import Thread
from flask_restful import Resource, Api

import sys
import fileinput

app = Flask('')
api = Api(app)

def get_Data(data):
  
  #Split string and insert the new average
  type, av = data.split("-")

  # replace average
  for i, line in enumerate(fileinput.input('Data/Player_Data.txt', inplace=1)):
   
    wordsList = line.split()
    
    if type in wordsList:

      # Check if it's not supposed to calc average
      if type != "Completed_Tutorial":
        #Add new number + the current
        newAverage = round((int(av)+int(wordsList[2]))) / 2
        
        sys.stdout.write(line.replace("= "+wordsList[2], "= "+str(round(newAverage))))
      else:
        newValue = int(av) + int(wordsList[2])
        sys.stdout.write(line.replace("= "+wordsList[2], "= "+str(newValue)))
    else:
        sys.stdout.write(line)
      
  return 1 

def add_Error(data):
    f = open("Data/Errors.txt","a")
    f.write(data+"\n")
    f.close()
    
    return 1

# Player Data
class Data(Resource):
  def get(self, data):
    return get_Data(data)

# Errors
class Error(Resource):
  def get(self, data):
    return add_Error(data)
    
#player data endpoint
api.add_resource(Data,'/api/plrData/<string:data>')
#errors endpoint
api.add_resource(Error,'/api/errors/<string:data>')

def run():
  app.run(host='0.0.0.0',port=7210)

def keep_alive():
  t = Thread(target=run)
  t.start()