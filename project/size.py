import os


def convert(x):
    output = ""
    if x >= 1000000000:
        x = x // 1000000000
        output += str(x) + " " + "GB"
        if x >= 10:
            output += "            VERY HEAVY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        elif x >= 5:
            output += "            HEAVY !!!!!!!!!!!!"
        else:
            output += "            ALREADY BIG !!!!"
    elif x >= 1000000:
        x = x // 1000000
        output += str(x) + " " + "MB"
    elif x >= 1000:
        x = x // 1000
        output += str(x) + " " + "KB"
    else:
        output += str(x) + " " + "B"
    return output


def run(path, graph, lvl, slash, want, allfiles, tab):
    files = os.listdir(path)
    size = 0
    output = ""
    for i in files:
        try:
            if os.path.isfile(path + slash + i):
                y = os.path.getsize(path + slash + i)
                size += y
                if (graph or lvl <= want) and allfiles:
                    output += tab + i + "*" + str(y) + '\n'
            if os.path.isdir(path + slash + i):
                x, y = run(path + slash + i, graph, lvl + 1, slash, want, allfiles, tab + '\t')
                size += y
                if graph or lvl <= want:
                    output += tab + "-- " + i + slash + "*" + str(y) + '\n' + x
        except:
            output += tab + "!!!" + i + "!!! MISSING PERMISSION," + '\n'
    return output, size


def decode(code):
    size, output, number = "", "", False
    for i in range(0, len(code)):
        if code[i] == '*':
            number = True
        elif code[i] == '\n' and code[i - 1] != ',':
            output += " " + convert(int(size)) + '\n'
            size = ""
            number = False
        elif number:
            size += code[i]
        else:
            output += code[i]
    return output