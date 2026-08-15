temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)

for temp in temperaturas:
    if temp < 37.5:
        print(temp, "- Normal")
    elif temp <= 38.5:
        print(temp, "- Febre moderada")
    else:
        print(temp, "- Febre alta")
