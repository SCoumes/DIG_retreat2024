flagColor = dict()
flagColor["Afghanistan"] = [112, 111, 116, 106]
flagColor["Albania"] = [106, 112]
flagColor["Argentina"] = [114,  116,  110]
flagColor["Austria"] = [106,  116]
flagColor["Barbados"] = [110,  114,  112]
flagColor["Belarus"] = [106,111]
flagColor["Belgium"] = [106,110,112]
flagColor["Bosnia and Herzegovina"] = [110, 116, 114]
flagColor["Brazil"] = [111,  116,  114,  110]
flagColor["British Empire"] = [106, 116, 114]
flagColor["Bulgaria"] = [106, 116, 111]
flagColor["Canada"] = [116,  106]
flagColor["Chile"] = [116, 106, 114]
flagColor["China"] = [106, 110]
flagColor["Colombia"] = [110, 106, 114]
flagColor["Croatia"] = [116, 106, 114]
flagColor["Denmark"] = [106, 116]
flagColor["East Germany"] = [110, 106, 112]
flagColor["German Reich"] = [116, 112, 106]
flagColor["Germany"] = [110, 106, 112]
flagColor["Greece"] = [114,  116]
flagColor["India"] = [116, 107, 111]
flagColor["Iran"] = [106, 116, 111]
flagColor["Israel"] = [114,  116]
flagColor["Italy"] = [116,  106,  111]
flagColor["Japan"] = [106, 116]
flagColor["Kenya"] = [111,  116,  112,  106]
flagColor["Kingdom of England"] = [106, 116]
flagColor["Kosovo"] = [116, 114, 110]
flagColor["Malaysia"] = [106, 116, 114, 110]
flagColor["Montenegro"] = [106, 110]
flagColor["Myanmar"] = [110, 111, 106, 116]
flagColor["Nepal"] = [106, 114, 116]
flagColor["Netherlands"] = [106, 114, 116]
flagColor["North Macedonia"] = [110, 106]
flagColor["Pakistan"] = [111, 116]
flagColor["Panama"] = [106, 116, 106]
flagColor["Peru"] = [106, 116]
flagColor["Poland"] = [106, 116]
flagColor["Portugal"] = [111,  106]
flagColor["Republic of Ireland"] = [111,  116,  107]
flagColor["Russia"] = [116,  106,  114]
flagColor["Serbia"] = [116,  106,  114]
flagColor["Slovenia"] = [106, 116, 114]
flagColor["South Africa"] = [106, 116, 111, 114, 110, 112]
flagColor["Soviet Union"] = [106, 110]
flagColor["Spain"] = [110,  106]
flagColor["State of Palestine"] = [106, 116, 111, 112]
flagColor["Sweden"] = [110,  114]
flagColor["Switzerland"] = [106,  116]
flagColor["Trinidad and Tobago"] = [116,  106,  112]
flagColor["Turkey"] = [106, 116]
flagColor["Ukraine"] = [110, 114]
flagColor["United Arab Emirates"] = [106, 116, 111, 112]
flagColor["United States"] = [116,  106,  114]
flagColor["Weimar Republic"] = [110, 112, 106]
flagColor["West Germany"] = [110, 112, 106]

id = 1000
nationalityNames = dict()
nationalityColors = dict()
for key in flagColor.keys():
    nationalityColors.update({id : flagColor[key]})
    nationalityNames.update({id : key})
    id += 1

print("GETTING CSV")
for key in nationalityNames.keys():
    print(str(key) +  "," +  nationalityNames[key])


print("\n \n \n")
print("GETTING DICT")
print(nationalityColors)

