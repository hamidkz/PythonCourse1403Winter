# lst = [7, 8.25, 10, 4, 15]
# passed = [score for score in lst if score >= 10]

people = [
    {
        "name": "Hasan",
        "age": 70,
    },
    {
        "name": "Zahra",
        "age": 20,
    },
    {
        "name": "Hamid",
        "age": 95,
    },
    {
        "name": "Nasim",
        "age": 12,
    },
    {
        "name": "Ali",
        "age": 25,
    },
]


people_over_60 = [person['name'] for person in people if person['age'] > 60]
print(people_over_60)

people = {
    "Ali": 65,
    "Mohammad": 30,
    "Hamid": 70,   
    "Neda": 12,   
    "Zahra": 40,   
}

result = {key: value for key, value in people.items() if value > 60}
print(result)