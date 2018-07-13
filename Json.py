# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:45:15 2018
"""
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
        
        
        
para = Json()

para.dic
para.update('model','name','FCN')
para.dic

para.show()