from unittest import TestCase

from nba_data.data.advanced_box_score import AdvancedBoxScore


class TestAdvancedBoxScore(TestCase):
    def test_instantiation(self):
        test_box_score = AdvancedBoxScore("bae", "jadley", "foo")
        self.assertIsNotNone(test_box_score)
        self.assertEqual(test_box_score.game_id, "bae")
        self.assertEqual(test_box_score.player_box_scores, "jadley")
        self.assertEqual(test_box_score.team_box_scores, "foo")
