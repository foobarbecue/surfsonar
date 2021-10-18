import pandas
import datetime

with open('2021-10-16 23_28_33.924498.txt','r') as datafile:
    data = []
    for line in datafile.readlines():
        try:
            data.append(eval(line))
        except ValueError as ve:
            print(ve)
df = pandas.DataFrame(data)
df.distance = df.distance / 1000.0
df.index=df.timestamp
fig = df.loc['2021-10-17 00:20':'2021-10-17 00:50',['distance','confidence']].plot(backend='plotly')
fig.write_html('_include/sonar_test_trail5_2021-01-17.html')