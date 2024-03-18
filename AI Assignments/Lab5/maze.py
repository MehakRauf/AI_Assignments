def is_valid_move(maze, visited, row, col):
    #checking all the conditions
    if row >= 0 and row < len(maze) and col >= 0 and col < len(maze[0]) and maze[row][col] != '#' and not visited[row][col]:
        return True
    return False

def solve_maze(maze, visited, row, col, end_row, end_col):
    if row == end_row and col == end_col:
        return True

    #marking the start as visited
    visited[row][col] = True
    #the robot can down and right
    directions = [(1,0), (0,1)]
    
    for d in directions:
        new_row = row + d[0]
        new_col = col + d[1]

        if is_valid_move(maze, visited, new_row, new_col):
            if solve_maze(maze, visited, new_row, new_col, end_row, end_col):
                return True

    return False

def main():
    maze = [
        ['.', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '#', '.', '#'],
        ['#', '#', '#', '.', '#', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.'],
        ['#', '#', '#', '#', '.', '#', '.', '#', '#', '#'],
        ['#', '.', '.', '#', '.', '#', '.', '#', '.', '#'],
        ['#', '#', '.', '#', '.', '#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    visited = [[False for _ in row] for row in maze]

    start_row=int (input("Enter the start row: "))
    start_col = int (input("Enter the start column: "))
    end_row= int (input("Enter the end row: "))
    end_col = int (input("Enter the end column: "))
    #if it is true means path exists
    if solve_maze(maze, visited, start_row, start_col, end_row, end_col):
        print("The maze has a path to the end.")
    #if no path
    else:
        print("There is no path in the maze.")

if __name__ == "__main__":
    main()
