from Snake_Game import * 


def run_game(display, clock):
    max_score = 0
    avg_score = 0
    test_games = 1
    score = 0
    steps_per_game = 50
    

    for _ in range(test_games):
        snake_start, snake_position, apple_position, score = starting_positions()

        

        for _ in range(steps_per_game):
            
            button = int(input())
            if collision_with_boundaries(snake_position[0]) == 1 or collision_with_self(snake_start,
                                                                                        snake_position) == 1:
                print("collision")
                break

            else:
                score += 0

            snake_position, apple_position, score = play_game(snake_start, snake_position, apple_position,
                                                              button, score, display, clock)

            if score > max_score:
                max_score = score

            print(score)
            if score == -1:
                break

run_game(display, clock)