from creature import Creature

# initialize game variables
game_over = False
hero = Creature()
enemy = Creature()

# main game loop
while not game_over:
    print("Hero's health: " + str(hero.get_health()))
    print("Monster's health: " + str(enemy.get_health()))

    choice = input("What do you want to do? ")

    # deal damage to the enemy
    if choice == "attack":
        enemy.deal_damage(40)
        if not enemy.is_alive():  # determine if the game is over
            game_over = True
            continue  # go back to beggining of loop
        
    # deal damage to the hero
    hero.deal_damage(20)
    if not hero.is_alive():
        game_over = True
