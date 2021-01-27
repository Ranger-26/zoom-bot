from schedule import * 
import pandas as pd

df = pd.read_csv('classes.csv', sep = ';')

time = [x for x in df['time']]
default = [x for x in df['default']]
monday = [x for x in df['monday']]
tuesday = [x for x in df['tuesday']]
wendsday = [x for x in df['wendsday']]
thursday = [x for x in df['thursday']]
friday = [x for x in df['friday']]
letter = [x for x in df['letter']]

a_day  = []
b_day = []

for a,b,c,d,e,f,g,h in zip(time,default,monday,tuesday,wendsday,thursday,friday,letter):
    new = Class(Timestamp(a[1:a.find(',')],a[a.find(',')+1:-1]),b,c,d,e,f,g)
    if h == 'a':
        a_day.append(new)
    elif h == 'b':
        b_day.append(new)

