class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def highest_score(self):
        return max(self.scores)

    def last_score(self):
        return self.scores[-1]

    def three_highest_scores(self):
        max_scores = []
        scores2 = self.scores.copy()
        for i in range(0, 3):
            max_score = max(scores2)
            max_score_index = scores2.index(max_score)
            scores2.pop(max_score_index)
            max_scores.append(max_score)
        return max_scores


nick = HighScores([30, 50, 20, 70])

nick.highest_score()
nick.last_score()
nick.three_highest_scores()

