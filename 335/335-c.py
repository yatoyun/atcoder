import sys
input = sys.stdin.readline

def new_coordinate(last_coordinate, value):
    if value == "R":
        new_coordinate = (last_coordinate[0]+1, last_coordinate[1])
    elif value == "L":
        new_coordinate = (last_coordinate[0]-1, last_coordinate[1])
    elif value == "U":
        new_coordinate = (last_coordinate[0], last_coordinate[1]+1)
    elif value == "D":
        new_coordinate = (last_coordinate[0], last_coordinate[1]-1)
    return new_coordinate

def main():
    N, Q = map(int, input().split())
    
    coordinates = [(i,0) for i in range(N,0,-1)]
    current_num_movements = 0
    for i in range(Q):
        query, value = input().split()
        query = int(query)
        
        if query == 1:
            coordinates.append(new_coordinate(coordinates[-1], value))
            current_num_movements+=1
        elif query == 2:
            value = int(value)
            p_coordinate = coordinates[N+current_num_movements-value]
            print(p_coordinate[0], p_coordinate[1])

if __name__ == "__main__":
    main()