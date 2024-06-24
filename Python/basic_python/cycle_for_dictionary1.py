# Напишите функцию get_competition_data().
def get_competition_data(data):
    scores = {}
    for race in data:
        for team, score in race.items():
            if team not in scores:
                scores[team] = 0
            scores[team] += score

    winner_team = None
    winner_score = 0
    for team, score in scores.items():
        if score > winner_score:
            winner_score = score
            winner_team = team

    print(f"Команды, участвовавшие в гонке: {', '.join(sorted(scores.keys()))}")
    print(f'В гонке победила команда {winner_team} c результатом {winner_score} баллов')

races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]


get_competition_data(races_data)