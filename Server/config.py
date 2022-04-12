import os
import json

class Config:
    names = []
    path = "Server\\Config"

    def __init__(self) -> None:
        self.loadFolder()
        
    def loadFolder(self):
        try:
            files = os.listdir(self.path)
            for file in files:
                self.names.append(file[:-5])
        except FileNotFoundError:
            print("Error: File not found. Current Path: " +  os.getcwd())

    def getNames(self):
        self.names = []
        self.loadFolder()
        return self.names

    def loadConfig(self, file):
        f = open(self.path + "//" + file + ".json")
        data = json.load(f)
        f.close()
        return data

    def saveConfig(self, file, data):
         f = open(self.path + "//" + file + ".json", 'w')
         json.dump(data, f)
         f.close()
         

    def deleteConfig(self, file):
        if os.path.exists(self.path + "//" + file + ".json"):
            os.remove(self.path + "//" + file + ".json")
        else:
            print("The file does not exist")


# simpiConfigs = Config()
# data = simpiConfigs.loadConfig("try")
# simpiConfigs.saveConfig("try2", data)