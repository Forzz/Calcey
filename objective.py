class Objective:
    def __init__(self, obj_id, obj_name, obj_amount):
        self.obj_id = obj_id
        self.obj_name = obj_name
        self.obj_amount = obj_amount

    def __str__(self):
        return f'{self.obj_name} | {self.obj_amount} ₽ | ID - {self.obj_id}'
        