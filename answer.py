import fileinput
import sys

def answer(lines: str) -> int:
    length: str = None
    sum: int = 0
    position: int = 0

    for line in lines:
        lineValue = int(line)
        if (lineValue == -999):
            break
        elif(position == 0):
            length = line
            position += 1
        else:
            if(int(line) > 0):
                sum += lineValue
            position += 1

    return sum

if __name__ == '__main__':
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        lines = data_file.readlines()

    print(answer(lines))