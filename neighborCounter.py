import matplotlib.pyplot as plt 
import functions as myFunc

data, height, width = myFunc.bitmap2Vector(f"smallTest.bmp")

datawEdges = myFunc.makeEdges(data,1)



mapofNext = []
for y in range(1,height+1):
        row =[]
        for x in range(1,width+1):
            pixel = datawEdges[y][x]
            neighbors = myFunc.countNext(datawEdges, (x,y))
            nextValue = myFunc.rules(pixel,neighbors, 2)
            row.append(nextValue)
        mapofNext.append(row)

myFunc.vector2Bitmap(datawEdges, "smallTestSolid.png", 20)
myFunc.vector2Bitmap(mapofNext, "smallTestSolidStep.png", 20)

plt.matshow(mapofNext)
plt.colorbar()
plt.show()