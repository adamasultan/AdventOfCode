import os

def main(elves :list[list]) -> int:
    elf_totals = []
    for elf in elves:
        current_elf_total = 0
        for calories in elf:
            current_elf_total+= calories
        elf_totals.append(current_elf_total)
    biggest = 0
    for total in elf_totals:
        if total > biggest:
            biggest = total
    return biggest
#print(os.listdir())

def open_file(givenfile) ->list:
    infile = open(givenfile, "r")
    blocks = []
    current_block = []
    for line in infile:
        if line.strip(): #Check if the line is not empty
            current_block.append(line.strip()) # add the string in that line without the newline character
        else: # if the line is empty
            blocks.append(current_block) # add the newly created block of strings to a list of blocks
            current_block = [] # set the new current block to empty again
    for block in blocks: 
        for i in range(len(block)):
            block[i] = int(block[i]) # change each string to int
    return blocks # return list of lists of ints
print(main(open_file('elves.txt')))