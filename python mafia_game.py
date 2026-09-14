import random

def mafia_game():
    print("=" * 50)
    print(" WELCOME TO MAFIA/WEREWOLF GAME ")
    print("=" * 50)
    
    # Step 1: Get number of players
    while True:
        try:
            num_players = int(input("Enter number of players (minimum 6): "))
            if num_players >= 6:
                break
            else:
                print(" Need at least 6 players to start!")
        except ValueError:
            print(" Please enter a valid number!")
    
   
    roles = ['Doctor', 'Mafia', 'Mafia', 'Investigator', 'Citizen', 'Citizen']
    

   
    for _ in range(extra_mafia):
        roles.append('Mafia')
    

    remaining_citizens = num_players - len(roles)
    for _ in range(remaining_citizens):
        roles.append('Citizen')
    
 
    players = []
    print(f"\n Enter {num_players} player names:")
    for i in range(num_players):
        name = input(f"Player {i+1} name: ").strip()
        while name == "":
            print(" Name cannot be empty!")
            name = input(f"Player {i+1} name: ").strip()
        players.append(name)
    

    random.shuffle(roles)
    
    
    player_roles = {}
    for i in range(num_players):
        player_roles[players[i]] = roles[i]
    

    print("\n" + "=" * 50)
    print(" GAME ROLES ASSIGNED! 🎮")
    print("=" * 50)
    
  
    for player, role in player_roles.items():
        print(f"👤 {player}: {role}")
    

    print("\n" + "=" * 50)
    print(" ROLE SUMMARY:")
    print("=" * 50)
    
    mafia_count = list(player_roles.values()).count('Mafia')
    citizen_count = list(player_roles.values()).count('Citizen')
    doctor_count = list(player_roles.values()).count('Doctor')
    investigator_count = list(player_roles.values()).count('Investigator')
    
    print(f" Mafia: {mafia_count}")
    print(f"Doctor: {doctor_count}")
    print(f" Investigator: {investigator_count}")
    print(f" Citizens: {citizen_count}")
    
    print("\n Game is ready to start!")
    print("💡 Remember: Mafia members know each other!")


if __name__ == "__main__":
    mafia_game()