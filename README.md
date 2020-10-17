#                       sigBits
A Steganography significant bits image decoder
May be useful in some CTF. Feel free to help :)
( This program use Python3 )

## Requirements
This program requires the lib Pillow, which can be installed as follows
```
            pip install Pillow
```
## How to use it?
   ### Usage
          python sigBits.py [OPTIONS] [FILE]
   ### Options
   
   Parameters Option | Functionality
   -------------------------------------| --------------------------------------------------------------------
   -h, --help | List all commands and functionality of them
   -t=<lsb or msb>, --type=<lsb or msb> | Choose between read LSB or MSB (Default is LSB)
   -o=<Order sigle>, --order=<Order sigle> | Read the lsb or msb in the specify order (Default is RGB) 
   -out=<Ouput name>, --output=<Output name> | Choose the name of the output file (Default is outputSB)
   -e=<Row or Column>, --extract=<Row or Column> | Choose between extracting by row or column (Default is Column)
   -b=<8 Bits>, --bits=<8 Bits> | Choose the bits you want to extract info ( Have higher priority than '--type or -t' )
  ### Examples
  ```
    
    python sbPy.py -t=lsb -o=rgb -out=MyOutputFile -e=row MyInputFile.png
    python sbPy.py -t=LSB -o=BGR -e=column SomeImage.jpg
    python sbPy.py --type=Msb --order=GBR --extract=CoLuMn AnotherImage.png
  ```
  __Note that the input of each options are not case-sensitive, that means you can write with Caps Lock or not__
