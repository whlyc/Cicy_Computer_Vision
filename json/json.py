import os
import json

class Json(object):
    def __init__(self):
        self.dic = {}
        if os.path.exists('test.json'):
            with open('test.json','r') as load_f:
                self.dic = json.load(load_f) #dump
        else:
            print('no argments!')
            
    def update(self,scope,name,content):
        self.dic[scope][name] = content
        with open('test.json','w') as f:
            f.write(json.dumps(self.dic))
            
    def show(self):
        print(self.dic)
    def set_dir(self,this):
        
        
