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
contentsToWrite = "Planet,Score"

# putting data into 2D list
n = 0 # 0 being the column names
data = []
for line in contentsRead.split("\n"):
    row = []
    for item in line.split(","):
        row.append(item)
    data.append(row)
    n += 1

# analyzing data for each planet
def findScore(planetData):
    score = 0

    part1 = 1.0 # factors: CHNOPS
    for i in range(1, 7):
        part1 *= float(planetData[i])
    
    radiusFactor = float(planetData[7]) / 6378.0 # ideally 1-2
    part2 = 1.0
    if radiusFactor < 1:
        part2 = 1 - (radiusFactor - 1)**2
    elif radiusFactor > 2:
        part2 = 1 - (radiusFactor - 2)**2
    if part2 < 0: part2 = 0
    
    part3 = float(planetData[8]) * float(planetData[9])

    score = (0.3 * part1) + (0.4 * part2) + (0.3 * part3)
    score = score ** 2 # to make differences even bigger
    return score

for planetIndex in range(1, n):
    planetData = data[planetIndex]
    score = findScore(planetData)
    print(planetData[0], score)
    contentsToWrite += "\n" + planetData[0] + "," + str(score)

writeFile("results.csv", contentsToWrite)

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
