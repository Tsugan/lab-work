class Class():
  def __init__(self, force, mana, speed, hp):
    self.force=force
    self.mana=mana
    self.speed=speed
    self.hp=hp

wizzard = Class(force = 60, mana = 100, speed = 50, hp = 50)
print(wizzard.mana)
