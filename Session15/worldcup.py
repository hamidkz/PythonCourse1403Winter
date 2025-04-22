import random

# تعداد تیمها: 8
# دو گروه چهارتایی

SEED_1 = ['Brazil', 'Spain']
SEED_2 = ['Mexico', 'Holland']
SEED_3 = ['Iran', 'USA']
SEED_4 = ['Canada', 'Norway']

WIDTH = 30

groups = []


def set_group(no, name):
    group = {
        'no': no,
        'name': name,
        'teams': []
    }

    teams = []

    # Choice from SEED 1
    team_seed_1 = random.choice(SEED_1)
    teams.append({
        'Name': team_seed_1,
        'Matches': 0,
        'W': 0,
        'D': 0,
        'L': 0,
        'Z': 0,
        'K': 0,
    })
    SEED_1.pop(SEED_1.index(team_seed_1))

    # Choice from SEED 2
    team_seed_2 = random.choice(SEED_2)
    teams.append({
        'Name': team_seed_2,
        'Matches': 0,
        'W': 0,
        'D': 0,
        'L': 0,
        'Z': 0,
        'K': 0,
    })
    SEED_2.pop(SEED_2.index(team_seed_2))

    # Choice from SEED 3
    team_seed_3 = random.choice(SEED_3)
    teams.append({
        'Name': team_seed_3,
        'Matches': 0,
        'W': 0,
        'D': 0,
        'L': 0,
        'Z': 0,
        'K': 0,
    })
    SEED_3.pop(SEED_3.index(team_seed_3))

    # Choice from SEED 4
    team_seed_4 = random.choice(SEED_4)
    teams.append({
        'Name': team_seed_4,
        'Matches': 0,
        'W': 0,
        'D': 0,
        'L': 0,
        'Z': 0,
        'K': 0,
    })
    SEED_4.pop(SEED_4.index(team_seed_4))

    group['teams'] = teams

    groups.append(group)


def print_group_table(group):
    print('-' * WIDTH)
    print(group.get('name'), '\t\t\t\t', 'M', '\t', 'W', '\t', 'D', '\t', 'L', '\t', 'Z', '\t', 'K')
    print('-' * WIDTH)
    for team in group.get('teams'):
        print(team.get('Name'), '\t\t\t\t\t', team.get('Matches'), '\t', team.get('W'), '\t', team.get('D'), '\t', team.get('L'), '\t', team.get('Z'), '\t', team.get('K'))


def print_all_group_tables():
    for group in groups:
        print_group_table(group)
        print('')


def play_match(team_1, team_2):
    return random.randint(0, 7), random.randint(0, 7)


def set_match_result(group):
    teams = group.get('teams')

    play_order = (
        (
            (0, 2),
            (1, 3),
        ),
        (
            (0, 3),
            (1, 2),
        ),
        (
            (0, 1),
            (2, 3),
        ),
    )

    for n in play_order:
        for m in n:
            result = play_match(teams[m[0]], teams[m[1]])

            group['teams'][m[0]]['Matches'] += 1
            group['teams'][m[1]]['Matches'] += 1

            group['teams'][m[0]]['Z'] += result[0]
            group['teams'][m[1]]['K'] += result[0]

            group['teams'][m[1]]['Z'] += result[1]
            group['teams'][m[0]]['K'] += result[1]

            if result[0] > result[1]: # تیم یک برنده شده
                group['teams'][m[0]]['W'] += 1
                group['teams'][m[1]]['L'] += 1
            elif result[1] > result[0]:
                group['teams'][m[0]]['L'] += 1
                group['teams'][m[1]]['W'] += 1
            else:
                group['teams'][m[0]]['D'] += 1
                group['teams'][m[1]]['D'] += 1


set_group(1, 'Group A')
set_group(2, 'Group B')

set_match_result(groups[0])
set_match_result(groups[1])

print_all_group_tables()

