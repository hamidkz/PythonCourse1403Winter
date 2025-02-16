name = "hamid"
age = 43

# result: "My name is Hamid. I'm 43."

result_1 = "My name is " + name.capitalize() + ". I'm " + str(age)
result_2 = f"My name is {name.capitalize()}. I'm {age}."
result_3 = "My name is {0}. I'm {1}.".format(
    name.capitalize(),
    age
)
print(result_3)
