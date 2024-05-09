import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import imageio
import os

def bitmap2Vector(filepath):
    
    #opens the image as a black and white picture
    img = Image.open(filepath).convert("1")

    #gets the dimensions of the image
    width, height = img.size
    
    #print(f"height = {height}, width = {width}")
    #starts the vector that will contain the image as individual pixels
    vectorR= []

    #loops through each pixel and stores it in a list that gets appended to vectorR
    for y in range(height):
        row = []

        for x in range(width):
            #gets the value of the pixels
            pixel = img.getpixel((x,y))
            #makes the white pixels dead (0) and the black ones alive (1)
            if pixel > 123:
                row.append(1)
            else:
                row.append(0)
        vectorR.append(row)

    return(vectorR, height, width)

def vector2Bitmap(vector,filename, scale = 1):
    height = len(vector)
    width = len(vector[0])

    img = Image.new("1", (width,height))
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            pixels[x,y] = vector[y][x]*255

    if scale != 1:
        newHeight = height*scale
        newWidth = width*scale
        newImg = img.resize((newWidth,newHeight))
        img = newImg

    img.save(filename)
    return(filename)

def bitmaps2Gif(filePaths, outputName, fps, loop):
    images = []
    
    for path in filePaths:
        images.append(imageio.imread(path))

    imageio.mimsave(outputName, images, fps=fps, loop=loop)
    print(f"saved series of images as {outputName}")

def deleteFiles(filepaths):
    
    for file in filepaths:
        if os.path.exists(file):
            try:
                os.remove(file)
            except:
                print(f"error deleting {file}, L")
        else:
            print(f"{file} don't exist bruv")

#vector that extends the matrix to have cells with the same value on the outside
def makeEdges(vector, value = bool):
    height = len(vector)
    width = len(vector[0])+2
    result = [[value]*width]
    for y in range(height):
        row = [value]
        row.extend(vector[y])
        row.append(value)
        result.append(row)
    result.append([value]*width)

    return(result)

#this does the same thing to the overall structure of the code, where it extends the matrix but this time it mirrors the other side of the matrix simulating a spherical map
def mirrorEdges(vector):
    height = len(vector)-1
    width = len(vector[0])-1
    result = []
    toprow = [vector[height][width]]
    toprow.extend(vector[height])
    toprow.append(vector[height][0])
    result.append(toprow)
    for y in range(height+1):
        row = [vector[y][width]]
        row.extend(vector[y])
        row.append(vector[y][0])
        result.append(row)
    botrow=[vector[0][width]]
    botrow.extend(vector[0])
    botrow.append(vector[0][0])
    result.append(botrow)

    return(result)

#counts the number of neighbors to the cell at pos asuuming that the cell isnt at the edge, which shouldnt be the case since I format the edges
def countNext(map, pos = (1,1)):
    x,y = pos
    xvalues = [x-1,x,x+1]
    yvalues = [y-1,y,y+1]
    
    bohrs = 0

    for why in yvalues:
        for eks in xvalues:
            bohrs += map[why][eks]
    
    #this method also counts the cell itself as a neighbor so we can correct it with this line
    bohrs -= map[y][x]

    return(bohrs)


def rules(status: bool, next: int, n: int =2):
    if next == n:
        return (status)
    elif next == n+1:
        return (1)
    else:
        return(0)
        
def SBrules(status, next, s, b):
    if status:
        if next in s:
            return(1)
        else:
            return(0)
    else:
        if next in b:
            return(1)
        else:
            return(0)
    




