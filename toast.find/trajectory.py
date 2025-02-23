import datetime
import camera
from dataclasses import dataclass

@dataclass
class LocatedToast:
    x: int
    y: int
    time: float

@dataclass
class Vec2D:
    x: int
    y: int    

# def findVectors(toast0: LocatedToast,toast1: LocatedToast):
#     vecX = toast1.x - toast0.x
#     vecY = toast1.y - toast0.y 

#     return (vecX,vecY)

def findXVelocity(toast0: LocatedToast,toast1: LocatedToast):
    return ((toast1.x - toast0.x) / (toast1.time - toast0.time))

def findYVelocity(toast0: LocatedToast,toast1: LocatedToast):
    return (toast1.y + (0.5 * 9.81 * (toast1.time * toast1.time)) - toast0.y) / toast1.time

def findXPos(xVel, time):
    return xVel * time

def findYPos(yVel, time):
    return yVel * time - (0.5 * 9.81 * (time * time))

if __name__ == "__main__":
    results = camera.watch_for_toast()
    print(results)
    # vectors = findVectors()