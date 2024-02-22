

class Location():
    def __init__(self, location) -> None:
        self.coordinates = [int(value) for value in location[0].split(",")]
        self.is_valid = self.location_validation()
    
    def location_validation(self):
        if len(self.coordinates) != 3:
            return False
           
        if self.coordinates[2] > 256 or self.coordinates[2] < 1:
            return False

        return True
        
        
        