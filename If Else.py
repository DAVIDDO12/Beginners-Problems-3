print("You are exploring a rainforest in search of treasure.Legend has it that there are some buried on a nearby island.")
action=input("You come across a lake.Do you want to swim across, or wait for a boat?(swim or wait)")
if action=="swim":
  print("You get eaten by a hungry shark. Game over.")
else:
  print("A boat arrives and you arrive at the island safely.")
  action2=input("You come to a cave.Do you want to venture inside or walk on?(venture or walk on)")
if action2=="venture":
  print("You are squished by boulders never to be seen again. Game over.")
else:
  print("You walk on around the cave safely.")
  action3=input("You encounter a tiger.Do you run or attack it?(run or attack)")
if action3=="run":
  print("The tiger reaches you and shreds you to pieces. Game over.")
else:
  print("You shred the tiger to pieces and eat it raw.")
  action4=input("You’re at a crossroads.Do you go left, right, or straight?(left, right or straight)")
if action4=="right":
  print("You march on and find the buried treasure! Yippee!!")
if action4=="left":
  print("You are trampled by a herd of wildebeest. Game over.")
if action4=="straight":
  print("You get stung by a poisonous wasp. Game over.")
