from game_bot import GameCog

# For each new GameCog, import the class here
from bot_functions.maths_game import MathsGame
from bot_functions.other_games import OtherGames

# Add the new game classes onto the end of this list
class Games(GameCog, MathsGame, OtherGames):
  game_command_prefix = '!'
  pass

def setup(client):
  client.add_cog(Games(client))

