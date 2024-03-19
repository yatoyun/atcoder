import sys
input = sys.stdin.readline

def rotate_direction(direction):
    if direction == [0,1]:
        return [1,0]
    elif direction == [1,0]:
        return [0,-1]
    elif direction == [0,-1]:
        return [-1,0]
    elif direction == [-1,0]:
        return [0,1]

def check_next_node(next_node, output_grid):
    if next_node[0]<0 or next_node[0]>=len(output_grid) or next_node[1]<0 or next_node[1]>=len(output_grid[0]):
        return False
    if output_grid[next_node[0]][next_node[1]]!="":
        return False
    return True

def get_next_node(current_node, direction):
    return [current_node[0]+direction[0], current_node[1]+direction[1]]

def main():
    N = int(input())
    
    output_grid = [[""]*N for _ in range(N)]
    output_grid[int(N/2)][int(N/2)] = "T"
    
    direction = [0,1] # +x
    current_node = [0,0]
    current_number = 1
    
    while current_number<N*N:
        output_grid[current_node[0]][current_node[1]] = str(current_number)
        next_node = get_next_node(current_node, direction)
        if not check_next_node(next_node, output_grid):
            direction = rotate_direction(direction)
        current_number += 1
        current_node = get_next_node(current_node, direction)
    
    for i in range(N):
        for j in range(N):
            print(output_grid[i][j], end=" ")
        print()
    

if __name__ == "__main__":
    main()