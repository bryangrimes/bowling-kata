from django.test import TestCase

from score.models import Game


class BowlingTests(TestCase):
    def setUp(self):
        self.game = Game()

    def test_all_gutters_equal_no_score(self):
        self.roll_balls(0)
        self.assertEquals(self.game.score(), 0)

    def test_simple_game(self):
        self.roll_balls(1)
        self.assertEquals(self.game.score(), 20)

    def test_suming_games(self):
        self.roll_balls(3, 10)
        self.roll_balls(4, 10)
        self.assertEquals(self.game.score(), 70)

    def skipped_roll_spare(self):
        self.roll_balls(5, 3)
        self.roll_balls(0, 17)
        self.assertEquals(self.game.score(), 20)

    # HELPERS
    def roll_balls(self, pins, number=20):
        for i in range(number):
            self.game.roll(pins)