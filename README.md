#                       sigBits
A Steganography Significant Bits Image Decoder
May be useful for CTF challenges and general stego analysis.
Feel free to contribute!
_(This program uses Python 3)_

## ✨Features

- Extract data from LSB, MSB, or custom bit positions
- Support for RGB channel permutation reading
- Bruteforce mode to automatically test all RGB permutations
- Row-wise or column-wise extraction
- Custom output file naming
- Simple CLI interface
- Built on Python 3 + Pillow

## ⚙️ Requirements
This program requires the lib Pillow, which can be installed as follows
```
            pip install Pillow
```
## How to use it
   ### 🧭 Usage
          SigBits [-h] -i INPUT [-t {lsb,msb}] [-o {rgb,rbg,grb,gbr,brg,bgr}] -out OUTPUT [-bf BRUTEFORCE]
               [-e {column,row}] [-b BITS]
   ### 🛠️ Options
   
   Parameters Option | Functionality
   -------------------------------------| --------------------------------------------------------------------
   -h, --help | List all commands and functionality of them
   -i, --input | Specifies the input file that the program will analyze
   -t, --type | Choose between read LSB or MSB (Default is LSB)
   -o, --order | Read the LSB/MSB in the specify order (Default is RGB)
   -out, --output | Choose the name of the output file
   -bf, --bruteforce | Bruteforce all possible permutations of the R, G, and B channel
   -e, --extract |  Choose between extracting by row or column (Default is Column)
   -b, --bits | Choose the bits you want to extract information from. If this option is provided, the --type (-t) parameter will be ignored

   ### Examples
   Extract using default LSB mode
   ```
   python sigBits.py -i image.png -out output.txt
   ```
   
   Extract using MSB
   ```
   python sigBits.py -i image.png -t MSB -out output.txt
   ```
   
   Extract using custom bit positions
   ```
   python sigBits.py -i image.png -b 00000001 -out output.txt
   ```
   
   Bruteforce all RGB permutations
   ```
   python sigBits.py -i image.png -bf -out output.txt
   ```
   
   Specify custom output file
   ```
   python sigBits.py -i image.png -out output.txt
   ```
   Read bits in BGR order
   ```
   python sigBits.py -i image.png -o BGR -out output.txt
   ```

## 🤝 Contributing

Contributions, issues, and pull requests are welcome!
If you’d like to add features or improve decoding methods, feel free to open a PR.
