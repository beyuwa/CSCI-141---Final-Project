from console import Console, CellRenderer, PlayerRenderer
from player import Player
from game import GameLogic
from board import Cell

def main():
    p = PlayerRenderer()
    c = CellRenderer(p)
    s = Console(c)

    alice = Player('Alice')
    bob = Player('Bob')
    carol = Player('Carol')
    david = Player('David')

    roster = [alice, bob, carol, david]

    num = s.get_user_actions('enter num of players','')

    players = roster[:num+1]

    g = GameLogic(s)

    cells = []
    for i in range(40):
        cells += ['']

    cells[0] = Cell('others', 'go')
    cells[1] = Cell('land','mediterranean avenue','60','2')
    cells[2] = Cell('others','community chest')
    cells[3] = Cell('land','baltic avenue','60','4')
    cells[4] = Cell('others','income tax')
    cells[5] = Cell('land','reading railroad','200','25')
    cells[6] = Cell('land','oriental avenue','100','6')
    cells[7] = Cell('others','chance')
    cells[8] = Cell('land','vermont avenue','100','6')
    cells[9] = Cell('land','connecticut avenue','120','8')
    cells[10] = Cell('others','jail')
    cells[11] = Cell('land','st. charles place','140','10')
    cells[12] = Cell('land','electric company','150','0')
    cells[13] = Cell('land','states avenue','140','10')
    cells[14] = Cell('land','virginia avenue','160','12')
    cells[15] = Cell('land','pennsylvania railroad','200','25')
    cells[16] = Cell('land','st. james place','180','14')
    cells[17] = Cell('others','community chest')
    cells[18] = Cell('land','tennessee avenue','180','14')
    cells[19] = Cell('land','new york avenue','200','16')
    cells[20] = Cell('others','free parking')
    cells[21] = Cell('land','kentucky avenue','220','18')
    cells[22] = Cell('others','chance')
    cells[23] = Cell('land','indiana avenue','220','18')
    cells[24] = Cell('land','illinois avenue','240','20')
    cells[25] = Cell('land','B. & O. railroad','200','25')
    cells[26] = Cell('land','atlantic avenue','260','22')
    cells[27] = Cell('land','ventnor avenue','260','22')
    cells[28] = Cell('land','water works','150','0')
    cells[29] = Cell('land','marvin gardens','280','24')
    cells[30] = Cell('others','go to jail')
    cells[31] = Cell('land','pacific avenue','300','26')
    cells[32] = Cell('land','north carolina avenue','300','26')
    cells[33] = Cell('others','community chest')
    cells[34] = Cell('land','pennsylvania avenue','300','26')
    cells[35] = Cell('land','short line','300','26')
    cells[36] = Cell('others','chance')
    cells[37] = Cell('land','park place','350','35')
    cells[38] = Cell('others','luxury tax')
    cells[39] = Cell('land','boardwalk','400','50')


    g.play_game(players, cells)

    #type, name, purchase_price=0, rent = 0, house_price = 0

    #bash cells
    #wonder what the stdin stuff is

if __name__ == "__main__":
    main()
