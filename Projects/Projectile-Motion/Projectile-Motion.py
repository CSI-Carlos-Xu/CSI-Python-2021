import math

# gun = "AK-101"
# caliber = "5.56 x 45mm"
# ammunition = "FMJ"
# velocity_ms = 957

# Building = "Ocean Tower"
# BuildingHeight = 243

# gravity_ms = 9.81


def ProjectileFunction(gun:str, caliber:str, ammunition:str, velocity_ms:float, Building:str, BuildingHeight:float, gravity_ms:int):
    time_s = math.sqrt((2 * BuildingHeight) / gravity_ms)
    distance = (velocity_ms * gravity_ms)

    print(f"The gun selected for the experiment is {gun}. The caliber of {gun} is {caliber}.")


    ProjectileFunction("AK-101","5.56 x 45mm","FMJ",957,"Ocean Tower",243,9.81)