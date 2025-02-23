age = 6
# result: Koodak, Javan, Miansaal, Pir

match age:
    case age if age < 10:
        print("Koodak")
    case age if age < 18:
        print("Nojavan")
    case age if age < 35:
        print("Javan")
    case age if age < 60:
        print("Miansaal")
    case _:
        print("Pir")
    
