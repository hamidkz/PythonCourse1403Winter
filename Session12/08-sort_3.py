classroom = [
    {
        "name": "Ali",
        "age": 17,
    },
    {
        "name": "Reza",
        "age": 30,
    },
    {
        "name": "Mina",
        "age": 12,
    },
    {
        "name": "Fatemeh",
        "age": 40,
    },
    {
        "name": "Zeinab",
        "age": 5,
    },
]

classroom.sort(key=lambda person: person.get('age'))
print(classroom)