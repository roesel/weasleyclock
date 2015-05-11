#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
#matplotlib.rc('font', family='Tahoma')
from math import radians, cos, sin, asin, sqrt, pi
import re
import matplotlib.pyplot as plt
import numpy as np



def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

l = np.array(
    [
        [u'Doma', 50.076376, 14.428572, 0.5, 0],
        [u'          Trojanka', 50.074253, 14.415439, 0.5, -pi/4],
        [u'Troja           ', 50.115189, 14.450250, 0.5, pi/4],
        [u'U Terky                  ', 50.134280, 14.382326, 0.5, pi/2],
        [u'            Břehovka', 50.091029, 14.416296, 0.5, -pi/2],
        [u'Podolí                  ', 50.053875, 14.428219, 0.5, 3*pi/4],
        [u'          Na hokeji', 50.104727, 14.493630, 0.8, -3*pi/4]
    ])
    
people = [
    ["david", "blue", "David"], 
    ["peto", "red", "Peto"],        
]

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_theta_offset(0.5*np.pi)
ax.get_yaxis().set_visible(False)
ax.grid()

for p in people:
    with open("output_"+p[0]+".txt", "r") as myfile:
        data = myfile.read().replace('\n', '')
    
    matches = re.findall(
            r"^.*<gx:coord>([0-9\.]*) ([0-9\.]*) ([0-9\.]*)<\/gx:coord>", data)
    
    x = matches[0][1]
    y = matches[0][0]
    
    current_location = '??'
    current_clock_position = pi
    min_distance = 100
    for location in l:
        dist_from_loc = haversine(float(x), float(y),
                                  float(location[1]), float(location[2]))
        if ((dist_from_loc < location[3]) and (dist_from_loc < min_distance)):
            min_distance = dist_from_loc
            current_location = location[0]
            current_clock_position = location[4]
    
    print(u"Current location: ", current_location)
    print(u"Distance from location: ", str(min_distance))
    
    ax.plot([0, current_clock_position], [0, 0.1], '-', linewidth=4, color=p[1], label=p[2])

xticks = []
for a in l[:, 4]:
    xticks.append(float(a))

ax.set_xticks(xticks)
ax.set_xticklabels(l[:, 0].tolist())
plt.savefig('weasley.png')
