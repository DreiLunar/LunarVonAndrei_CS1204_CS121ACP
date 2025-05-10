from abc import ABC, abstractmethod

class AbstractWeapon(ABC):
    def __init__(self, name, level, damage, damage_type, range, durability, origin, age):
        self.name = name
        self.level = level
        self.damage = damage
        self.damage_type = damage_type
        self.range = range
        self.durability = durability
        self.origin = origin
        self.age = age

    @abstractmethod
    def special_attack(self):
        pass


class Weapon(AbstractWeapon):
    def __init__(self, name, level, damage, damage_type, range, durability, origin, age, has_special_attack=False):
        super().__init__(name, level, damage, damage_type, range, durability, origin, age)
        self.has_special_attack = has_special_attack

    def display_stats(self):
        print(f"\n{self.name} Stats:")
        print(f"Level: {self.level}")
        print(f"Damage: {self.damage}")
        print(f"Damage Type: {self.damage_type}")
        print(f"Range: {self.range}")
        print(f"Durability: {self.durability}/100")

    def use_weapon(self):
        if self.durability <= 0:
            print(f"{self.name} is broken and cannot be used!")
            return False

        self.durability -= 10
        print(f"{self.name} was used, dealing {self.damage} damage! Remaining durability: {self.durability}/100")
        return True

    def special_attack(self):
        if not self.has_special_attack:
            print(f"{self.name} has no special attack.")
        else:
            if self.name == "Doughdil":
                print(f"{self.name} charms the enemy, lowering their defenses!")
            elif self.name == "Wand":
                print(f"{self.name} fires a bolt of blue lightning!")
            elif self.name == "Pope's Staff":
                print(f"{self.name} unleashes divine power, disintegrating every enemy target!")
            elif self.name == "Tome":
                print(f"{self.name} creates a magic circle, healing all allies in a wide-range area!")

class WeaponManager:
    def __init__(self):
        self.sword_weapons = {
            "1": Weapon("Dagger", 65, 45, "Physical", "Melee", 100, "Reality", "Medieval",),
            "2": Weapon("Doughdil", 96, 69, "Physical", "Melee", 100, "Fantasy", "Modern", has_special_attack=True),
            "3": Weapon("Zweihander", 80, 95, "Physical", "Close", 100, "Reality", "Medieval Germany",)
        }

        self.marksman_weapons = {
            "1": Weapon("Short Bow", 70, 60, "Physical", "Medium", 100, "Reality", "Paleolithic Era",),
            "2": Weapon("Long Bow", 66, 110, "Physical", "Long", 100, "Reality", "Neolithic Era",),
            "3": Weapon("Crossbow", 69, 75, "Physical", "Long", 100, "Reality", "400 BCE",)
        }

        self.caster_weapons = {
            "1": Weapon("Wand", 75, 123, "Magic", "Medium", 100, "Fantasy", "Arcane Era", has_special_attack=True),
            "2": Weapon("Pope's Staff", 999, 999, "Holy Magic", "Global", 100, "Fantasy", "Great Holy Era", has_special_attack=True),
            "3": Weapon("Tome", 100, 130, "Invocation", "Long", 100, "Fantasy", "Verdant Epoch", has_special_attack=True)
        }

        self.ranger_weapons = {
            "1": Weapon("AWM Sniper", 80, 230, "Physical", "Extreme", 100, "Reality", "Modern Era"),
            "2": Weapon("M4A1 Rifle", 73, 120, "Physical", "Long", 100, "Reality", "Modern Era"),
            "3": Weapon("Desert Eagle", 65, 50, "Physical", "Close", 100, "Modern", "Contemporary")
        }

        self.weapon_types = {
            "1": ("Sword", self.sword_weapons),
            "2": ("Marksman", self.marksman_weapons),
            "3": ("Caster", self.caster_weapons),
            "4": ("Ranger", self.ranger_weapons)
        }

    def show_weapon_types(self):
        print("Select weapon class:")
        for key, (name, _) in self.weapon_types.items():
            print(f"{key}. {name}")

    def show_weapons(self, type_choice):
        if type_choice not in self.weapon_types:
            print("Invalid weapon type selection.")
            return None

        type_name, weapons = self.weapon_types[type_choice]
        print(f"\nSelect {type_name} weapon:")
        for key, weapon in weapons.items():
            print(f"{key}. {weapon.name}")

        weapon_choice = input("Enter your choice: ")
        if weapon_choice not in weapons:
            print("Invalid weapon selection.")
            return None

        return weapons[weapon_choice]


def main():
    manager = WeaponManager()

    while True:
        manager.show_weapon_types()
        type_choice = input("Enter your choice (or 'q' to quit): ")

        if type_choice.lower() == 'q':
            break

        weapon = manager.show_weapons(type_choice)
        if weapon:
            weapon.display_stats()
            use_choice = input("\nDo you want to use this weapon? (Y/N): ")
            if use_choice.upper() == 'Y':
                weapon.use_weapon()

            if weapon.has_special_attack:
                special_choice = input("\nDo you want to use the special attack? (Y/N): ")
                if special_choice.upper() == 'Y':
                    weapon.special_attack()

        print("\n" + "-" * 40 + "\n")


if __name__ == "__main__":
    main()
