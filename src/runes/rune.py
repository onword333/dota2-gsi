class Rune:
    def __init__(self, name, appearance_time) -> None:
        self.name = name
        self.appearance_time = appearance_time

    def time_until_next_appearance(self, data):
        time_to_next_rune = 0
        if 'map' in data:
            game_time = data['map']['clock_time']                
            next_rune_time = self.appearance_time * (int(game_time // self.appearance_time) + 1)
            time_to_next_rune = next_rune_time - game_time
        return time_to_next_rune

    def __repr__(self) -> str:
        return f"{self.name} Rune appears every {self.appearance_time} seconds"

