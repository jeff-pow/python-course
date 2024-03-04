"""
Jeff Powell
9/8/23
CSC295
Program takes an input of points one at a time, groups places them into groups
of three (for three dimensions), and calculates distance between the set of
points. It then formats these distances and prints the max and min to console.
"""
import math


# Function handles reading input in from the console and sorting points into
# the reference point list and all other points
def main():
    list = []
    while True:
        i = input()
        if i == 'q':
            break
        list.append(float(i))
    ref_point = list[0:3]  # First three entries are the reference point
    other_points = list[3:]  # All other entries make up the rest of the points
    previously_found_points = []  # List to hold the points previously seen
    results = [(0, ref_point)]
    # The reference point has a distance of zero from itself
    for i in range(0, len(other_points), 3):
        point2 = other_points[i:i + 3]
        if previously_found_points.__contains__(point2):
            continue
        results.append(distance(ref_point, point2))
        previously_found_points.append(point2)
    output_points(results)


# Function takes in a list with a length of three, and prints it out as a point
# using the format required
def print_point(point):
    print('(', point[0], ', ', point[1], ', ', point[2], ')', sep='')


# The 'results' parameter is a list of tuples containing (distance, point)
# where the distance is a float denoting how far the point is from the
# reference point and the point is a list of three floats.
# The function then prints the required information
def output_points(results):
    print('Reference point: ', end='')
    print_point(results[0][1])
    # Remove the first element (reference point) from the list
    results = results[1:]
    copy = results.copy()
    # Sort the list based on distance
    # (first element of the tuple the list stores)
    copy.sort()
    max_dist = copy[-1][0]
    min_dist = copy[0][0]

    min_list = [p for p in results if p[0] == min_dist]

    max_list = [p for p in results if p[0] == max_dist]

    print(f'Distance to nearest point: {min_dist:.2f}')
    print('Nearest point(s):')
    for p in min_list:
        print_point(p[1])

    print(f'Distance to farthest point: {max_dist:.2f}')
    print('Farthest point(s):')
    for p in max_list:
        print_point(p[1])


# Method calculates the 3d distance between two points in cartesian coordinates
def distance(point1, point2):
    dist = math.sqrt((point2[0] - point1[0]) ** 2 +
                     (point2[1] - point1[1]) ** 2 +
                     (point2[2] - point1[2]) ** 2)
    dist = round(dist, 2)
    return dist, point2


if __name__ == "__main__":
    main()
