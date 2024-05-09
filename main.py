import numpy as np # type: ignore
import matplotlib.pyplot as plt 
import functions as myFunc

fileName = 'test'
#imports the data from the image that will be used as a starting point
data, height, width = myFunc.bitmap2Vector(f"{fileName}.bmp")

frames = 200
loops = 0


fig, cont = plt.subplots()
img = cont.matshow(data, cmap="magma")

def updatePlot(nextFrame):
    img.set_data(nextFrame)
    fig.canvas.draw()
    plt.pause(0.01)


imageList= []
for n in range(frames):
    #turns the current vector into an image to create the gif of the final animation
    imageList.append(myFunc.vector2Bitmap(data,f"images\\{fileName}{n}.bmp",4))
    
    #sets the bounds of the vector
    datawEdges = myFunc.mirrorEdges(data)

    #loops through the vector and applies the rules to create the next vector
    mapofNext= []
    total = 0
    for y in range(1,height+1):
        row =[]
        for x in range(1,width+1):
            pixel = datawEdges[y][x]
            neighbors = myFunc.countNext(datawEdges, (x,y))
            nextValue = myFunc.SBrules(pixel,neighbors, [2,3], [3,6])
            row.append(nextValue)
            total += nextValue
        mapofNext.append(row)
    if data == mapofNext:
        print("sable configuration found")
        loops = 1
        break
    
    data = mapofNext

    #checks if the map is empty if it is then there wont be anything going on so we stop the loop
    if total == 0:
        loops = 1
        break
        
    #updatePlot(data)


myFunc.bitmaps2Gif(imageList,f"results\\{fileName}.gif", 15, loops)

myFunc.deleteFiles(imageList)


