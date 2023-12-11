# -----------------------------------------------
# P.DEC.1
# -----------------------------------------------
# • Užduotis „Tankas“. Sukurti klasę Tankas, kuri:
#   • Tarp metodų turėtų pirmyn(), atgal(), kairėn(), dešinėn(), šūvis(), info()
#     metodus.
#   • Turėtų atributus, kurie:
#     • saugotų tanko koordinates.
#     • saugotų tanko kryptį.
#     • saugotų šūvių skaičių į kiekvieną kryptį.
#   • Leistų tankui judėti per vieną poziciją pirmyn (į Šiaurę), atgal (į
#     Pietus), kairėn (į Vakarus) arba dešinėn (į Rytus). Programos pradžioje
#     tankas atsisukęs į Šiaurę, todėl atspausdintas tekstas „tankas pajuda
#     kairėn“ reikštų, kad jis pasisuko 90 laipsnių ir pajudėjo per vieną
#     poziciją į Vakarus.
#   • Leistų tankui šaudyti tik ta kryptimi, į kurią jis yra atsisukęs.
#   • Iškvietus metodą info(), atspausindtų:
#     • į kurią kryptį tankas šiuo metu yra atsisukęs.
#     • kokios yra tanko koordinatės.
#     • kiek šūvių tankas atliko iš viso.
#     • kiek šūvių tankas atliko į kiekvieną kryptį atskirai.
# • Visas tanko ir informacijos valdymas turi būti atliktas konsolėje (grafinio
#   interfeiso nereikia). Tam reikės sukurti meniu ir priimti vartotojo
#   nurodymus.  Veiksmai (t.y. kviečiami metodai) turi būti atliekami tol, kol
#   vartotojas nesustabdys programos (pvz., pasirinkęs tam tikrą meniu punktą).
#   Grafinio interfeiso programuoti nereikia, tačiau pateikiama iliustracija
#   orientacijai: https://i.imgur.com/YDLBYfx.png
# • Patobulinti programą taip, kad koordinačių sistemoje būtų generuojamas
#   taikinys. Tanko užduotis – atsidurti tinkamoje pozicijoje ir reikiama
#   kryptimi, kad iššovus būtų fiksuojamas pataikymas. Tankui pataikius,
#   konsolėje atsirastų užrašas „pataikei“ ir tuoj pat būtų sugeneruotas naujas
#   taikinys.
# • Sugalvoti taškų sistemą, pvz., pradedama su 100 taškų, už pataikymus galima
#   skirti 50 taškų (pataikyus sumuoti), o už kiekvieną tanko pajudėjimą
#   nubraukti 10 taškų. Pasibaigus taškams, programa parodytų, kiek numušta
#   taikinių, ir pasibaigtų. Taip pat, galima saugoti ir geriausius rezultatus
#   (angl. highest scores) – programai pasibaigus, įvedamas žaidėjo vardas,
#   kuris, kartu su numuštų taikinių skaičiumi, įrašomas tarp geriausių
#   rezultatų. Šiuos rezultatus galima būtų pvz. pažiūrėti su komanda (meniu
#   punktu) „top“.
# • Sugalvoti papildomų programos patobulinimų.
# -----------------------
# English description will be added.
# -----------------------------------------------
import random


class Tank:

    def __init__(self, name):
        self.name = name
        self.direction = 'N'
        self.x = 0
        self.y = 0
        self.shots = {"N": 0, "S": 0, "E": 0, "W": 0}
        self.points = 0
        self.targets_hit = 0
        self.highest_scores = []

    def move_north(self):
        self.direction = "N"
        self.y += 1

    def move_south(self):
        self.direction = "S"
        self.y -= 1

    def move_east(self):
        self.direction = "E"
        self.x += 1

    def move_west(self):
        self.direction = "W"
        self.x -= 1

    def shoot(self):
        self.shots[self.direction] += 1
        if self.direction == "E" and self.x + 1 == enemy_tank.enemy_x and self.y == enemy_tank.enemy_y:
            self.targets_hit += 1
            self.points += 50
            print('Hit!')
            return True
        elif self.direction == "W" and self.x - 1 == enemy_tank.enemy_x and self.y == enemy_tank.enemy_y:
            self.targets_hit += 1
            self.points += 50
            print('Hit!')
            return True
        elif self.direction == "N" and self.x == enemy_tank.enemy_x and self.y + 1 == enemy_tank.enemy_y:
            self.targets_hit += 1
            self.points += 50
            print('Hit!')
            return True
        elif self.direction == "S" and self.x == enemy_tank.enemy_x and self.y - 1 == enemy_tank.enemy_y:
            self.targets_hit += 1
            self.points += 50
            print('Hit!')
            return True
        else:
            self.points -= 50
            print('Miss')
            return False

    def change_direction(self):
        dir_choice = input('Choose your direction N S E W: ')
        if dir_choice == "N":
            self.direction = "N"
            print("Tank is now facing North.")
        elif dir_choice == "S":
            self.direction = "S"
            print("Tank is now facing South.")
        elif dir_choice == "E":
            self.direction = "E"
            print("Tank is now facing East.")
        elif dir_choice == "W":
            self.direction = "W"
            print("Tank is now facing West.")
        else:
            print("Invalid choice. Direction remains unchanged.")

    def info(self):
        print("Current direction:", self.direction)
        enemy_tank.enemy_coordinates()
        print("Tank coordinates: [{}, {}]".format(self.x, self.y))
        print("Total shots fired:", self.shots)
        print("Shots fired in each direction:")
        for direction, count in self.shots.items():
            print(f"{direction}: {count} shots")
        print("Targets hit:", self.targets_hit)
        print("Score:", self.points)


class Target:
    def __init__(self, name):
        self.name = name
        self.enemy_x = random.randint(-10, 10)
        self.enemy_y = random.randint(-10, 10)
        self.coordinates = [self.enemy_x, self.enemy_y]

    def enemy_coordinates(self):
        print(f"{self.name} is at: {self.coordinates}")


if __name__ == "__main__":
    enemy_tank = Target("Target")
    tank_1 = Tank("Panzer")

    while True:
        print("\n--- Tank Actions ---")
        print("1. Move North")
        print("2. Move South")
        print("3. Move East")
        print("4. Move West")
        print("5. Change direction")
        print("6. Shoot")
        print("7. Tank Info")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            tank_1.move_north()
        elif choice == "2":
            tank_1.move_south()
        elif choice == "3":
            tank_1.move_east()
        elif choice == "4":
            tank_1.move_west()
        elif choice == '5':
            tank_1.change_direction()
        elif choice == "6":
            if tank_1.shoot():
                enemy_tank = Target('Enemy')
        elif choice == "7":
            tank_1.info()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
