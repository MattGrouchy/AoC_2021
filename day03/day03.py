'''
Project: day03
Created Date: Friday December 17th 2021
Author: Matthew Grouchy
'''


def part1(data):
    ''' function for part 1. Takes binary values.'''
    # gamma rate = most common bit in the column
    # epilson rate = least common bit in the column. i.e., (gamma rate)'.
    # The sums should be larger than or less than half the data
    sums = []
    sums = [0 for bit in data[0]]
    gamma = [0 for bit in data[0]]

    for line in data:
        for i, bit in enumerate(line):
            sums[i] += int(bit)

    dataLength = len(data)
    for i in range(len(sums)):
        gamma[i] = int(sums[i] > (dataLength/2))
        # print(sums[i], dataLength/2)

    epilson = [int(not gamma[i]) for i in range(len(gamma))]

    gammaB = "".join(str(i) for i in gamma)
    epsilonB = "".join(str(i) for i in epilson)
    # product = int(gammaB, 2) * int(epsilonB, 2)
    # print(product)
    return gamma


def find_most_common(data, bit, default):
    # sums = 0
    ones = 0
    zeros = 0
    for line in data:
        if (int(line[bit]) == 1):
            ones += 1
        else:
            zeros += 1

    if (ones == zeros):
        return int(default)
    elif (ones > zeros):
        # ones larger so return 1
        return 1
    else:
        return 0


def find_least_common(data, bit, default):
    # sums = 0
    ones = 0
    zeros = 0
    for line in data:
        if (int(line[bit]) == 1):
            ones += 1
        else:
            zeros += 1

    if (ones == zeros):
        return int(default)
    elif (ones > zeros):
        # ones larger so return 0
        return 0
    else:
        return 1


def part2(data):
    print("part2")
    # life support rating = oxygen generator rating * CO2 scrubber rating

    ''' Consider only the first bit of every number. Discard numbers which do not match the bit criteria.
    If there is only one number left, stop. Otherwise repeat the process starting with the next bit to the right.

    ogr:
        - Determine the most common value in the current bit position, and keep only numbers with that bit in that position.
        - If 0 and 1 are equally common keep only number with 1 in that position.
    '''

    csr = data.copy()
    ogr = data.copy()

    # make a for loop for each bit
    for i in range(len(csr[0])):

        ogr_tokens = []
        ogr_done = False
        csr_tokens = []
        csr_done = False

        most_common = find_most_common(ogr, i, 1)
        least_common = find_least_common(csr, i, 0)
        print("least: ", least_common, "most: ", most_common)

        # if we haven't found the csr_token yet then loop again
        if (not csr_done):
            # loop through every line inside csr. Compare the ith bit to least common. If they are the same, add to csr_tokens
            for j in range(len(csr)):
                if (int(csr[j][i]) == least_common):
                    # add the number from csr to csr_tokens
                    csr_tokens.append(csr[j])

        # Before moving to the next bit, check if csr_tokens has more than one element
        if (len(csr_tokens) <= 1):
            csr_done = True
        else:
            csr = csr_tokens.copy()

        # if we haven't found the ogr_token yet then loop again
        if (not ogr_done):
            # loop through every line inside ogr. Compare the ith bit to the most common. If they are the same, add to ogr_tokens
            for j in range(len(ogr)):
                if (int(ogr[j][i]) == most_common):
                    ogr_tokens.append(ogr[j])

        # Check if ogr_tokens has more than one element
        if (len(ogr_tokens) <= 1):
            ogr_done = True
        else:
            ogr = ogr_tokens.copy()

    print(csr_tokens)
    print(ogr_tokens)

    product = int(csr_tokens[0], 2) * int(ogr_tokens[0], 2)

    val1 = eval("0b"+csr_tokens[0])
    val2 = eval("0b"+ogr_tokens[0])

    print("product: ", val1*val2)


if __name__ == "__main__":
    print("day03 main")
