import nuts

class Player:
    def __init__(self,
                color:str = None,
                name:str = None,
                player_number:int = 0,
                rank:int = -1,
                has_finished:bool = False,
                nuts:list=[nuts.Nut(),nuts.Nut(),nuts.Nut(),nuts.Nut()]
                ) -> None:
        self.color = color
        self.name = name
        self.player_number = player_number
        self.rank = rank
        self.has_finished = has_finished
        self.nuts = nuts
    def set_color(self, color):
        self.color = color
    def set_name(self, name):
        self.name = name
    def set_player_number(self, player_number):
        self.player_number = player_number
    def set_rank(self, rank):
        self.rank = rank
    def set_has_finished(self, has_finished):
        self.has_finished = has_finished
    def set_nuts(self, nuts):
        self.nuts = nuts
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
    def get_player_number(self):
        return self.player_number
    def get_rank(self):
        return self.rank
    def get_has_finished(self):
        return self.has_finished
    def get_nuts(self):
        return self.nuts