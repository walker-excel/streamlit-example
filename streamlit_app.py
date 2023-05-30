import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

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
            return int(healing_amount)
        else:
            damage_amount = self.calculate_damage(move, defender)
            defender.health -= damage_amount
            return int(damage_amount)


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
    creature1 = Creature(10, 100, 20, 30, 15, 10, 5, 50)
    creature2 = Creature(8, 80, 15, 25, 12, 8, 3, 60)

    st.title("Test Battle")

    col1, col2 = st.columns(2)

    # Initialize attack_outputs list if not already present in session_state
    if "attack_outputs" not in st.session_state:
        st.session_state.attack_outputs = []

    with col1:
        st.header("Creature 1")
        if st.button(f"{move1.name}"):
            output = attack_one(creature1, creature2, move1)
            st.session_state.attack_outputs.append(output)
            check_win_condition(creature1, creature2)
        if st.button(f"{move2.name}"):
            output = attack_two(creature1, creature2, move2)
            st.session_state.attack_outputs.append(output)
            check_win_condition(creature1, creature2)
        if st.button(f"{move3.name}"):
            output = attack_three(creature1, creature2, move3)
            st.session_state.attack_outputs.append(output)
            check_win_condition(creature1, creature2)

    with col2:
        st.header("Creature 2")
        if st.button(f"{move4.name}"):
            output = attack_four(creature1, creature2, move4)
            st.session_state.attack_outputs.append(output)
            check_win_condition(creature1, creature2)
        if st.button(f"{move5.name}"):
            output = attack_five(creature1, creature2, move5)
            st.session_state.attack_outputs.append(output)
            check_win_condition(creature1, creature2)
        if st.button(f"{move6.name}"):
            output = attack_six(creature1, creature2, move6)
            st.session_state.attack_outputs.append(output)
            check_win_condition(creature1, creature2)

    st.write("Attack Logs:")
    for output in st.session_state.attack_outputs:
        st.write(output)


def attack_one(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 1 dealt {damage} damage to Creature 2. Creature 2 now has {defender.health} HP."


def attack_two(attacker, defender, move):
    healing = attacker.attack(move, defender)
    return f"Creature 1 healed for {healing} HP. Creature 1 now has {attacker.health} HP."


def attack_three(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 1 dealt {damage} damage to Creature 2. Creature 2 now has {defender.health} HP."


def attack_four(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 2 dealt {damage} damage to Creature 1. Creature 1 now has {defender.health} HP."


def attack_five(attacker, defender, move):
    healing = attacker.attack(move, defender)
    return f"Creature 2 healed for {healing} HP. Creature 2 now has {attacker.health} HP."


def attack_six(attacker, defender, move):
    damage = attacker.attack(move, defender)
    return f"Creature 2 dealt {damage} damage to Creature 1. Creature 1 now has {defender.health} HP."


def check_win_condition(creature1, creature2):
    if creature1.health <= 0:
        st.session_state.attack_outputs.append("Creature 1 has 0 HP. Creature 2 Wins!")
    elif creature2.health <= 0:
        st.session_state.attack_outputs.append("Creature 2 has 0 HP. Creature 1 Wins!")


if __name__ == "__main__":
    main()
