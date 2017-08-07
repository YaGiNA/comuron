from unicodedata import east_asian_width


def length(strings):
    len = 0
    for (i, char) in enumerate(strings):
        if "NaH".count(east_asian_width(char)) > 0:
            len += 1
        else:
            len += 2
        if len > 50:
            return strings[:i] + "@" + length(strings[i:])
    return strings


with open('report.txt', mode='w') as f:
    r = open('report.md', 'r')
    for line in r:
        if not (line[0] == "#" or line[0] == "(" or line[0] == '"'):
            line = "　" + line
        pr_line = length(line)
        pr_line = pr_line.replace("@", "\n")
        f.write(pr_line)
    r.close()
