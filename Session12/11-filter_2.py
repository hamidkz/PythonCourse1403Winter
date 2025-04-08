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

result = filter(lambda d: d.get("age") > 20, classroom )
print(list(result))