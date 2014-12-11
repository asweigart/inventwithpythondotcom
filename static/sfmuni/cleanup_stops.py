import munistops

# collect all routes to each stop
stopsToRoutes = {}
stopsFoundSoFar = []
for route in munistops.munistops:
    if route in ['1AX', '1BX', '5L', '8AX', '8BX', '9L', '14L', '14X', '28L', '31AX', '31BX', '38L', '38AX', '38BX', '71L', 'K OWL', 'L OWL', 'M OWL', 'N OWL', 'T OWL' '59', '60', '61', '30X', 'NX']:
        continue # skip redundant routes
    for stop in munistops.munistops[route]:
        if stop['title'] in stopsFoundSoFar:
            continue # don't have stops listed more than once (happens when, for example, inbound and outbound stops are at the same intersection)
        stopsFoundSoFar.append(stop['title'])
        stopsToRoutes.setdefault(stop['stopId'], {'lat':None, 'lon':None, 'title':None, 'routes':[]})
        stopsToRoutes[stop['stopId']]['lat'] = stop['lat']
        stopsToRoutes[stop['stopId']]['lon'] = stop['lon']
        stopsToRoutes[stop['stopId']]['title'] = stop['title']
        if route not in stopsToRoutes[stop['stopId']]['routes']:
            stopsToRoutes[stop['stopId']]['routes'].append(route)

# compile the javascript code
stopToRoutesJS = []
for stopId in stopsToRoutes.keys():
    stopInfo = stopsToRoutes[stopId]
    stopToRoutesJS.append('"%s": {"lat": %s, "lon": %s, "title": "%s", "routes": %s}' % (stopId, stopInfo['lat'], stopInfo['lon'], stopInfo['title'], stopInfo['routes']))

# output javascript
fo = open('stops_cleanedup.js', 'w')
fo.write("""
// Actually, you can just hover over the markers and a tool tip shows up, so I don't need the stopInfoWindow
/*var stopInfoWindow = new google.maps.InfoWindow({
    disableAutoPan: true
    });*/

var stopsList = ["%s"];
var stopsToRoutes = {%s};
for (var i = 0; i < stopsList.length; i++) {
    currentStopId = stopsList[i];
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(stopsToRoutes[currentStopId]['lat'], stopsToRoutes[currentStopId]['lon']),
        map: map,
        title: stopsToRoutes[currentStopId]['title']
        });
    /*(function(thisContent, thisMarker) { // making this into a closure so that "thisContent" keeps its value
        google.maps.event.addListener(marker, 'click', function() {
            stopInfoWindow.close();
            stopInfoWindow.setContent(thisContent);
            stopInfoWindow.open(map, thisMarker);
            });
    })(stopsToRoutes[currentStopId]['title'] + '<br />' + stopsToRoutes[currentStopId]['routes'].join(), marker);*/
}
""" % ('","'.join(stopsToRoutes.keys()),  ','.join(stopToRoutesJS)))
fo.close()