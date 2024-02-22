

class Block():
    def __init__(self, block_id) -> None:
        self.id =  int(block_id)
        self.is_valid = self.block_validation()
    
    def block_validation(self)-> bool:
        if self.id <= 0:
            return False
        return True