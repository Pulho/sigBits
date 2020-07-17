#                       sbPy
A Steganography program to deecode LSB or MSB on images
May be useful on your CTF. Feel free to help :)

## Requirements
This program requires the lib Pillow, which can be installed as follows
```
            pip3 install Pillow
```
## How to use it?
   ### Usage
          python3 sbPy.py [OPTIONS] [FILE]
   ### Options
   
   Parameters Option | Functionality
   -------------------------------------| --------------------------------------------------------------------
   -h, --help | List all commands and functionality of them
   -t=<lsb or msb>, --type=<lsb or msb> | Choose between read LSB or MSB (Default is LSB)
   -o=<Order sigle>, --order=<Order sigle> | Read the lsb or msb in the specify order (Default is RGB) 
   -out=<Ouput name>, --output=<Output name> | Choose the name of the output file (Default is outputSB)
   -e=<Row r Column>, --extract=<Row or Column> | Choose between extracting by row or column (Default is Column
  ### Examples
  ```python
    
    python3 sbPy.py -t=lsb -o=rgb -out=MyOutputFile -e=row MyInputFile.png
    python3 sbPy.py -t=LSB -o=BGR -e=column lol.jpg
    python3 sbPy.py --type=Msb --order=GBR --extract=CoLuMn AnotherImage.bmp
  ```
  __Note that the input of each options are not case-sensitive, that means you can write with Caps Lock or not__
  
  ## Upcoming
    Option to select each bit you want to extract from the R,G and B values ( Not just LSB or MSB ) 
