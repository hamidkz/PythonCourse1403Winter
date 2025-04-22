PATHS = (
    ('Tehran', 'Karaj'),
    ('Karaj', 'Qazvin'),
    ('Tehran', 'Chaloos'),
    ('Karaj', 'Chaloos'),
    ('Qazvin', 'Rasht'),
    ('Chaloos', 'Ramsar'),
    ('Ramsar', 'Rasht'),
)

paths = []
for p in PATHS:
    paths.append(p)
    paths.append((p[1], p[0]))

ORIGIN = 'Rasht'
DESTINATION = 'Tehran'

# output: [['Tehran', 'Karaj', 'Qazvin']]

def find_next_point(origin: str, history: list = None) -> list:
    if history is None:
        next_points = [p[1] for p in paths if p[0] == origin] # origin: Tehran , next_points: ['Karaj']
    else:
        next_points = [p[1] for p in paths if p[0] == origin and p[1] not in history]

    if len(next_points) == 0:
        return None

    ways = []
    for point in next_points:
        if point == DESTINATION:
            ways.append([DESTINATION]) # ['Karaj']
        else:
            k = find_next_point(point, history + [origin] if history else [origin])
            if k is not None:
                ways.extend(k)

    for way in ways:
        way.insert(0, origin)
    return ways

result = find_next_point(ORIGIN)
print(result)
