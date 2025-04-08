scores = [7, 10, 12, 5, 17]

passed_scores = [s for s in scores if s >= 10]
print(passed_scores)

passed_scores_2 = filter(lambda x: x >= 10, scores)
print(list(passed_scores_2))
