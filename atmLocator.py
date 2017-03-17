from urllib2 import urlopen
import cStringIO
import json
import Image

API_KEY = 'AIzaSyA2Xzos3wIhIMJMtYtnnmF9LnqjZhkkRdQ'
MAP_KEY = 'AIzaSyDH275XorzUB0D_lBW2LvH-GW0tDMcm694'
radius = 50000
latitude = 28.604009 #Have to get these from client side
longitude = 77.048278 #Have to get these from client side


result = urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + "," + str(longitude) + "&radius=" + str(radius) + "&type=" + "atm" + "&key=" + API_KEY +"&keyword=federalbank")

json_obj = json.load(result)

for x in range(len(json_obj['results'])):
    if(json_obj['results'][x]['name'][:12].lower() == 'federal bank'):
        print json_obj['results'][x]['name'].lower()[:12]
        print json_obj['results'][x]['name']
        print json_obj['results'][x]['vicinity']
        #print str(json_obj['results'][x]['geometry']['location']['lat']) + " " + str(json_obj['results'][x]['geometry']['location']['lng'])
        print "________________________________________ \n"

string = ''

for y in range(len(json_obj['results'])):
    if(json_obj['results'][y]['name'][:12].lower() == 'federal bank'):
        string = string + "&markers=size:mid%7Ccolor:blue%7C" + str(json_obj['results'][y]['geometry']['location']['lat']) + "," + str(json_obj['results'][y]['geometry']['location']['lng'])

smap = urlopen("https://maps.googleapis.com/maps/api/staticmap?maptype=hybrid&size=400x400" + string + "&key=" + MAP_KEY)

mapImageFile = cStringIO.StringIO(smap.read())
img = Image.open(mapImageFile)
img.show()
