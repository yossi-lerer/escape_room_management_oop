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

    def is_valid_players(self, players):
        if self.min_players <= players <= self.max_players:
            return True
        return False

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(
            room_id=data['room_id'],
            name=data['name'],
            difficulty=data['difficulty'],
            duration=data['duration'],
            min_players=data['min_players'],
            max_players=data['max_players'],
            price_per_player=data['price_per_player'],
            is_active=data['is_active']
        )