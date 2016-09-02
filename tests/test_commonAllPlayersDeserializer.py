import json
import os
from unittest import TestCase

from stats.client.deserializers.common_all_players_deserializer import CommonAllPlayersDeserializer
from stats.data.team import Team
from tests.config import ROOT_DIRECTORY


class TestCommonAllPlayersDeserializer(TestCase):
    def test_instantiation(self):
        deserializer = CommonAllPlayersDeserializer()
        self.assertTrue(deserializer.__dict__ == {})

    def test_deserialize_common_all_players(self):
        with open(os.path.join(ROOT_DIRECTORY, 'tests/files/commonallplayers.json')) as data_file:
            data = json.load(data_file)
            deserialized_players = CommonAllPlayersDeserializer.deserialize_common_all_players(data)
            quincy_acy = deserialized_players[0]
            self.assertEqual(quincy_acy.name, "Quincy Acy")
            self.assertEqual(quincy_acy.nba_id, 203112)
            self.assertEqual(quincy_acy.team, Team.sacramento_kings)