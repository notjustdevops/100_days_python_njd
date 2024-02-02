game_level = 3
def create_enemy():
    enemies =["Zombies", "Pirates", "Aliens"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()