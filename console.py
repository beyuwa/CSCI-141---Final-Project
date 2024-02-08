class PlayerRenderer:
    
    def __init__(ego, indent=0):
        ego.indent = indent

    def render_player(ego, player):
        msg = ''

        for i in range(ego.indent):
            msg += '\t' 

        default = f'Player: {player.name}, Money: {player.money}'
        msg += default
        print(msg)

    #duplicate function print(msg) --> return(msg)
    def render_player_returning_msg(ego, player):
        msg = ''

        for i in range(ego.indent):
            msg += '\t' 

        default = f'Player: {player.name}, Money: {player.money}'
        msg += default

        return(msg)

class CellRenderer:
    def __init__(ego, player_renderer, indent=0):
        ego.indent = indent
        ego.player_renderer = player_renderer
        #(ego.player_renderer).indent += 1

    def render_cell(ego, cell):
        msg = ''

        for i in range(ego.indent):
            msg += '\t' 

        default = f'Cell: {cell.name} (land), Price: {cell.purchase_price}'
        default += f', Rent: {cell.rent}, House Price: {cell.house_price}'
        default += f', Color: {cell.color}'

        if cell.owner != None: #adding along the owner name
            default += f', Owner: {(cell.owner).name}'

        msg += default

        second = ''

        if (len(cell.players) > 0) and (cell.name == 'boardwalk'):
            msg += '\n'
            for i in range(len(cell.players)):
                if cell.players[i].is_bankrupt != True:
                    second += ((ego.player_renderer).render_player_returning_msg(cell.players[i]))
                    second += '\n'

        msg += second
        #had to make message before print otherwise unconditional "\n"
        print(msg)

'''
from player import Player
from board import Cell

player = Player("John")
cell = Cell("land", "Park Place")
cell.players = [player]
player_renderer = PlayerRenderer(3)
cell_renderer = CellRenderer(player_renderer, 2)
cell_renderer.render_cell(cell)
'''

class Console:
    
    def __init__(ego, cell_renderer):
        ego.CR = cell_renderer

    def get_user_actions(ego, prompt, actions):
        #pro
        print(prompt)
        for i in range(len(actions)):
            print(f'    {i+1}. {actions[i]}')

        while True:
            inpy = input('Give me some input.')

            #only if its good
            if inpy.isdigit() == True:
                inpy = int(inpy)
                if (inpy <= 4):
                    break
        
        #index of action is inpy - 1
        return(inpy - 1)

    def render_board(ego, cells):
        for i in range(len(cells)):
            (ego.CR).render_cell(cells[i])

