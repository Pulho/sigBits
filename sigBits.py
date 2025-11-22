import argparse
from PIL import Image

def setupArgparser():
    parser = argparse.ArgumentParser(
        prog='SigBits',
        description='A Steganography significant bits image decoder'
    )
    parser.add_argument('-i', '--input', type=str.lower, help='Specifies the input file that the program will analyze', required=True)
    parser.add_argument('-t', '--type', type=str.lower, help='Choose between read LSB or MSB (Default is LSB)', default='lsb', choices=['lsb', 'msb'], required=False)
    parser.add_argument('-o', '--order', type=str.lower, help='Read the LSB/MSB in the specify order (Default is RGB)', default='rgb', choices=['rgb', 'rbg', 'grb', 'gbr', 'brg', 'bgr'], required=False)
    parser.add_argument('-out', '--output', type=str, help='Choose the name of the output file', required=True)
    parser.add_argument('-bf', '--bruteforce', type=bool, help='Bruteforce all possible permutations of the R, G, and B channel', required=False)
    parser.add_argument('-e', '--extract', type=str.lower, help='Choose between extracting by row or column (Default is Column)', default='column', choices=['column', 'row'], required=False)
    parser.add_argument('-b', '--bits', type=str.lower, help='Choose the bits you want to extract information from. If this option is provided, the --type (-t) parameter will be ignored', required=False) # Rever
    return parser

def extract_binary(strInput: str, bits: str):
    strInput = strInput[2:]
    outputList = []

    while len(strInput) < 8:
        strInput = "0" + strInput

    for i in range(0,8):
        if bits[i] == '1':
            outputList.append(strInput[i])
    return outputList

def write_output_file(outputFile: str, dataBin: list):
    resultFile = open(outputFile, "w")
    
    size = len(dataBin)
    for i in range(0,size,8):
        # Each 8 bits convert into a int value
        value = int("".join(dataBin[i:i+8]),2)
        # Check if it is in the printable range
        if value >= 32 and value <= 126:
            resultFile.write(chr(value))
    resultFile.write("\n")
    resultFile.close()

def get_significant_bits(input: str, order: str, output: str, bruteforce: bool, extract: str, bits: str):
    dataBin = []
    with Image.open(input) as img:
        width, height = img.size
        xPattern = height
        yPattern = width
        
        if extract == "row":
            xPattern = width
            yPattern = height
        
        if bruteforce:
            for bruteforceOrder in ['rgb', 'rbg', 'grb', 'gbr', 'brg', 'bgr']:
                get_significant_bits(input=input, order=bruteforceOrder, output=bruteforceOrder.upper() + output, bruteforce=False, extract=extract, bits=bits)
        else:
            for x in range(0, xPattern):
                for y in range(0, yPattern):
                    if extract == "row":
                        pixel = list(img.getpixel((x,y)))
                    else:
                        pixel = list(img.getpixel((y,x)))

                    R = extract_binary(bin(pixel[0]), bits)
                    G = extract_binary(bin(pixel[1]), bits)
                    B = extract_binary(bin(pixel[2]), bits)
                    
                    if order == "rgb":
                        dataBin.extend(R)
                        dataBin.extend(G)
                        dataBin.extend(B)
                    elif order == "rbg":
                        dataBin.extend(R)
                        dataBin.extend(B)
                        dataBin.extend(G)
                    elif order == "grb":
                        dataBin.extend(G)
                        dataBin.extend(R)
                        dataBin.extend(B)
                    elif order == "gbr":
                        dataBin.extend(G)
                        dataBin.extend(B)
                        dataBin.extend(R)
                    elif order == "brg":
                        dataBin.extend(B)
                        dataBin.extend(R)
                        dataBin.extend(G)
                    else:
                        dataBin.extend(B)
                        dataBin.extend(G)
                        dataBin.extend(R)        
            write_output_file(outputFile=output, dataBin=dataBin)
    
def main():
    parser = setupArgparser()
    args = parser.parse_args()
    
    if not args.bits:
        if args.type == 'lsb':
            args.bits = "00000001"
        else:
            args.bits= "10000000"
            
    get_significant_bits(input=args.input, order=args.order, output=args.output, bruteforce=args.bruteforce, extract=args.extract, bits=args.bits)
    print("Done, check the output file(s)!")


if __name__ == '__main__':
    main()

