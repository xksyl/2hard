input_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in input_numbers:
    empty_string = ""
    for p in range(1, 21):
        for j in range(p + 1, 21):
            if i % (p + j) == 0:
                empty_string = empty_string + ''.join(map(str, [p, j]))
            else:
                continue

    print(i, "-", empty_string)