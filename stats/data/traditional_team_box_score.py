from team import Team
from unit import Unit


class TraditionalTeamBoxScore:
    def __init__(self, team, seconds_played, unit, field_goals_made, field_goal_attempts,
                 three_point_field_goals_made, three_point_field_goal_attempts,
                 free_throws_made, free_throws_attempts, offensive_rebounds, defensive_rebounds, assists,
                 steals, blocks, turnovers, personal_fouls):
        self.team = team
        self.seconds_played = seconds_played
        self.unit = unit
        self.field_goals_made = field_goals_made
        self.field_goal_attempts = field_goal_attempts
        self.three_point_field_goals_made = three_point_field_goals_made
        self.three_point_field_goal_attempts = three_point_field_goal_attempts
        self.free_throws_made = free_throws_made
        self.free_throws_attempts = free_throws_attempts
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls

    @staticmethod
    def create(team_id, unit_name, seconds_played, field_goals_made, field_goal_attempts,
               three_point_field_goals_made, three_point_field_goal_attempts,
               free_throws_made, free_throws_attempts, offensive_rebounds, defensive_rebounds, assists,
               steals, blocks, turnovers, personal_fouls):
        return TraditionalTeamBoxScore(team=Team.get_team_by_id(team_id=team_id),
                                       unit=Unit.get_unit_from_name(unit_name=unit_name),
                                       seconds_played=seconds_played,
                                       field_goals_made=field_goals_made,
                                       field_goal_attempts=field_goal_attempts,
                                       three_point_field_goals_made=three_point_field_goals_made,
                                       three_point_field_goal_attempts=three_point_field_goal_attempts,
                                       free_throws_made=free_throws_made,
                                       free_throws_attempts=free_throws_attempts,
                                       offensive_rebounds=offensive_rebounds,
                                       defensive_rebounds=defensive_rebounds,
                                       assists=assists,
                                       steals=steals,
                                       blocks=blocks,
                                       turnovers=turnovers,
                                       personal_fouls=personal_fouls)