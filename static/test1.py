import shelve
shelfFile = shelve.open('_generatePagesMTimes')

print([x for x in shelfFile.values()])