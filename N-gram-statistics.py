import os
N = 4
HEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
LABEL = {"PUA":0, "SoftwareBundler":1, "Torjan":2, "PWS":3, "TrojanDownloader":4, "VirTool":5, "BackDoor":6, "Misleading":7, "BrowserModifier":8, "TorjanSpy":9, "Ransom":10, "Program":11, "Hacktool":12, "DDoS":13, "Virus":14}
count_statistics = {}
#paths = {"./VirusShare_00dee9ce6cbd5e0997cf703825a32d76", "./VirusShare_0a0a82c14074b691069a603c066c22f6", "./VirusShare_0b4dff474876dc48f6e23841709ce3cb"}
paths = os.listdir("./")
count = 0;
for path in paths:
    count = count + 1
    path = path.rstrip()
    file = open(path, "rb")
    for line in file:
        tl = str(line).rstrip().split("\\x")[1:]
        tl = [element for element in tl if (len(element) == 2) and (element[0] in HEX) and (element[1] in HEX)]
        for i in range(len(tl) - (N - 1)):
            txt = "".join(tl[i:i + N])
            if (not (txt[0:2] == txt[2:4] and txt[2:4] == txt[4:6] and txt[4:6] == txt[6:8])):
                if (count_statistics.get(txt) == None):
                    count_statistics[txt] = 1
                else:
                    count_statistics[txt] = count_statistics[txt] + 1
    count_statistics = dict((key, value) for key, value in count_statistics.items() if value > 2)
    file.close()
    print("%i, %i" % (count, len(count_statistics)))

op = open("grams.txt", "w")
print(len(count_statistics))    
sorted_grams = sorted(count_statistics.items(), key=lambda x: x[1], reverse = True) 
for i in range(100000):
    op.write(sorted_grams[5000 + i])
    op.write("\n")
op.close()
