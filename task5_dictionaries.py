from data import video_game_sales

sales_by_genre = {}

for game in video_game_sales:
    genre = game[4]
    global_sales = game[9]

    if genre in sales_by_genre:
        sales_by_genre[genre] = sales_by_genre[genre] + global_sales
    else:
        sales_by_genre[genre] = global_sales

print(sales_by_genre)

games_per_publisher = {}

for game in video_game_sales:
    PUBLISHER = game[5]

    if PUBLISHER in games_per_publisher:
        games_per_publisher[PUBLISHER] = games_per_publisher[PUBLISHER] + 1

    else:
      games_per_publisher[PUBLISHER] = 1

print(games_per_publisher)

top_game = {
    "name": video_game_sales[0][1],
    "year": video_game_sales[0][3],
    "genre": video_game_sales[0][4],
    "publisher": video_game_sales[0][5],
    "global_sales": video_game_sales[0][9]
}

for key, value in top_game.items():
    print(key, ":", value)
