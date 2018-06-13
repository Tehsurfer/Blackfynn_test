from blackfynn import Collection, Blackfynn, TimeSeries
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
import pandas as pd
from git_hub import git_hub

def blackfynn_get(dataset='Timeseries Dataset',collection=0,channels='sine 50 Hz'):

   #establish connection with the API
    bf = Blackfynn(api_token='**********************************',api_secret='**********************************',)
    ds = bf.get_dataset(dataset)
    print(ds)

     # get all timeseries collections
    ts = []
    for ds_temp in ds:
        ts.append(ds_temp)

    
    # NOTE: THIS NEEDS TO BE MADE MODULAR
    data = ts[collection].get_data(length='1s')

    # take the data from the channel and process it to be read by javascript

    #process y values
    temp = np.asarray(data[channels])
    java_y = []
    for el in temp:
        java_y.append(float(str(el)))

    #generate x values
    #NOTE: CURRENTLY NOT MODULAR
    temp2 = np.linspace(0,1,len(temp))
    java_x =[]
    for el in temp2:
        java_x.append(el)

    #write to file
    f = open('data.js', 'w')
    f.write('arbData = ')
    f.write(str(java_y))
    f.write('\ndate = ')
    f.write(repr(java_x))
    f.close()

    #update gitub
    g = git_hub()
    g.update()

    print('update ran successfully')


blackfynn_get(dataset='Demo Data From BlackFynn',collection=2,channels='LG10')
