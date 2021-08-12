import os
from pathlib import Path
import pandas as pd

column = ['Title']
df = pd.read_csv("video_games.csv",header=0)
column=list(df.Title)


def PathGen(file):
    return 'C:/Users/lucas/Documents/GitHub/bluegames/static/img/game-covers/%s.jpg'%(file)

def fileChecker():
    for i in range(len(column)):
        image = column[i]
        apagar = list()
        my_file = Path(PathGen(image))
        if my_file.is_file():
            return
        else:
            apagar.append(i)
    df.drop(apagar)
    print(apagar)
    
    df.to_csv('video_games2.csv')

fileChecker()