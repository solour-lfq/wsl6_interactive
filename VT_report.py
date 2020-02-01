# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:34:49 2020

@author: solour-lfq
"""

import requests, os
url = "https://www.virustotal.com/vtapi/v2/file/report"
f = open("label.txt", "w")
current = "./"
count = 0
files = os.listdir(current)
for file in files:
    if (file[3] == "u"):
        MD = file.split("_")[1]
        params = {'apikey': 'be4bbc6965fde07dd599b430934f8eb46d97d7af65ad97dc612aa2242a19c18b', 'resource': MD}
        try:
            response = requests.get(url, params=params)
            response_json = response.json()
            try:
                detected = response_json["scans"]["Microsoft"]["detected"]
                result = response_json["scans"]["Microsoft"]["result"]
                f.write(MD)
                f.write(" ")
                f.write(str(detected))
                f.write(" ")
                try:
                    result.split(":")
                    f.write(result.split(":")[0])
                    f.write(" ")
                    f.write(result.split(":")[1])
                    f.write("\n")
                except:
                    f.write("U U")
                    f.write("\n")
            except:
                f.write(MD)
                f.write(" ")
                f.write("False U U\n")
        except:
            print("Lose connection...")
            f.write(MD)
            f.write(" ")
            f.write("False U U\n")
        count = count + 1
        print(count)           
f.close()