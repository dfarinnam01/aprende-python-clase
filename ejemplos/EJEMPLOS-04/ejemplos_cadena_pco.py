cadena = "pablo"
for i in range(len(cadena)):
    print(cadena[:i+1])
match cadena:
    case "pablo":
        print("es pablo pa")