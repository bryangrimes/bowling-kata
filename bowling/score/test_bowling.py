from django.test import TestCase

from score.models import Game


class BowlingTests(TestCase):
    def setUp(self):
        self.game = Game()

    def test_all_gutters_equal_no_score(self):

        for i in range(20):
            self.game.roll(0)

        self.assertEquals(self.game.score(), 0)


    def test_simple_game(self):
        for i in range(20):
            self.game.roll(1)

        self.assertEquals(self.game.score(), 20)