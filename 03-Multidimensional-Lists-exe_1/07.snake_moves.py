def print_func(rows_, cols, full_snake_length_):
    snake_print = ''
    remaining_snake = full_snake_length_
    for i in range(rows):
        snake_print = remaining_snake[:cols]
        remaining_snake = remaining_snake[cols:]
        if i % 2 != 0:
            snake_print = snake_print[::-1]
        print(snake_print)


rows, columns = map(int, input().split())
snake = input()

full_length = rows * columns
whole_snake_in_matrix = full_length // len(snake)
remaining_snake_in_matrix = full_length - (whole_snake_in_matrix * len(snake))
full_snake_length = snake * whole_snake_in_matrix + snake[:remaining_snake_in_matrix]

print_func(rows, columns, full_snake_length)
