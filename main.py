from PIL import Image
import numpy as np
from pathlib import Path

row_length = int(input("Row lenght for your image: "))
inputTxt = Path("input.txt")
if not inputTxt.is_file():
    print("Please enter bits to convert in input.txt")

def parse_string_to_2d_array(input_string: str, row_length: int) -> list:
    input_string = input_string.replace('0', '2').replace('1', '0').replace('2', '1').replace(" ", "")
    result = []
    for i in range(0, len(input_string), row_length):
        row = list(map(int, input_string[i:i + row_length]))
        result.append(row)
    return result

with open("input.txt", "r") as bits:
    bitStr: str = bits.read()

data: list = parse_string_to_2d_array(bitStr, row_length)

try:
    array = np.array(data, dtype=np.uint8) * 255 
except ValueError:
    print("Lenght of your bytes must be divisible by row length you entered!")
else:
    image = Image.fromarray(array, 'L')  # 'L' - black and white image mode
    image.save('output.png')
    print("Succesfully saved your image, check out output.png file!")