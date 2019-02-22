# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:11:16 2019

@author: daniel
"""

import pandas
import psycopg2


# Connect to an existing database
conn = psycopg2.connect(dbname="sensor", user="sensor", password="sensor")

# Open a cursor to perform database operations, Posicion para los registros. 
cur = conn.cursor()


url = "https://github.com/freelecorp/prediccion_temperatura/blob/master/sensor1.csv"
df = pandas.read_csv(url)

for index, row in df.iterrows():
    tm = row['Temperatura']
    hm = row['Humedad']
    cl = row['Clima']

    #print(tm,hm)
    
    campos = "temperatura, humedad, clima"
    
    cur.execute("INSERT INTO sensor (" + campos + ") Values (%s, %s, %s)",
                (tm, hm, cl))
    

conn.commit()