"""
This program is a modification based on work created and shared by Google (https://developers.google.com/readme/policies) and used according to terms described in the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0).
The original code can be found in https://developers.google.com/optimization/routing/tsp
"""

import math
from random import random
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from matplotlib.path import Path
from matplotlib import patches
import matplotlib.pyplot as plt


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Locations in block units
    data['locations'] = [(random()*100, random()*100) for i in range(100)]
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Euclidean distance
                distances[from_counter][to_counter] = (int(
                    math.hypot((from_node[0] - to_node[0]),
                               (from_node[1] - to_node[1]))))
    return distances


def print_solution(manager, routing, solution, locations):
    """Plots solution on the xy plane."""
    """Modified from the original code."""
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    vertices = []
    while not routing.IsEnd(index):
        vertices.append(locations[manager.IndexToNode(index)])
        previous_index = index
        index = solution.Value(routing.NextVar(index))
    fig, ax = plt.subplots()
    x, y = zip(*vertices)
    line, = ax.plot(x, y, 'bo-')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    plt.show()


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = compute_euclidean_distance_matrix(data['locations'])

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution, data['locations'])


if __name__ == '__main__':
    main()
