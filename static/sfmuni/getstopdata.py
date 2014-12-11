import pprint, requests, routedata
import xml.etree.ElementTree as ET

allRoutesStopData = {} # this will be the big dictionary we store all data in
for route in routedata.allRoutes:
    allRoutesStopData[route] = []

    req = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=%s' % (route))
    if req.status_code != 200:
        raise Exception('Could not download route data for %s' % (route))

    # load the downloaded XML text into an XML object we can navigate
    root = ET.fromstring(req.text)
    for child in root[0]: # iterate over all the elements in the <route> element
        if child.tag != 'stop':
            continue # skip the non-<stop> elements

        allRoutesStopData[route].append({'title': child.attrib['title'],
                                         'lon': child.attrib['lon'],
                                         'lat': child.attrib['lat'],
                                         'stopId': child.attrib['stopId']}) # append the stop

# output all the data to a file named munistops.py:
fo = open('munistops.py', 'w')
fo.write('munistops = ' + pprint.pformat(allRoutesStopData))
fo.close()
