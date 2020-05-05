# zip combine the components


Names = {"Sri", "ravi", "lasy", "rom"}
company ={"dell", "access", "pipe", "micro"}

zipped = set(zip(Names,company))


print(zipped)

for (a,b) in zipped:
    print(a,b)