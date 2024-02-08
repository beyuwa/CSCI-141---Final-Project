class Cell:
    
    def __init__(ego, type, name, purchase_price=0, rent = 0, house_price = 0, color = None, owner = None, players = []):
        ego.name = name
        ego.type = type
        ego.purchase_price = int(purchase_price)
        ego.rent = int(rent)
        ego.house_price = house_price
        ego.color = color
        ego.owner = owner
        ego.players = players
            
            
            

