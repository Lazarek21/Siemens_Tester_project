import sys
import json

f = open(sys.argv[1])
inputJson = json.load(f)

items = ""
colections = ""

for colection in inputJson:
    for item in inputJson[colection]:
        colections += '\tColection.{}->push("{}");\n'.format(colection, item["name"])
        items += '\tinitDataItem("{}", {}, "{}", {});\n'.format(item["name"], item["tag"], item["type"], item["size"])

f.close()

colections = colections[1:]
colections = colections[:-1]
items = items[1:]
items = items[:-1]

templateFile = open("template.cpp", "r")

outputTxt = templateFile.read()

outputTxt = outputTxt.replace("// generated code here", items, 1)
outputTxt = outputTxt.replace("// generated code here", colections, 1)

outputFile = open('output.cpp','w+')
outputFile.write(outputTxt)
outputFile.close()