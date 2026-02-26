#!/usr/bin/env python3

import functools
from operator import add, sub, mul, concat


def base_enchantment(power: int, element: str, target: str) -> callable:
    return f"{element} enchantment with power {power} cast on {target}"


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(lambda spell1, spell2:
                                add(spell1, spell2), spells)
    if operation == "multiply":
        return functools.reduce(lambda spell1, spell2:
                                mul(spell1,spell2), spells)
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
    pass


def spell_dispatcher() -> callable:
    pass


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    sum = spell_reducer(spells, "add")
    product = spell_reducer(spells, "multiply")
    max = spell_reducer(spells, "max")
    min = spell_reducer(spells, "min")
    print(f"Sum: {sum}")
    print(f"Product: {product}")
    print(f"Max: {max}")
    print(f"Min: {min}")

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    fire = enchantments['fire_enchant'](target="enemy")
    ice = enchantments['ice_enchant'](target="enemy")
    lightning = enchantments['lightning_enchant'](target="enemy")
    print(fire)
    print(ice)
    print(lightning)

if __name__ == "__main__":
    main()
