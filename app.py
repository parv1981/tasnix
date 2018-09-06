# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 12:53:48 2018

@author: Parvesh Joon
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 12:52:53 2018

@author: Parvesh Joon
"""

from flask import Flask
import json
app = Flask(__name__)


@app.route("/getName/<state>")
def getName(state):
    with open("mocks/mocks3.json") as input_file:
        people_state = json.load(input_file)
        flg = "n"
        for key,item in people_state.items():
            if key == state:
                flg = "y"
                return item 
        if flg == "n":
            return "State not Found"
#        print(people_state)
#        return "True"

@app.route("/getState/<name>")
def getState(name):
    with open("mocks/mocks3.json") as input_file:
        people_state = json.load(input_file)
        flg = "n"
        for key,item in people_state.items():
            state = key
            name_list = [x.strip() for x in item.split(',')]
            for i in range(len(name_list)):
                if name_list[i] == name:
                    flg = "y"
                    return state
        if flg == "n":
            return "Name not Found"

if __name__ == "__main__":
    app.run()
