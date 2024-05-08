import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import functions as myFunc

#imports the data from the image that will be used as a starting point
data, height, width = myFunc.bitmap2Vector("test.bmp")

datawEdges = myFunc.mirrorEdges(data)

mapofNext= []
for y in range(1,height+1):
    row =[]
    for x in range(1,width+1):
        pixel = datawEdges[y][x]
        neighbors = myFunc.countNext(datawEdges, (x,y))
        nextValue = myFunc.rules(pixel,neighbors, 2)
        row.append(nextValue)
    mapofNext.append(row)

plt.matshow(mapofNext)
plt.colorbar()
plt.show()

