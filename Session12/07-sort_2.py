names = ["HamidReza", "NazaninZahra", "Amin", "FatemehMina"]

def get_last_char(name: str):
    return name[-1]

# names.sort(key=get_last_char)
# names.sort(key=lambda name:name[0])
# names.sort(key=lambda name:len(name))
# print(names)

sorted_names = sorted(names, key=lambda name:name[0])
print(names)
print(sorted_names)