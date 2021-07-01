import sqlite3


class BestScoreDB:
    def __init__(self):
        self.conn = sqlite3.connect('flappybird.db')

        self.cursor = self.conn.cursor()

    def get_best_score(self):
        self.cursor.execute('SELECT * FROM BestScore WHERE id = 9263')
        result = self.cursor.fetchone()
        return result[1]

    def update_best_score(self, score):
        self.cursor.execute(f'UPDATE BestScore SET score = {score} WHERE id = 9263')
        self.conn.commit()

if __name__ == '__main__':
    bs = BestScoreDB()
    bs.update_best_score(3)
    print(bs.get_best_score())
    bs.update_best_score(0)
    print(bs.get_best_score())