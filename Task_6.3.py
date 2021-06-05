import os
import pickle


dirpath = os.getcwd()

def public():
    for file in os.listdir(dirpath):
        if file.endswith(".dat"):
            with open(file, 'rb') as f:
                data_new = pickle.load(f)
                print(data_new)


public()
