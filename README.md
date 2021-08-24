# tic-tac-toe-bot-pip-package
tic tac toe bot with setting ability
[PyPy:](https://pypi.org/project/tic-tac-toe-api-bot/)

Usage Example
```python
import tic_tac_toe

map = tic_tac_toe.Field(clear_place_sign= '',player_sign='x',bot_sign='o',turn= 'player') #default values (turn is randomed if defaut, posible ['bot','player'])
bot = tic_tac_toe.Bot(map,level=100) #
print(map.is_payer_turn()) #>> True
print(map.get_map()) #>> [['', '', ''], ['', '', ''], ['', '', '']]
print(map.make_move(position = [0,0],skip_check=False,place_anyway=False)) #position = [0-2,0-2],skip_check - if True, skips check for turn, place_anyway - skip check if place free
#>> False # it prints if someone won after that (could be "bot","player","draw" (when no places free and anyone win),False)
print(map.get_map())#>>[['x', '', ''], ['', '', ''], ['', '', '']]
print(map.is_payer_turn())# >> False
print(bot.make_move())# >> False
print(map.get_map())#>> [['x', 'o', ''], ['', '', ''], ['', '', '']]
print(map.is_payer_turn())# >> True
print(map.make_move(position = [0,1],skip_check=False,place_anyway=True)) # False
print(map.get_map())#>> [['x', 'x, ''], ['', '', ''], ['', '', '']]
print(map.is_payer_turn())# >> False
print(map.make_move(position = [0,2],skip_check=True,place_anyway=False)) # player
```
