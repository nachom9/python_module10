#!/usr/bin/env python3

import functools
from operator import add, mul


def base_enchantment(power: int, element: str, target: str) -> callable:
    return f"{element} enchantment with power {power} cast on {target}"


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(lambda spell1, spell2:
                                add(spell1, spell2), spells)
    if operation == "multiply":
        return functools.reduce(lambda spell1, spell2:
                                mul(spell1, spell2), spells)
    if operation == "max":
        return max(spells)
    if operation == "min":
        return min(spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment,
                                          power=50, element="fire"),
        "ice_enchant": functools.partial(base_enchantment,
                                         power=50, element="ice"),
        "lightning_enchant": functools.partial(base_enchantment,
                                               power=50, element="lightning")
        }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatcher() -> str:
        return "Unknown spell"

    @dispatcher.register
    def damage_spell(spell_damage: int) -> str:
        return f"Spell does {spell_damage} damage"

    @dispatcher.register
    def enchantment(enchantment: str) -> str:
        return f"Enchantment: {enchantment}"

    @dispatcher.register
    def multi_cast(spells: list) -> str:
        return f"Spells: {spells}"

    return dispatcher


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    sum_spells = spell_reducer(spells, "add")
    product = spell_reducer(spells, "multiply")
    max_spell = spell_reducer(spells, "max")
    min_spell = spell_reducer(spells, "min")
    print(f"Sum: {sum_spells}")
    print(f"Product: {product}")
    print(f"Max: {max_spell}")
    print(f"Min: {min_spell}")

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    fire = enchantments['fire_enchant'](target="enemy")
    ice = enchantments['ice_enchant'](target="enemy")
    lightning = enchantments['lightning_enchant'](target="enemy")
    print(fire)
    print(ice)
    print(lightning)

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher")
    dispatcher = spell_dispatcher()
    spell = dispatcher(90)
    enchantment = dispatcher("dark fire")
    spells = dispatcher(["fireball", "ice_shield", "heal"])
    print(spell)
    print(enchantment)
    print(spells)


if __name__ == "__main__":
    main()
