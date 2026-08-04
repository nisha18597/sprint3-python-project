messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

game_name = video_game_sales[4][1]
print(game_name[:7])

messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']

for name in messy_names:
    print(name.strip().lower())


print(f"#1 Best Seller: Wii Sports (2006) - $82.74M global sales")
