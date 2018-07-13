import os
import json

class Json(object):
    def __init__(self,json_dir = 'json/param.json'):
        self.dic = {}
        self.dir = json_dir
        if os.path.exists(self.dir):
            with open(self.dir,'r') as load_f:
                self.dic = json.load(load_f) #dump
        else:
            print('no argments')
            
    def update(self,scope,name,content):
        self.dic[scope][name] = content
        with open(self.dir,'w') as f:
            f.write(json.dumps(self.dic))
            
    def show(self):
        print(self.dic)
    
    
        
        
