from Snake_Game import * 
from Feed_Forward_Neural_Network import *

def run_game_with_ml(display, clock, weights):

    steps_per_game = 100 
    prevScore = 0
    snake_start, snake_position, apple_position, score, currDirection = starting_positions()
    W1, W2 = get_weights_from_encoded(weights)
    steps = 0
    length = 3
    collision = False
    
    
    while steps < steps_per_game:
        
        # curr_state = [isLeftOccupied(snake_start, snake_position,currDirection), isFrontOccupied(snake_start, snake_position,currDirection), isRightOccupied(snake_start, snake_position,currDirection), getSinusValue(snake_start, apple_position,currDirection)]
        
        curr_state = [getLeftScaledDistance(snake_start, snake_position,currDirection), getForwardScaledDistance(snake_start, snake_position,currDirection), getRightScaledDistance(snake_start, snake_position,currDirection)] + getFoodDirection(snake_start,apple_position,currDirection)
        # curr_state = [isLeftOccupied(snake_start, snake_position,currDirection), isFrontOccupied(snake_start, snake_position,currDirection), isRightOccupied(snake_start, snake_position,currDirection)] + getFoodDirection(snake_start,apple_position,currDirection)
        
        predicted_button = np.argmax(np.array(forward_propagation(np.array(curr_state), W1, W2)))
        button_direction = predicted_button
        if currDirection=='R':
            if button_direction==0:
                snake_start[1] -= 10
                currDirection = 'U'
            elif button_direction==1:
                snake_start[0] += 10
            else:
                snake_start[1] += 10
                currDirection = 'D'

        elif currDirection=='U':
            if button_direction==0:
                snake_start[0] -= 10
                currDirection = 'L'
            elif button_direction==1:
                snake_start[1] -= 10
            else:
                snake_start[0] += 10
                currDirection = 'R'
        
        elif currDirection=='L':
            if button_direction==0:
                snake_start[1] += 10
                currDirection = 'D'
            elif button_direction==1:
                snake_start[0] -= 10
            else:
                snake_start[1] -= 10
                currDirection = 'U'
        
        else:
            if button_direction==0:
                snake_start[0] += 10
                currDirection = 'R'
            elif button_direction==1:
                snake_start[1] += 10
            else:
                snake_start[0] -= 10
                currDirection = 'L'

        snake_position, apple_position, score = play_game(snake_start, snake_position, apple_position,predicted_button, score, display, clock,currDirection)
        steps += 1
        if prevScore < score:
            steps_per_game += 100
            prevScore = score
            length += 1
        
        if collision_with_boundaries(snake_position[0]) == 1 or collision_with_self(snake_start, snake_position)==1:
            print("collision")
            collision = True
            break

        i=0
        while i<100000:
            i+=1

    if (score < 10) :
        fitness = math.floor(steps *steps * pow(2, (math.floor(score))));
        # if not collision:
        #     fitness -= 1000000000
        return fitness, score
    else :
        fitness =  steps * steps;
        fitness *= pow(2, 10);
        fitness *= (length-9);
        # if not collision:
        #     fitness -= 1000000000
        return fitness, score
    

# sol_per_pop = 10
# num_weights = n_x*n_h + n_h*n_y

# pop_size = (sol_per_pop,num_weights)

# pop = np.random.choice(np.arange(-1,1,step=0.01),size=pop_size,replace=True)
# for i in range(pop.shape[0]):
#     print(run_game_with_ml(display,clock,pop[i]))
