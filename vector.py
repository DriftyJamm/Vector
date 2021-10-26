import numpy
import math
clas Vector3:
  def __init__(self, x, y, z)
    self.x = x
    self.y = y
    self.z = z

  def scale(self, num):
    self.x *= num
    self.y *= num
    self.z *= num

class Vector:
  def __init__ (self, x, y):
    self.x = x
    self.y = y

  def add(self, vec):
    self.x += vec.x
    self.y += vec.y
  
  def subtract(self, vec):
    self.x -= vec.x
    self.y -= vec.y

  def dot(self, vec):
    return self.x * vec.x + self.y * vec.y    

  def cross(self, vec):
    ah = self.hypot()
    bh = vec.hypot()
    theta = math.acos(self.dot(vec)/ah*bh) 
    sin = math.sin(theta)
    n = Vector3(0, 0, 1)
    return n.scale(ah * bh * sin).z

  def hypot(self):
    return (self.x **2 + self.y **2)**0.5

