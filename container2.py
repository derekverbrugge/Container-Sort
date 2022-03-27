class Container:
  def __init__(container, name, domesticFlag, region, periodmin, periodmax, associatedReportingMarks, length, type):
    container.name = name
    container.domesticFlag = domesticFlag
    container.region = region
    container.periodMin = periodmin
    container.periodMax = periodmax
    container.associatedReportingMarks = associatedReportingMarks
    container.length = length
    container.type = type

  def printContainerName(container):
      print("This container's name is " + container.name + ".")
  
  def printIsDomestic(container):
    if container.domesticFlag == 1:
        print("This container is domestic.")
    else:
        print("Conatiner is not domestic.")

  def printContainerRegion(container):
      print("This container's region is " + container.region + ".")

  def printContainerPeriod(container):
      print("This container existed from " + str(container.periodMin) + " - " + str(container.periodMax))

  def printContainerAssociatedReportingMarks(container):
      print("This container's associated reporting marks are " + container.associatedReportingMarks + ".")

  def printContainerLength(container):
    print("This container is " + str(container.length) + "' long.")

  def printContainerType(container):
    if container.type == "std":
        print("This is a standard container")
    if container.type == "ins":
        print("This is an insulated container")
    if container.type == "ref":
        print("This is a refrigerated container")
    if container.type == "tnk":
        print("This is a tank container")

  def printAllContainerData(container):
    print("============== Container ==============")
    container.printContainerName()
    print("================ Data ================")
    container.printIsDomestic()
    container.printContainerRegion()
    container.printContainerPeriod()
    container.printContainerAssociatedReportingMarks()
    container.printContainerLength()
    container.printContainerType()

class Containers:
    def __init__(containers, containerList):
        containers.containerList = containerList

    def printAllContainerNames(containers):
    
        print("============== Containers ==============")
        for x in containers.containerList:
            x.printContainerName()
        print(" ")

    def printAllContainerData(containers):
        
        print("========= Containers with Data =========")
        for x in containers.containerList:
            x.printAllContainerData()
        print(" ")

c1 = Container("One", 0, "World", 2000, 2010, "NONE", 40, "std")
c2 = Container("JBHunt", 1, "US", 1990, 2000, "BNSF", 40, "ins")
c3 = Container("Hyundai", 0, "Korea", 1990, 2000, "NONE", 20, "std")
c4 = Container("Swift", 1, "US", 1990, 2000, "BNSF", 40, "ref")
c5 = Container("Evergreen", 0, "US", 1990, 2000, "BNSF", 40, "std")
c6 = Container("China", 0, "China", 1990, 2000, "BNSF", 40, "std")

clist = [c1,c2,c3,c4,c5,c6]
flist = []
compli = []

compList = Containers(compli)
containerList = Containers(clist)
filterList = Containers(flist)

containerList.printAllContainerNames()
#containerList.printAllContainerData()

#test filter settings =======================================================
domesticFlag = 0                                                #0 or 1
date = 1998 
regions = ["NONE"]
types = ["std", "ins"]                                          #std, ins, ref, tnk
lengths = [40]                                                  #20, 40, 48
associatedReportingMarks = ["NONE"]

inList = 0

#Container Sort =============================================================
#def containerSort(containerList, date, domesticFlag, ):


#populate by date
for x in clist:
    if x.periodMin < date and date < x.periodMax:
        #don't add duplicates
        for y in flist:
            if y == x:
                inList = 1
        if inList == 0:
            flist.append(x)

#filter by region
compli.clear()
if regions[0] != "NONE":
    for x in flist:
        for y in regions:
            if x.region == y:
                compli.append(x)
    flist.clear()
    for x in compli:
        flist.append(x)


#filter by reporting marks
if associatedReportingMarks[0] != "NONE":
    compli.clear()
    for x in flist:
        for y in associatedReportingMarks:
            if x.associatedReportingMarks == y:
                compli.append(x)
    flist.clear()
    for x in compli:
        flist.append(x)

#validates types
compli.clear()
for x in flist:
    for y in types:
        if x.type == y:
            compli.append(x)
flist.clear()
for x in compli:
    flist.append(x)

#validates lengths
compli.clear()
for x in flist:
    for y in lengths:
        if x.length == y:
            compli.append(x)
flist.clear()
for x in compli:
    flist.append(x)

#validates domestic flag
compli.clear()
for x in flist:
    if x.domesticFlag == domesticFlag:
        compli.append(x)
flist.clear()
for x in compli:
    flist.append(x)

#compList.printAllContainerNames() #for checking the comparison list

filterList.printAllContainerNames()
