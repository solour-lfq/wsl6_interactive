f = open("label.txt", "r")
d = {}
for line in f:
    txt = line.split(" ")[2]
    if (txt != "U"):
        if (d.get(txt) == None):
            d[txt] = 1
        else:
            d[txt] = d[txt] + 1
print(d)
f.close()