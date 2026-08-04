game_names = []
for game in video_game_sales:
   game_names.append(game[1]) 

print(game_names)

new_game = [21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18]
video_game_sales.append(new_game)
print(len(video_game_sales))

number_of_games = 21
number_of_columns = 10
name_of_the_dataset = 'Video Game Sales'
dataset_info = (number_of_games, number_of_columns, name_of_the_dataset)
print(dataset_info)
