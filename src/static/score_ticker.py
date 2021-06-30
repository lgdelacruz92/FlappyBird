
class ScoreTicker:
    def __init__(self):
        self.toggle = False
        self.current_score = 0

    def update(self, bird, rects):
        for rect in rects:
            if bird.x > rect[0] and bird.x < rect[0] + rect[2]:
                self.toggle = True
            elif bird.x > rect[0] + rect[2]:
                if self.toggle == True:
                    self.current_score += 1
                    self.toggle = False

    def get_score(self):
        return self.current_score

    def get_score_str(self):
        return str(self.current_score)

    def reset(self):
        self.toggle = False
        self.current_score = 0