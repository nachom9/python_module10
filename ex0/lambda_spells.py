#!/usr/bin/env python3


def check_power(mage_power: int, min_power: int):
    if mage_power >= min_power:
        return True
    else:
        return False


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    stats = {
        'max_power': 0,
        'min_power': 0,
        'avg_power': 0
    }
    stats['max_power'] = max(mages, key=lambda x: x['power'])['power']
    stats['min_power'] = min(mages, key=lambda x: x['power'])['power']
    stats['avg_power'] = (
        round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
        )
    return stats


def main():

    artifacts = [
        {'name': 'Water Chalice', 'power': 72, 'type': 'weapon'},
        {'name': 'Earth Shield', 'power': 63, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 92, 'type': 'accessory'},
        {'name': 'Fire Staff', 'power': 66, 'type': 'weapon'}
        ]
    mages = [
        {'name': 'Morgan', 'power': 92, 'element': 'light'},
        {'name': 'Rowan', 'power': 63, 'element': 'ice'},
        {'name': 'Phoenix', 'power': 76, 'element': 'ice'},
        {'name': 'Rowan', 'power': 66, 'element': 'water'},
        {'name': 'Kai', 'power': 57, 'element': 'lightning'}
        ]
    spells = ['heal', 'meteor', 'flash', 'earthquake']

    print("\nTesting artifact sorter...")
    ord_arf = artifact_sorter(artifacts)
    print(f"{ord_arf[0]['name']} ({ord_arf[0]['power']} power) comes before"
          f" {ord_arf[1]['name']} ({ord_arf[1]['power']} power)")

    print("\nTesting spell transformer...")
    spell_names = spell_transformer(spells)
    print(spell_names)


if __name__ == "__main__":
    main()
