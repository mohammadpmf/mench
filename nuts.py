class Nut:
    def __init__(self,
                color:str = None,
                name:str = None,
                nut_number:int = 0,
                position:int = -1,
                has_finished:bool = False,
                has_passed_40:bool = False
                ) -> None:
        self.color = color
        self.name = name
        self.nut_number = nut_number
        self.position = position
        self.has_finished = has_finished
        self.has_passed_40 = has_passed_40
    def set_color(self, color):
        self.color = color
    def set_name(self, name):
        self.name = name
    def set_nut_number(self, nut_number):
        self.nut_number = nut_number
    def set_position(self, position):
        self.position = position
    def set_has_finished(self, has_finished):
        self.has_finished = has_finished
    def set_has_passed_40(self, has_passed_40):
        self.has_passed_40 = has_passed_40
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
    def get_nut_number(self):
        return self.nut_number
    def get_position(self):
        return self.position
    def get_has_finished(self):
        return self.has_finished
    def get_has_passed_40(self):
        return self.has_passed_40
