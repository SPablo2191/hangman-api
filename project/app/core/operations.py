from enum import Enum

class Operations(str, Enum):
    start_new_game = "/new"
    show_instrucctions="/instructions"
    get_help="/help"
    make_a_guess="/guess"
