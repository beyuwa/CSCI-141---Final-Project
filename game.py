from random import randint

class GameLogic:

    def __init__(ego, console=None):
        ego.console = console

    def relinquish_property(ego, player, cells):

        for i in range(40):
            if cells[i].owner == player:
                cells[i].owner = None

        return cells

    def roll_dice(ego, player, cell_list):
        passGo = False
        num = randint(1,6)
        #num = 3 #MANUAL FIX BECAUSE PYTEST IS RNG WHAT
        # remove player
        
        if player in cell_list[player.position].players:
                (cell_list[player.position].players).remove(player)

        if player.is_bankrupt == False:
            player.position += num
            
        if player.position >= 40:
            passGo == True
            player.position %= 40
            player.money += 200
        
        (cell_list[player.position].players) += [(player)]

        msg = ''
        msg += f'{player.name} rolled a {num} and moved to {cell_list[player.position].name}, which is'
        
        if cell_list[player.position].owner != None:
            msg += f' owned by {(cell_list[player.position].owner).name}.'
        else:
            msg += ' not owned by anyone.'

        if passGo == True:
            msg += '\n'
            msg += f'{player.name} passed Go and collected 200 dollars.'

        print(msg)

    def take_player_action(ego, players, cells, player):    
        ego.move(players, cells, (players[player]))

    def move(ego, people, cells, player):
        GameLogic.roll_dice(ego, player, cells)
        GameLogic.passive_action(ego, people, cells, player)
    
    def passive_action(ego, people, cells, player):
        index = player.position

        if cells[index].type == 'land':
            if cells[index].owner != None: #owned

                player.money += -(cells[index].rent)
                (cells[index].owner).money += (cells[index].rent)
                
            else:
                GameLogic.active_action(ego, people, cells, player)

    def active_action(ego, people, cells, player):
        index = player.position
        choice = (ego.console).get_user_actions('!! do one of these actions', ["Buy Cell", "Do nothing"])
        if choice == 0:
            player.money += -(cells[index].purchase_price)
            cells[index].owner = player
    
    def play_game(ego, players, cells):
        testcounter = 0
        initial = len(players)

        while True:
            (ego.console).render_board(cells)

            #nothing costs any money, so things aren't going to work
            testcounter += 1

            #if testcounter > 3:
                #break

            specialcase = initial

            temproster = players #because my for loops don't like deletion

            for i in range(len(temproster)):
                
                if temproster[i].money <= 0:
                    temproster[i].is_bankrupt = True

            
            for i in range(len(temproster)):

                #print(i)
                #print(f' now {temproster}')
                #print(f' no2 {players}')
                if temproster[i].is_bankrupt == True:    
                    
                
                    cells = ego.relinquish_property(temproster[i], cells) #remove ownership
                    
                    #players.remove(temproster[i]) this is broken af what
                    thirdlist = []
                    for n in range(len(temproster)):
                        if temproster[i] != players[n]:
                            thirdlist += [players[n]]

                    #print(f' was {temproster}')

                    players = thirdlist

            if len(players) <= 1:
                if len(players) == 0:
                    print('No one wins!')
                    break
                else:
                    print(f'{players[0].name} wins!')
                    break

            for n in range(len(players)):
                ego.take_player_action(players, cells, n)

            
        
