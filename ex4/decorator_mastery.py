#!/usr/bin/env python3

import time
import functools
from typing import Any


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def decorator(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 3)
        print(f"Spell completed in {execution_time} seconds")
        return result
    return decorator


def power_validator(min_power: int) -> callable:
    def decorator(func) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if args[2] < min_power:
                return "Insufficient power for this spell"
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func) -> Any:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempt_count = 0
            try:
                result = func()
            except Exception:
                print(f"Spell failed, retrying... "
                      f"({attempt_count} n/{max_attempts})")
                result = func()
                attempt_count += 1
                if attempt_count >= max_attempts:
                    return "Spell casting failed after max_attempts attempts"
            return result
        return wrapper
    return decorator


class MageGuild:

    def __init__(self, power: int) -> None:
        self.spells_info: dict[str, int] = {}
        self.mage_power: int = power

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        no_spaces = name.replace(' ', '')
        if len(no_spaces) >= 3 and no_spaces.isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


def main() -> None:
    spells = {
        "blizzard": 5,
        "flash": 5,
        "heal": 23,
        "lighning": 13
    }
    mage_guild = MageGuild(30)
    mage_guild.spells_info = spells

    print("\nTesting spell timer...")
    print(f"result: {fireball()}")

    print("\nTesting MageGuild...")
    print(mage_guild.validate_mage_name('Casey'))
    print(mage_guild.validate_mage_name('Jo'))
    for name, power in spells.items():
        print(mage_guild.cast_spell(name, mage_guild.mage_power))
        mage_guild.mage_power -= power


if __name__ == "__main__":
    main()
