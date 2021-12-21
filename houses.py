class House:
    def __init__(self,
                house_number:int = 0,
                is_empty:bool = True
                ) -> None:
        self.house_number = house_number
        self.is_empty = is_empty
    def set_house_number(self, house_number):
        self.house_number = house_number
    def set_is_empty(self, is_empty):
        self.is_empty = is_empty
    def get_house_number(self):
        return self.house_number
    def get_is_empty(self):
        return self.is_empty
        