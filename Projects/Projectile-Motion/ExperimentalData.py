import math
class ExperimentData:
    def __init__(self, gun:str, caliber:str, ammunition:str, velocity_ms:float, Building:str, BuildingHeight:float, gravity_ms:int):
        self.gun = gun
        self.caliber = caliber
        self.ammunition = ammunition
        self.velocity_ms = velocity_ms
        self.Building = Building
        self.BuildingHeight = BuildingHeight
        self.gravity_ms = gravity_ms
    

    def getTime(self):
        return (math.sqrt(2 * self.BuildingHeight / self.getgravity_ms()))

    def getDistance(self):
        return(self.velocity_ms * self.getTime())

    