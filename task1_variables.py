total_games = len(video_game_sales)
print(total_games)

index_to_average = 9
total_global_sales = [row[index_to_average] for row in video_game_sales]
avg_global_sales = sum(total_global_sales) / len(total_global_sales)
print(f"Avg global sales of all video games is {avg_global_sales}.")

top_game_share = (video_game_sales[0][9]/sum(total_global_sales)) * 100
print(top_game_share)
