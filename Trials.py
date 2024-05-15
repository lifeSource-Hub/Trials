import sys
import Mutators

GAME_MODE = None

old_new_game = sys.modules["__main__"].PyGameView.new_game

def new_game_redux(self):
    mutators = None
    trial_name = None

    if GAME_MODE is not None:
        mutators = Mutators.all_trials[GAME_MODE].mutators
        trial_name = Mutators.all_trials[GAME_MODE].name
        print(trial_name, mutators)

    old_new_game(self, mutators=mutators, trial_name=trial_name, seed=None)

sys.modules["__main__"].PyGameView.new_game = new_game_redux
