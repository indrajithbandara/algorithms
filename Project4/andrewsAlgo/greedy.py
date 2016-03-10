import math

def cityDistance(c1, c2):
	# each input is an array with city, xcoord and ycoord in the 0, 1, 2 spots
	d = int(round(math.sqrt( (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2 )))
	return d

#for use with the 2-opt part
def totalDist(path):
    finalDistance = 0
    for i in range(1,len(path)):
        finalDistance += cityDistance(cities[path[i-1]], cities[path[i]])
    finalDistance += cityDistance(cities[path[0]], cities[path[len(path) - 1]])
    return finalDistance


def greedyTSP(cities):
    visited = list()
    mustVisit = cities

    current = mustVisit[0]

    visited.append(current)
    mustVisit.remove(current)

    tourLength = 0

    while(len(mustVisit) > 0):
        shortestPath = float('inf') # set to infinity
        for i in range(0, len(visited)):
            for j in range(0, len(mustVisit)):
                distance = cityDistance(visited[i], mustVisit[j])
                if distance < shortestPath:
                    shortestPath = distance
                    nearestCity = mustVisit[j]
        tourLength += shortestPath
        visited.append(nearestCity)
        mustVisit.remove(nearestCity)

    lastDistance = cityDistance(visited[0], visited[len(visited)-1])

    tourLength += lastDistance


    print tourLength
    print len(visited)
    for city in visited:
        print city[0]


    return (visited, tourLength)




