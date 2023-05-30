import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

import streamlit as st


class Creature:
    def __init__(self, level, health, physical_attack, magic_attack, armor, magic_resistance, faith, speed):
        self.level = level
        self.health = health
        self.physical_attack = physical_attack
        self.magic_attack = magic_attack
        self.armor = armor
        self.magic_resistance = magic_resistance
        self.faith = faith
        self.speed = speed

    def calculate_damage(self, move, defender):
        attack_stat = self.physical_attack if move.type == MoveType.Physical else self.magic_attack
        defense_stat = defender.armor if move.type == MoveType.Physical else defender.magic_resistance
        damage = move.power * (attack_stat / defense_stat) * (self.level / defender.level) + 2
        return int(damage)

    def calculate_healing(self, move):
        healing = (move.power * self.faith) / ((self.level / 3.0) + 1)
        return int(healing)

    def attack(self, move, defender):
        if move.is_healing_move:
            healing_amount = self.calculate_healing(move)
            self.health += healing_amount
            st.write(f"Creature healed for {healing_amount} health.")
        else:
            damage_amount = self.calculate_damage(move, defender)
            defender.health -= damage_amount
            st.write(f"Creature dealt {damage_amount} damage to the opponent.")


class Move:
    def __init__(self, name, power, move_type, is_healing_move):
        self.name = name
        self.power = power
        self.type = move_type
        self.is_healing_move = is_healing_move


class MoveType:
    Physical = 1
    Magic = 2

move1 = Move("Fireball", 40, MoveType.Magic, False) # Define move1
move2 = Move("Heal", 30, MoveType.Magic, True) # Define move2
move3 = Move("Tackle", 20, MoveType.Physical, False) # Define move3
move4 = Move("Firebolt", 40, MoveType.Magic, False)  # Define move4
move5 = Move("Cure", 30, MoveType.Magic, True) # Define move5
move6 = Move("Rush", 20, MoveType.Physical, False) # Define move6

def main():
    global creature1, creature2, counter  # Declare variables as global

    creature1 = Creature(10, 100, 20, 30, 15, 10, 5, 50)
    creature2 = Creature(8, 80, 15, 25, 12, 8, 3, 60)

    counter = 0

    faster_creature = creature1 if creature1.speed > creature2.speed else creature2
    slower_creature = creature2 if faster_creature == creature1 else creature1

    st.title("Test Battle")

    global col1, col2
    col1, col2 = st.columns(2)

    with col1:
        st.header("Creature 1")
        st.button(f"{move1.name}", on_click=attack_one)
        st.button(f"{move2.name}", on_click=attack_two)
        st.button(f"{move3.name}", on_click=attack_three)

    with col2:
        st.header("Creature 2")
        st.button(f"{move4.name}", on_click=attack_four)
        st.button(f"{move5.name}", on_click=attack_five)
        st.button(f"{move6.name}", on_click=attack_six)

    notfication()

    if creature1.speed > creature2.speed:
        col1.write("Faster")
        col2.write("Slower")
    else:
        col2.write("Faster")
        col1.write("Slower")

def attack_one():
    global counter  # Declare counter as a global variable
    # Action to be performed when the button is clicked
    creature1.attack(move1, creature2)
    counter += 1  # Add 1 to counter

    notfication()
    c_turn_one()
    re_calculate()
    v_notification()


def attack_two():
    global counter  # Declare counter as a global variable
    # Action to be performed when the button is clicked
    creature1.attack(move2, creature2)
    counter += 1  # Add 1 to counter

    notfication()
    c_turn_one()
    re_calculate()
    v_notification()


def attack_three():
    global counter  # Declare counter as a global variable
    # Action to be performed when the button is clicked
    creature1.attack(move3, creature2)
    counter += 1  # Add 1 to counter

    notfication()
    c_turn_one()
    re_calculate()
    v_notification()


def attack_four():
    global counter  # Declare counter as a global variable
    # Action to be performed when the button is clicked
    creature2.attack(move4, creature1)
    counter += 1  # Add 1 to counter

    notfication()
    c_turn_two()
    re_calculate()
    v_notification()


def attack_five():
    global counter  # Declare counter as a global variable
    # Action to be performed when the button is clicked
    creature2.attack(move5, creature1)
    counter += 1  # Add 1 to counter

    notfication()
    c_turn_two()
    re_calculate()
    v_notification()


def attack_six():
    global counter  # Declare counter as a global variable
    # Action to be performed when the button is clicked
    creature2.attack(move6, creature1)
    counter += 1  # Add 1 to counter

    notfication()
    c_turn_two()
    re_calculate()
    v_notification()

def notfication():
    col1.write(f"Creature 1 Health: {creature1.health}")
    col2.write(f"Creature 2 Health: {creature2.health}")

def v_notification():

    if creature1.health <= 0:
        col1.write("Victory!")
        col2.write("Defeat...")
    elif creature2.health <= 0:
        col2.write("Defeat...")
        col1.write("Victory")

def c_turn_one():
    col1.write("Opponent's Turn...")
    col2.write("Your Turn...")

def c_turn_two():
    col1.write("Your Turn...")
    col2.write("Opponent's Turn...")


def re_calculate():
    global counter  # Declare counter as a global variable
    if counter == 2:
        if creature1.speed > creature2.speed:
            col1.write("Choose an attack creature 1")
            col2.write("Waiting on Creature 1...")
            counter = 0
        else:
            col2.write("\nChoose an attack creature 2")
            col1.write("\nWaiting on Creature 2...")
            counter = 0

if __name__ == "__main__":
    main()
