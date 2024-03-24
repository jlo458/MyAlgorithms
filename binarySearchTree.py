# This is my binary search tree data structure 
# It finds items at average time of O(logn) and inserts items also in O(logn) time 
# Can be altered to also delete items 

# Works as an alternative for binary search if index not important and inserting/deleting is needed


binTree = {}
binTree["dave"] = ["adi","manny"]
binTree["manny"] = ["maggie","suzie"]
binTree["adi"] = ["",""]
binTree["maggie"] = ["",""]
binTree["suzie"] = ["",""] 

def findPerson(theName, currentName):
  try:
    if theName == currentName: 
      print(theName,"was found!")
  
    elif max(theName, currentName) == theName: 
      currentName = binTree[currentName][1]
      findPerson(theName, currentName)
  
    else:
      currentName = binTree[currentName][0]
      findPerson(theName, currentName)

  except: 
    print(theName,"was not found!")


def addPerson(theName, currentName):
  try:
    if theName == currentName: 
      print(theName,"was already in tree!")

    elif max(theName, currentName) == theName: 
      currentNewName = binTree[currentName][1]
      if currentNewName == "":
        binTree[currentName][1] = theName
        binTree[currentNewName] = ["",""]
        print("person added!")
        print(binTree[currentName],binTree[currentNewName])

      else:  
        currentName = currentNewName
        addPerson(theName, currentName)

    else:
      currentNewName = binTree[currentName][0]
      if currentNewName == "":
        binTree[currentName][0] = theName
        binTree[currentNewName] = ["",""]
        print("person added!")
        print(binTree[currentName],binTree[currentNewName])

      else: 
        currentName = currentNewName
        addPerson(theName, currentName)

  except: 
    print("Tree not found")

personToFind = "steve"
addPerson(personToFind, "dave")



