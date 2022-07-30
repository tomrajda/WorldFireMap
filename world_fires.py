import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'project_2\chapter_16\Global_Fire_Visual/SUOMI_VIIRS_C2_Global_7d.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lat_index = header_row.index('latitude')
    lon_index = header_row.index('longitude')
    date_index = header_row.index('acq_date')
    brightness_index = header_row.index('bright_ti4')

    # Downloading data from file .csv
    lats = []
    lons = []
    dates = []
    brightnesses = []
    hover_texts = []

    # Stopper of loop (so much data)
    num_loop = 0
    stopper = 10_000

    for row in reader:  
        date = datetime.strptime(row[date_index], "%Y-%m-%d") #strpttime
        try:     
            lat = float(row[lat_index])
            lon = float(row[lon_index])
            brightness = float(row[brightness_index])
            hover_text = f"{date.strftime('%Y-%m-%d')} - {brightness}" #strftime
        except ValueError:
            print(f"No data found for {date}.")
        else:
            lats.append(lat)
            lons.append(lon)
            brightnesses.append(brightness)
            dates.append(dates)
            hover_texts.append(hover_text)
        
        num_loop += 1
        if num_loop == stopper:
            break
        
# Visualization world fire map
title_1 = "Global Fire Activity - Past 7d"
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [0.025*brightness for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title=title_1)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fire_activity.html')



