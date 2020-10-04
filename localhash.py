import random
import math

'''
Generate random points near origin for exploration
inspired by https://xkcd.com/426/
coordinate transformation from 
https://gis.stackexchange.com/questions/25877/generating-random-locations-nearby

According to preference user should edit these 
homebase_url = googlemaps url for the desired center point for point generation
const_min = minimum distance from the center point
const_max = maximum distance from the center point

'''

#google maps url as the origin point for generation
homebase_url = 'https://www.google.com/maps/@60.1702083,24.9520565,17z'
const_min = 1 #in km = minimum distance
const_max = 3.5 #in km = maximum distance

const_r = 111.300 #equatorial earth radius

url_params = homebase_url.split('@')[1]
lat_origin = float(url_params.split(',')[0])
lon_origin = float(url_params.split(',')[1])

u = ( const_min + random.random() * ( const_max-const_min ) ) / const_max
v = random.random()
w = const_max/const_r * math.sqrt(u)
t = 2 * math.pi * v

x = w * math.cos(t)
lon_diff = w * math.sin(t)
lat_diff = x / math.cos( lat_origin / 360 * (2*math.pi) )

print(f'https://www.google.com/maps/@{lat_origin+lat_diff},{lon_origin+lon_diff},19z')

