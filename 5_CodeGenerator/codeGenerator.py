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

#remove \t from begin and \n from end
colections = colections[1:]
colections = colections[:-1]
items = items[1:]
items = items[:-1]

outputTxt = '#include "modules/TestDevice.hpp"\n#include "iolink/iolink.hpp"\n\n#define True true\n\t#define False false\n\nDeviceAB::DeviceAB(uint8_t slot):\nModule(slot, "IODevice")\n{\n\tinitItems();\n\tinitCollections();\n}\n\nDeviceAB::~DeviceAB()\n{\n}\n\nvoid DeviceAB::initItems()\n{\n\t// generated code here\n}\n\nvoid DeviceAB::initCollections(){\n\tstd::shared_ptr<Iolink> Colection = Iolink::getInstance();\n\t// generated code here\n}'

outputTxt = outputTxt.replace("// generated code here", items, 1)
outputTxt = outputTxt.replace("// generated code here", colections, 1)

outputFile = open('output.cpp','w+')
outputFile.write(outputTxt)
outputFile.close()