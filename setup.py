from setuptools import setup, find_packages


l = """[GitHub:](https://github.com/ruslan-ilesik/tic-tac-toe-bot-pip-package)
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
print(map.check_win()) #player
```"""


setup(name='tic_tac_toe_api_bot',
      version='0.2.7',
      description='simple bot for tic tac toe',
      long_description=l,
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
      ],
      keywords='tic_tac_toe bot api game_api ',
      url='https://github.com/ruslan-ilesik/tic-tac-toe-bot-pip-package',
      author='lesikr',
      license='MIT',
      packages=['tic_tac_toe'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False,
      )
