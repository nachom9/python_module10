#!/usr/bin/env python3

def fireball(target: str) -> str:
    return (f"Fireball hits {target}")


def heal(target: str) -> str:
    return (f"Heals {target}")


def base_spell(damage: int, magic_resist: int) -> int:
    if damage - magic_resist < 0:
        return 0
    return damage - magic_resist


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda target: (
        spell1(target),
        spell2(target)
        )


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda dmg, rst: base_spell(dmg, rst) * multiplier


def condition(spell: callable, target: str) -> bool:
    if "hits" in spell(target):
        return True
    return False


def conditional_caster(condition: callable, spell: callable) -> callable:
    return (
        lambda target: spell(target) if condition(spell, target)
        else "Spell fizzled"
        )


def spell_sequence(spells: list[callable]) -> callable:
    return lambda target: list(spell(target) for spell in spells)


def main():
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    comb_res = combined("Dragon")
    print(f"Combined spell result: {comb_res[0]}, {comb_res[1]}")

    print("\nTesting power amplifier...")
    power_amp = power_amplifier(base_spell, 6)
    starting_power = 10
    final_power = power_amp(starting_power, 5)
    print(f"Original: {starting_power}, Amplified: {final_power}")

    print("\nTesting conditional caster...")
    conditional_test = conditional_caster(condition, fireball)
    conditional_result = conditional_test("Goblin")
    print(conditional_result)

    print("\nTesting spell sequence")
    sequence_test = spell_sequence([fireball, heal])
    sequence_result = sequence_test("Goblin")
    print(sequence_result)


if __name__ == "__main__":
    main()
