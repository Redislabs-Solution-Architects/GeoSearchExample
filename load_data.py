import hashlib 
import gpxpy 
import gpxpy.gpx 
from redisearch import Client, Query, TextField, GeoField, NumericField


client = Client(
   'attractions',
   host='127.0.0.1',
   password='',
   port=6379
   )

client.create_index([
   TextField('title', weight=5.0),
   TextField('description'),
   NumericField('verified', sortable=True),
   GeoField('geo'),
])


gpx_file = open('All_States_Offbeat_Tourist_Attractions.gpx', 'r', encoding='utf-8')

gpx = gpxpy.parse(gpx_file)

for waypoint in gpx.waypoints:
    if "Verified" in waypoint.comment:
        v = 1
    else:
        v = 0
    t = "%s,%s,%s" %(waypoint.name, waypoint.longitude, waypoint.latitude)
    client.add_document(
        hashlib.md5(t.encode('utf-8')).hexdigest(),
        description = waypoint.name,
        geo = "%s,%s" %(waypoint.longitude, waypoint.latitude),
        verified = v,
    )