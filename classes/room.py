class Room:
    def __init__(self, room_id, name, difficulty, duration, min_players, max_players, price_per_player, is_active) -> None:
        self.room_id = room_id
        self.name = name
        self.difficulty = difficulty
        self.duration = duration
        self.min_players = min_players
        self.max_players = max_players
        self.price_per_player = price_per_player
        self.is_active = is_active

    def activate(self):
        pass

    def deactivate(self):
        pass

    def is_valid_players(self, players):
        pass

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        pass