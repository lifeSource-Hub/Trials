import sys
import Mutators

GAME_MODE = None

old_new_game = sys.modules["__main__"].PyGameView.new_game

def new_game_redux(self):
    mutators = None
    trial_name = None

    if isinstance(GAME_MODE, int) and (0 <= GAME_MODE < len(Mutators.all_trials)):
        mutators = Mutators.all_trials[GAME_MODE].mutators
        trial_name = Mutators.all_trials[GAME_MODE].name
        print("Starting", trial_name, "trial")

    old_new_game(self, mutators=mutators, trial_name=trial_name, seed=None)

sys.modules["__main__"].PyGameView.new_game = new_game_redux
