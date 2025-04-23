while (1):
  num_of_teams = int(input("Enter the number of teams in the tournament: "))
  if num_of_teams < 2:
    print("The minimum number of teams is 2, try again.")
  else:
    break

team_idx = 0
team_names = [None]*num_of_teams

while (1):

  team_name = input(f"Enter the name for team #{team_idx + 1}")
  team_num_chars, team_num_words = len(team_name), len(team_name.split(" "))
  team_is_correct = False 
  
  while not team_is_correct:
    if not (team_num_words <= 2):
      print("Team names may have at most 2 words, try again.")
      break
    elif not (team_num_chars >= 2):
      print("Team names must have at least 2 characters, try again.")
      break 
    else:
      team_is_correct = True
      break

  if team_is_correct:
    team_names[team_idx] = team_name
    team_idx += 1
    if team_idx >= len(team_names):
      break
  else:
    continue

while (1):
  games_played_by_teach_team = int(input("Enter the number of games played by each team: "))
  if games_played_by_teach_team < len(team_names) - 1:
    print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    continue
  else:
    break

team_idx = 0
team_wins = [0]*len(team_names)

while (1):

  team_win_count = int(input(f"Enter the number of wins Team {team_names[team_idx]} had: "))
  team_win_count_is_correct = False 
  
  while not team_win_count_is_correct:
    if team_win_count < 0:
      print("The minimum number of wins is 0, try again.")
      break
    elif team_win_count > games_played_by_teach_team:
      print(f"The maximum number of wins is {games_played_by_teach_team}, try again.")
      break 
    else:
      team_win_count_is_correct = True
      break

  if team_win_count_is_correct:
    team_wins[team_idx] = team_win_count
    team_idx += 1
    if team_idx >= len(team_names):
      break
  else:
    continue

print("Generating the games to be played in the first round of the tournament...")
team_nested_list = []
for team_idx in range(len(team_names)):
  team_nested_list.append([team_names[team_idx], team_wins[team_idx]])
team_nested_list.sort(key = lambda x : x[1])

start_idx = 0
end_idx = len(team_names) - 1

for _ in range(len(team_names)//2):
  home_team, away_team = team_nested_list[start_idx], team_nested_list[end_idx]
  print(f"Home: {home_team[0]} VS Away: {away_team[0]}")
  start_idx += 1
  end_idx -= 1