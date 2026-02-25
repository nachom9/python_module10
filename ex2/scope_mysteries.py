#!/usr/bin/env python3

from typing import Any


def mage_counter() -> callable:
    counter = 0

    def count_calls() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count_calls


def spell_accumulator(initial_power: int) -> callable:
    actual_power = initial_power

    def add_power(power: int) -> int:
        nonlocal actual_power
        actual_power += power
        return actual_power
    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda item: f"{enchantment_type} {item}"


def memory_vault() -> dict[str, callable]:
    default_dict = {}

    def store(key: str, value: Any) -> None:
        default_dict[key] = value

    def recall(key: str) -> Any:
        return default_dict.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main():
    print("\nTesting mage counter...")
    count_calls = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {count_calls()}")

    print("\nTesting spell accumulator...")
    add_power = spell_accumulator(2)
    print(f"Actual power: {add_power(4)}")
    print(f"Actual power: {add_power(11)}")
    print(f"Actual power: {add_power(3)}")

    print("\nTesting enchantment factory...")
    flame_item = enchantment_factory('Flaming')
    froze_item = enchantment_factory('Frozen')
    fire_item = flame_item('Sword')
    ice_item = froze_item('Shield')
    print(fire_item)
    print(ice_item)

    print("\nTesting memory vault")
    funcs = memory_vault()
    invalid_result = funcs['recall']("name")
    print(invalid_result)
    funcs['store']("name", "nacho")
    valid_result = funcs['recall']("name")
    print(valid_result)


if __name__ == "__main__":
    main()
