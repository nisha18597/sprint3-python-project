from data import video_game_sales

for game in video_game_sales:
    if game[9] > 25:
     print(game[1] , game[9])


pre_2000_count = 0

for game in video_game_sales:
    if game[3] < 2000:
     pre_2000_count = pre_2000_count + 1
    
    
print(pre_2000_count)


total_na = 0
total_jp = 0


for game in video_game_sales:
    total_na = total_na + game[NA_SALES]
    total_jp = total_jp + game[JP_SALES]


print("Total North America Sales:", total_na)
print("Total Japan Sales:", total_jp)

if total_na > total_jp:
    print("North America had higher sales.")
elif total_jp > total_na:
    print("Japan had higher sales.")
else:
    print("Both regions had equal sales.")

nintendo_games = []
for game in video_game_sales:
    if game[5] == 'Nintendo':
     nintendo_games. append(game[1])

print(nintendo_games)
