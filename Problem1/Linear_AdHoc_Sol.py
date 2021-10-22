from typing import List

def is_K_far_from_houses(point: List[int], list_of_houses: List[List[int]], K: int):
    max_distance = 0
    for house in list_of_houses:
        max_distance = max(max_distance, abs(house[0]-point[0])+abs(house[1]-point[1]))
        if max_distance > K:
            return False
    return True


def find_suitable_locations(grid: List[List[int]], K: int):
    """
    :param grid: A 2d array of 0 and 1s where 0 -> empty spot 1-> house
    :param k: max distance from a house
    :return: number of suitable empty spots with distance less than k
    """
    max_x, max_y = [float("-inf")] * 2
    min_x, min_y = [float("inf")] * 2

    list_of_houses = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                list_of_houses.append((x,y))
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                min_x = min(min_x, x)
                min_y = min(min_y, y)

    suitable_locations = 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            # remove the extremeties
            if x < min_x - K or y < min_y - K:
                continue
            if x > max_x + K or y > max_y + K:
                continue
            if grid[x][y] == 0:
                if is_K_far_from_houses((x,y), list_of_houses, K):
                    suitable_locations += 1
    return suitable_locations

# print(find_suitable_locations( [ [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0] ], 4)) #-> 8
# print(find_suitable_locations([ [0, 1], [0, 0] ],1)) #-> 2
print(find_suitable_locations( [ [0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1] ], 2)) #-> 2