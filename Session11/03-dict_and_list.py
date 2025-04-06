classroom = [
    {
        'name': 'Hamid',
        'age': 12,
        'scores': [12, 10, 7, 15],
    },
    {
        'name': 'Neda',
        'age': 20,
        'scores': [19, 17, 9, 11],
    }
]

result = []
for student in classroom:
    member = {}
    member.update(name=student.get('name'))
    nomarat = student.get('scores')
    member.update(average=sum(nomarat)/len(nomarat))
    result.append(member)

print(result)