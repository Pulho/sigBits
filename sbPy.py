import os
import binascii
import sys
from PIL import Image

def help(func=None):
    if func == None:
        print("Usage:\n\tsbPy [OPTIONS] [FILE]")
        print("\nOptions:\n\t-t=<lsb or msb>, --type=<lsb or msb>:\n\t\tChoose between read LSB or MSB (Default is LSB)\n\n\t-o=<Order sigle>, --order=<Order sigle>:\n\t\tRead the lsb or msb in the specify order (Default is RGB)\n\n\t-out=<Ouput name>, --output=<Output name>\n\t\tChoose the name of the output file (Default is outputSB)\n\n\t-e=<Row r Column>, --extract=<Row or Column>\n\t\tChoose between extracting by row or column (Default is Column)")
    return

def writeResults(outputFile, dataBin):
    resultFile = open(outputFile + ".txt", "w")
    size = len(dataBin)
    for i in range(0,size,8):
        value = int("".join(dataBin[i:i+8]),2)
        if value >= 32 and value <= 126:
            resultFile.write(chr(value))
    resultFile.write("\n")
    resultFile.close()

def getSB(file, ord, type, outFile, ext):
    dataBin = []
    print(ord)
    print(type)
    print(outFile)
    print(ext)
    if type == "LSB":
        with Image.open(file) as img:
            width, height = img.size
            xPattern = height
            yPattern = width
            if ext == "ROW":
                xPattern = width
                yPattern = height
            for x in range(0, xPattern):
                for y in range(0, yPattern):
                    if ext == "ROW":
                        pixel = list(img.getpixel((x,y)))
                    else:
                        pixel = list(img.getpixel((y,x)))
                    R = bin(pixel[0])[-1:]
                    G = bin(pixel[1])[-1:]
                    B = bin(pixel[2])[-1:]
                    if ord == "RGB":
                        dataBin.append(R)
                        dataBin.append(G)
                        dataBin.append(B)
                    elif ord == "RBG":
                        dataBin.append(R)
                        dataBin.append(B)
                        dataBin.append(G)
                    elif ord == "GRB":
                        dataBin.append(G)
                        dataBin.append(R)
                        dataBin.append(B)
                    elif ord == "GBR":
                        dataBin.append(G)
                        dataBin.append(B)
                        dataBin.append(R)
                    elif ord == "BRG":
                        dataBin.append(B)
                        dataBin.append(R)
                        dataBin.append(G)
                    else:
                        dataBin.append(B)
                        dataBin.append(G)
                        dataBin.append(R)
    else:
        with Image.open(file) as img:
                width, height = img.size
                xPattern = height
                yPattern = width
                if ext == "ROW":
                    xPattern = width
                    yPattern = height
                for x in range(0, xPattern):
                    for y in range(0, yPattern):
                        if ext == "ROW":
                            pixel = list(img.getpixel((x,y)))
                        else:
                            pixel = list(img.getpixel((y,x)))
                        R = bin(pixel[0])[2]
                        G = bin(pixel[1])[2]
                        B = bin(pixel[2])[2]
                        if ord == "RGB":
                            dataBin.append(R)
                            dataBin.append(G)
                            dataBin.append(B)
                        elif ord == "RBG":
                            dataBin.append(R)
                            dataBin.append(B)
                            dataBin.append(G)
                        elif ord == "GRB":
                            dataBin.append(G)
                            dataBin.append(R)
                            dataBin.append(B)
                        elif ord == "GBR":
                            dataBin.append(G)
                            dataBin.append(B)
                            dataBin.append(R)
                        elif ord == "BRG":
                            dataBin.append(B)
                            dataBin.append(R)
                            dataBin.append(G)
                        else:
                            dataBin.append(B)
                            dataBin.append(G)
                            dataBin.append(R)
    writeResults(outFile, dataBin)

def checkParameters(file, parameters):
    order = 'RGB' # Default
    sbType = 'LSB' # Default
    outputFile = "outputSB" # Default
    extract = "COLUMN" # Default

    size = len(parameters)
    for i in range(size):
        # Help
        if parameters[i] == "--help" or parameters[i] == "-h":
            help()
            exit()
        # Order
        elif parameters[i][:3] == "-o=":
            order = parameters[i][3:].upper()
            if len(order) > 3:
                print(f"INPUT ERROR: Parameter '{order}' Exceeds parameter size ( Expected length = 3 )")
                exit()
            if order.find("R") == -1 or order.find("G") == -1 or order.find("B") == -1:
                print(order.find("R"), order.find("G"), order.find("B"))
                print(f"INPUT ERROR: Parameter '{order}' Has different characters than 'R,G,B' or repetitive character")
                exit()
        elif parameters[i][:8] == "--order=":
            order = parameters[i][3:].upper()
            if len(order) > 3:
                print(f"INPUT ERROR: Parameter '{order}' Exceeds parameter size ( Expected length = 3 )")
                exit()
            if order.find("R") == -1 or order.find("G") == -1 or order.find("B") == -1:
                print(f"INPUT ERROR: Parameter '{order}' Has different characters than 'R,G,B' or repetitive character")
                exit()
        # Type
        elif parameters[i][:3] == "-t=":
            sbType = parameters[i][3:].upper()
            if sbType != "LSB" and sbType != "MSB":
                print(f"INPUT ERROR: Type '{sbType}' Not recognized")
                exit()
        elif parameters[i][:7] == "--type=":
            sbType = parameters[i][7:].upper()
            if sbType != "LSB" and sbType != "MSB":
                print(f"INPUT ERROR: Type '{sbType}' Not recognized")
                exit()
        # Output file name
        elif parameters[i][:5] == "-out=":
            outputFile = parameters[i][5:]
        elif parameters[i][:9] == "--output=":
            outputFile = parameters[i][9:]
        # Row or Column
        elif parameters[i][:3] == "-e=":
            extract = parameters[i][3:].upper()
        elif parameters[i][:10] == "--extract=":
            extract = parameters[i][10:].upper()
        else:
            print(f"INPUT ERROR: Parameter '{parameters[i]}' Not recognized")
            exit()
    getSB(file, ord=order, type=sbType, outFile=outputFile, ext=extract)


def main(): # Adjustments for parameters
    if len(sys.argv) < 2:
        help()
        return
    elif len(sys.argv) == 2 and ( sys.argv[1] == '--help' or sys.argv[1] == '-h'):
        help()
        return
    checkParameters(sys.argv[-1:][0], sys.argv[1:-1])
main()

