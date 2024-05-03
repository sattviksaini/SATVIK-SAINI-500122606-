class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def delete_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return
        print(f"Player {player_name} not found in team {self.name}.")

    def __str__(self):
        return self.name


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def __str__(self):
        return f"Match between {self.home_team} and {self.away_team} is in progress..."


class FootballTeamManagementSystem:
    def __init__(self):
        self.teams = []

    def create_team(self):
        team_name = input("Enter team name: ")
        team = Team(team_name)
        self.teams.append(team)
        print(f"Team {team_name} created.")

    def add_player(self):
        team_name = input("Enter team name: ")
        player_name = input("Enter player name: ")
        player = Player(player_name)
        for team in self.teams:
            if team.name == team_name:
                team.add_player(player)
                print(f"{player_name} added to team {team_name}.")
                return
        print(f"Team {team_name} does not exist.")

    def delete_player(self):
        team_name = input("Enter team name: ")
        player_name = input("Enter player name: ")
        for team in self.teams:
            if team.name == team_name:
                team.delete_player(player_name)
                return
        print(f"Team {team_name} does not exist.")

    def schedule_match(self):
        if len(self.teams) < 2:
            print("You need at least two teams to schedule a match.")
            return

        print("Available Teams:")
        for idx, team in enumerate(self.teams, start=1):
            print(f"{idx}. {team}")

        home_team_idx = int(input("Enter home team number: ")) - 1
        away_team_idx = int(input("Enter away team number: ")) - 1

        home_team = self.teams[home_team_idx]
        away_team = self.teams[away_team_idx]

        match = Match(home_team, away_team)
        print(match)

    def main_menu(self):
        while True:
            print("\nFootball Team Management System")
            print("1. Create a Team")
            print("2. Add Player to a Team")
            print("3. Delete Player from a Team")
            print("4. Schedule Match")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_team()

            elif choice == '2':
                self.add_player()

            elif choice == '3':
                self.delete_player()

            elif choice == '4':
                self.schedule_match()

            elif choice == '5':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = FootballTeamManagementSystem()
    system.main_menu()
