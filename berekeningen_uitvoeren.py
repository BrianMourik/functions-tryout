def calculate(som):
    if "x" in som:   
        strSplit = som.split("x")
        return int(strSplit[0]) * int(strSplit[1])

    elif "*" in som:
        strSplit = som.split("*")
        return int(strSplit[0]) * int(strSplit[1])

    elif "-" in som:
        strSplit = som.split("-")
        return int(strSplit[0]) - int(strSplit[1])

    elif "+" in som:
        strSplit = som.split("+")
        return int(strSplit[0]) + int(strSplit[1])

    elif "/" in som:
        strSplit = som.split("/")
        return int(strSplit[0]) / int(strSplit[1])

    elif ":" in som:
        strSplit = som.split(":")
        return int(strSplit[0]) / int(strSplit[1])    

print(calculate(input("SOM ")))