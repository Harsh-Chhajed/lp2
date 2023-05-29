def is_safe(graph, colors, vertex, color):
    # Check if it is safe to color the vertex with the given color

    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False

    return True


def graph_coloring_util(graph, colors, vertex, num_colors):
    # Base case: If all vertices are colored, return True
    if vertex == len(graph):
        return True

    # Recursive case: Try coloring the vertex with each available color
    for color in range(1, num_colors + 1):
        if is_safe(graph, colors, vertex, color):
            colors[vertex] = color

            # Recur to color the remaining vertices
            if graph_coloring_util(graph, colors, vertex + 1, num_colors):
                return True

            # If coloring the vertex doesn't lead to a solution, backtrack and try the next color
            colors[vertex] = 0

    # If no valid coloring found, return False
    return False


def graph_coloring(graph, num_colors):
    # Create a list to store the colors of each vertex
    colors = [0] * len(graph)

    # Call the utility function to solve the problem
    if not graph_coloring_util(graph, colors, 0, num_colors):
        print("No solution exists.")
        return

    # Print the solution
    for vertex, color in enumerate(colors):
        print("Vertex", vertex, "is colored with color", color)


# Example usage: Solve Graph Coloring for a sample graph
sample_graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}
num_colors = 3

graph_coloring(sample_graph, num_colors)
