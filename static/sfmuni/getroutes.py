import requests
import xml.etree.ElementTree as ET

# use the requests module to download the webpage (you can copy and paste this page into your browser to see it for yourself)
req = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni')

tree = ET.fromstring(req.text) # parse the XML in the webpage
root = tree.getroot() # get the first (root) XML element
routes = {} # this dictionary will store all the routes names and their titles
for child in root: # loop through all the routes
    routes[child.attrib['tag']] = child.attrib['title'] # key is route name, value is full route name

# save the routes dictionary to a text file (routedata.py) to use later
import pprint
fo = open('routedata.py', 'w')
fo.write('allRoutes = ' + pprint.pformat(routes))
fo.close()
