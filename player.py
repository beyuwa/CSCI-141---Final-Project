class Player:
    
    def __init__(ego, name, money = 1500, position = 0):
        ego.name = name
        ego.money = money
        ego.position = position
        ego.color = (255, 0, 0)
        ego.is_bankrupt = False

    