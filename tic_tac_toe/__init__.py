import random

class Field():
    def __init__(self,clear_place_sign = '',player_sign = 'x',bot_sign = 'o',turn = random.choice(['player','bot']) ):
        self.map = [[clear_place_sign,clear_place_sign,clear_place_sign],[clear_place_sign,clear_place_sign,clear_place_sign],[clear_place_sign,clear_place_sign,clear_place_sign]]
        self.clear_place_sign = clear_place_sign
        self.player_sign = player_sign
        self.bot_sign = bot_sign
        self.turn = turn

        self.combinations = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]

    def get_map(self):
        return self.map
    
    def is_payer_turn(self):
        return self.turn == 'player'

    def make_move(self,position,skip_check = False,place_anyway = False):
        is_all = True
        for i in self.combinations:
            for b in i:
                if self.map[b[0]][b[1]] != self.clear_place_sign:
                    is_all = False
        if is_all:
            return 'draw'

        if skip_check or self.turn == 'player':
            if self.map[position[0]][position[1]] != self.clear_place_sign and not place_anyway:
                raise Exception('Place already taken, if you want to place sign anyway, add `place_anyway` argument with value `True`')
            self.map[position[0]][position[1]] = self.player_sign

        else:
            raise Exception('Not player turn, if you want to make move anyway, add `skip_check` argument with value `True`')

        if not skip_check:        
            self.turn = 'bot'
        return self.check_win()

    def check_win(self):
        for i in self.combinations:
            if self.map[i[0][0]][i[0][1]] != self.clear_place_sign and self.map[i[0][0]][i[0][1]] == self.map[i[1][0]][i[1][1]] == self.map[i[2][0]][i[2][1]]:
                return ('player' if self.map[i[0][0]][i[0][1]] == self.player_sign else 'bot')

        return False

class Bot():
    def __init__(self,field : Field,level = 100):
        if not isinstance(field,Field):
            raise Exception('field should be instance of `Field` class')
        self.field = field
        self.level = 100-level
    
    def make_move(self,skip_check = False):
        def set_new(position):
            self.field.map[position[0]][position[1]] = self.field.bot_sign
            self.field.turn = 'player'
            return self.field.check_win()

        if not skip_check and self.field.turn != 'bot':
            raise Exception('Not bot`s turn. If you want bot to make move anyway, add `skip_check` argument with value `True`')

        is_all = True
        for i in self.field.combinations:
            for b in i:
                if self.field.map[b[0]][b[1]] == self.field.clear_place_sign:
                    is_all = False
        if is_all:
            return 'draw'

        if random.randint(0,100) > self.level:
            # finding place where we win
            for i in self.field.combinations:
                counter = 0
                place = True
                for b in i:
                    if self.field.map[b[0]][b[1]] == self.field.player_sign:
                        place = False
                        break
                    elif self.field.map[b[0]][b[1]] == self.field.clear_place_sign:
                        counter +=1
                    if counter > 1:
                        place = False
                if place:
                    return set_new(b)

            #find places where we will lose if dont place
            for i in self.field.combinations:
                counter = 0
                place = True
                for b in i:
                    if self.field.map[b[0]][b[1]] == self.field.bot_sign:
                        place = False
                        break
                    elif self.field.map[b[0]][b[1]] == self.field.clear_place_sign:
                        counter +=1
                    if counter > 1:
                        place = False
                if place:
                    return set_new(b)
            
        #random position
        positions = []
        for i in self.field.combinations:
            for b in i:
                if self.field.map[b[0]][b[1]] == self.field.clear_place_sign:
                    positions.append(b)
        return set_new(random.choice(positions))