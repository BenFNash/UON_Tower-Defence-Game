class Player:

    # could add name to record score to leaderboard
    def __init__(self, difficulty):
        self.lives = self.get_lives(difficulty)

    def get_lives(self, difficulty):
        lives = 0
        if difficulty == 'easy':
            lives = 20
        elif difficulty == 'medium':
            lives = 15
        elif difficulty == 'hard':
            lives = 10
        else:
            lives = 1
        return lives
