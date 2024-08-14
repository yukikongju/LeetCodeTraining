from functools import reduce
from collections import defaultdict

# Box > Content


class Book:

    def __init__(self, label: str, focal_length: int) -> None:
        self.label = label
        self.fl = focal_length

    def __str__(self):
        #  return f"Label: {self.label} ; Focal Length: {self.fl}"
        return f"[{self.label} {self.fl}]"

    def set_fl(self, val: int):
        self.fl = val



def read_inputs(file_name: str):
    with open(file_name, "r") as f:
        res = f.readline().strip().split(',')
    return res

def print_boxes(boxes):
    for idx, box in enumerate(boxes):
        if box:
            print(f"Box {idx}: ", end=" ")
            for book in box:
                print(book, end=" ")
            print('\n')


def part2():
    #  FILE_NAME = "~/Projects/LeetCodeTraining/AdventOfCode/2023/day15/inputs/1.txt"
    FILE_NAME = "inputs/0.txt"
    inputs = read_inputs(file_name=FILE_NAME)

    # --- PART 2
    idx = 0
    box_dct = defaultdict(tuple) # (box, position)
    boxes = [[] for _ in range(256)]
    for i, s in enumerate(inputs):
        separator = '-' if '-' in s else '='
        
        if separator == '-':
            label = s.split('-')[0]
            if label in box_dct:
                # todo: remove in box
                box, pos = box_dct[label]
                pos = int(pos)
                boxes[box] = boxes[box].pop(pos)
                box_dct.pop(label)
                idx=pos
            else:
                idx += 1 # (?)
        else: # sep is '='
            label, fl = s.split('=')
            fl = int(fl)

            if label in box_dct: # replace
                box, pos = box_dct[label]
                boxes[box][pos].set_fl(fl)
            else:
                boxes[idx].append(Book(label=label, focal_length=fl))

        print(f"Step {i+1}: {s}\n")
        print_boxes(boxes)



if __name__ == "__main__":
    part2()

    
