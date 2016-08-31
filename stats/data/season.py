from enum import Enum


class Season(Enum):
    season_2015 = "2015-16"

    @staticmethod
    def get_season(season_name):
        season = season_name_map.get(season_name)

        if season is None:
            raise RuntimeError("Unknown season name: %s", season_name)

        return season

season_name_map = {
    "2015-16": Season.season_2015
}