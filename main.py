def get_data_from_file(filename):
    with open(filename, 'r') as file:
        width, length = (list(map(int, file.readline().split())))
        input_matrix = []
        for line in file:
            input_matrix.append(line.strip())
    return width, length, input_matrix


def initialise_solution_matrix(width, length):
    solution_matrix = [[0 for _ in range(width)] for _ in range(length)]
    for i in range(1, length - 1):
        solution_matrix[i][width - 1] = None
    solution_matrix[0][width - 1] = 1
    solution_matrix[length - 1][width - 1] = 1
    return solution_matrix


def find_paths_from_plate(solution_matrix, input_matrix,
                          plate, column, width, length):
    paths = None
    if solution_matrix[column][plate + 1] is not None:
        paths = solution_matrix[column][plate + 1]
    for current_column in range(0, length):
        for current_plate in range(plate + 1, width):
            if input_matrix[column][plate] == input_matrix[current_column][current_plate]:
                if current_plate == plate + 1 and current_column == column:
                    continue
                if solution_matrix[current_column][current_plate] is not None:
                    if paths is None:
                        paths = 0
                    paths += solution_matrix[current_column][current_plate]
    solution_matrix[column][plate] = paths


def algorithm(filename):
    width, length, input_matrix = get_data_from_file(filename)
    solution_matrix = initialise_solution_matrix(width, length)
    for current_plate in range(width - 2, -1, -1):
        for current_column in range(length - 1, -1, -1):
            find_paths_from_plate(solution_matrix, input_matrix,
                                  current_plate, current_column,
                                  width, length)
    solution = 0
    for column in range(length):
        if solution_matrix[column][0] is not None:
            solution += solution_matrix[column][0]
    return solution


if __name__ == '__main__':
    from tests import AlgorithmTests
    
    tests = AlgorithmTests()
    tests.testAlgorithm()
