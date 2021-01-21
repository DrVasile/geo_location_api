import os
import gmplot
import requests
from requests import RequestException
from numpy import random


class CoordinatesPlotter:
    @staticmethod
    def plot_coordinates_on_map():

        apikey = ''

        try:
            response = requests.get("")
            response.raise_for_status()
            print(response)

            response_json = response.json()
            feeds = response_json['feeds']
            lat_list = []
            lon_list = []

            for feed in feeds:
                lat = float(feed['field2'])
                lon = float(feed['field1'])
                lat_list.append(lat)
                lon_list.append(lon)

            curr_lat = lat_list[-1]
            curr_lon = lon_list[-1]

            origin_lat = lat_list[0]
            origin_lon = lon_list[0]
            zoom_lvl = 16

            gmap = gmplot.GoogleMapPlotter(origin_lat, origin_lon, zoom_lvl, apikey=apikey)

            for i in range(100):
                curr_lat += (random.rand() - 0.5) / 10000.0
                lat_list.append(curr_lat)
                curr_lon += (random.rand() - 0.5) / 10000.0
                lon_list.append(curr_lon)

            gmap.plot(lat_list, lon_list, edge_width=7, color='blue')
            print(lat_list[0:5])
            print(lon_list[0:5])

            gmap.draw('map.html')
            os.system('map.html')

        except RequestException:
            print('Request not satisfied!')
