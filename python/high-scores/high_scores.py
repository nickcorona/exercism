class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        max_scores = []
        scores2 = self.scores.copy()

        i = 0
        while i < 3:
            try:
                max_score = max(scores2)
            except ValueError:
                break
            max_score_index = scores2.index(max_score)
            scores2.pop(max_score_index)
            max_scores.append(max_score)
            i += 1
        return max_scores
