#***************************************************************************
# MANY INTERESTING THINGS F21
# AUDI LIN & ELIZABETH JIA
#***************************************************************************

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsRead = readFile("planetsData.csv")
contentsToWrite = ""

data = []
for line in contentsRead.split("\n"):
    row = []
    for item in line.split(","):
        row.append(item)
    data.append(row)

print(data)

"""
PLANETS NEED CHNOPS for life

must be in habitable zone

must be 1-2x radius of earth, or else pressure will be too high/low

Areas where conditions might potentially support life is called the "Habitable Zone."
In this area planets nee to be close enough to the Sun for solar energy to drive the chemistry of life.
A common assumption about extraterrestrial life is that water is a requirement: water in its liquid state.
Recently, however, astronomers have discovered that there are other factors that need to be
taken into consideration, such as the atmosphere of the planet/moon,
the amount of heat coming from the planet core, and what geological process,
if any, are taking place on the surface of the planet and/or moon.

All of these can affect a planet's ability to nurture and support life.  


"""
