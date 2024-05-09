import functions as myFun

file = "cat"

filetoscale = myFun.bitmap2Vector(f"{file}.bmp")[0]

myFun.vector2Bitmap(filetoscale, f"{file}Scaled.png",4)