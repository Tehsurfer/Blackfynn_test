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

    # show general channel information for our files
    for ts_temp in ts:
        print("---------------- Information for File: {} ----------------\n").format(str(ts_temp.name))

        # nicely print the names and IDs of the channels for the first timeseries file
        print "The channels available for this file are:"
        for i in ts_temp.channels:
            print i.name, "with ID = ", i.id

        # show the number of channels in file
        print
        print("File '{}' has {} channels\n").format(ts_temp.name, len(ts_temp.channels))


    # Get data for 1s length of time
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


blackfynn_get(channels='sine 1 Hz')
