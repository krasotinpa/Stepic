with open("input.txt") as fin:
    lines = fin.readlines()

with open("output.txt", "w") as fout:
    fout.writelines(reversed(lines))
