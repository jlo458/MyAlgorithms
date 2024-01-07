# This program is my intro to greedy algorithms 
# I take a set of radio stations and a set of states
# My goal is to find the least amount of radio stations covering these states as efficiently as possible

statesNeeded = set(["mt", "wa", "or", "ca", "id", "nv", "ut", "az"])  

stations = {} 
stations["kOne"] = set(["ut", "nv", "id"]) 
stations["kTwo"] = set(["wa", "id", "mt"]) 
stations["kThree"] = set(["ca", "nv", "or"]) 
stations["kFour"] = set(["nv", "ut"])
stations["kFive"] = set(["ca", "az"]) 

finalStations = set()  

while statesNeeded:
  bestStation = None
  statesCovered = set()
  for station, statesPerStation in stations.items(): 
    covered = stations[station] & statesNeeded 
    if len(covered) > len(statesCovered): 
      bestStation = station 
      statesCovered = covered 

  finalStations.add(bestStation)
  statesNeeded = statesNeeded - statesCovered

print(finalStations)
