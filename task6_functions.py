from data import video_game_sales

def calculate_total_sales(game):
    result = game[6] + game[7] + game[8]
    return result

print(calculate_total_sales(video_game_sales[0]))

def filter_by_genre(data, genre='Platform'):
    filtered_games = []

    for game in data:
        if game[4] == genre:   # Genre is at index 4
            filtered_games.append(game)

    return filtered_games


# Test without specifying a genre (uses default 'Platform')
platform_games = filter_by_genre(video_game_sales)

print(platform_games)


# Test with a specific genre
sports_games = filter_by_genre(video_game_sales, 'Sports')

print(sports_games)


def get_summary(game):
    name = game[1]          # Game name
    year = game[3]          # Release year
    genre = game[4]         # Genre
    global_sales = game[9]  # Global sales

    return f"{name} ({year}) - {genre} - ${global_sales}M"


for game in video_game_sales:
    print(get_summary(game))
