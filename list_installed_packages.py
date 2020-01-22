import pkg_resources

#Keep an empty list to store packages/modules later
lstPackages = []

#Get working set iterator from pkg_resources
workingSet = pkg_resources.working_set.__iter__()
for entry in workingSet:
    #Load working set into a list (to sort in a good way) with package name, and version
    lstPackages.append(entry.key + " " + entry.version)

#Sort the packages(assending by default)
lstPackages.sort()

#Print sorted packages
for pkg in lstPackages:
    print(pkg)

#Terminate the program
exit()
