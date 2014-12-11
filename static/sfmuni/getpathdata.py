import pprint, requests, routedata # routedata has the allRoutes variable with the route name info
import xml.etree.ElementTree as ET

allRoutesPathData = {} # this will be the big dictionary we store all data in
for route in routedata.allRoutes: # loop through all the routes
    allRoutesPathData[route] = [] # this will be a list of lists of {'lon':XXX, 'lat':XXX} dictonaries

    req = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=%s' % (route))
    if req.status_code != 200:
        raise Exception('Could not download route data for %s' % (route))

    # load the downloaded XML text into an XML object we can navigate
    root = ET.fromstring(req.text)
    for child in root[0]: # iterate over all the elements in the <route> element
        if child.tag != 'path':
            continue # skip the non-<path> elements

        pathElement = []
        for point in child: # child is a <path> element, point is a <point> element in the path
            pathElement.append({'lon': point.attrib['lon'], 'lat': point.attrib['lat']}) # append this point to the path
        allRoutesPathData[route].append(pathElement) # append the path to the main dictionary

# output all the data to a file named munipaths.py:
fo = open('munipaths.py', 'w')
fo.write('munipaths = ' + pprint.pformat(allRoutesPathData))
fo.close()
