dt = '1403/02/05'

month = int(dt[5:7])
if month == 1:
    result = "ّFarvardin"
elif month == 2:
    result = "Ordibehesht"
elif month == 3:
    result = "Khordad"
else:
    result = "Esfand"
print(result)

match month:
    case 1:
        result = "Farvardin"
    case 2:
        result = "Ordibehesht"
    case 3:
        result = "Khordad"                
    case _:
        result = "Esfand"
print(result)


# if month < 7:
#     pass

match month:
    case 1 | 2 | 3 | 4 | 5 | 6:
        print("Nimsale avval")
    case _:
        print("Nimsale 2vom")
