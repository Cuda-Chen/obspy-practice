#/usr/bin/env python

'''
read seismogram file 
'''
from obspy import read
st = read('../data/test.mseed')
print(st) # we can see there are three traces
print(len(st)) # length of the stream
tr = st[0] # get trace[0]
print(tr)

'''
accessing meta data
'''
print(tr.stats) # print trace stats
print(tr.stats.station) # print station info
print(tr.stats.mseed.encoding) # MiniSEED data encoding

'''
accessing waveform data
'''
print(tr.data)
print(tr.data[0:3]) # you can slice the data
print(len(tr)) # ... or output the length of data

'''
data preview

Make a plot for fast preview of the waveform.
we can see there are three figures.
'''
st.plot()
