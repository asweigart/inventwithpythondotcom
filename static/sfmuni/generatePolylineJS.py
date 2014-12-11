import munipaths # get the path data we previously grabbed
import random

COLORS = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#800000', '#008000', '#000080', '#808000', '#008080', '#800080']

fo = open('polylineJS.js', 'w')

for route in munipaths.munipaths.keys():
    routeColor = random.choice(COLORS) # choose a random color for this route's paths

    for path in munipaths.munipaths[route]:
        latlngJavaScript = []
        for point in path:
            latlngJavaScript.append('new google.maps.LatLng(%s, %s)' % (point['lat'], point['lon']))
        latlngJavaScript = ', '.join(latlngJavaScript)

        polylineJavaScript = """var routePath = new google.maps.Polyline({
    path: [%s],
    strokeColor: '%s',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });
routePath.setMap(map);

""" % (latlngJavaScript, routeColor)

        fo.write(polylineJavaScript)
fo.close()