'''formulates the pascal triangle'''


def pascal_triangle(n):
    '''
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        List of lists of integers representing Pascal’s triangle
    '''
    comb_lis = []
    if n == 0:
        return "you need it to be ";
    for i in range(n):
        comb_lis.append([])
        comb_lis[i].append(1)
        if (i > 0):
            for j in range(1, i):
                comb_lis[i].append(comb_lis[i - 1][j - 1] + comb_lis[i - 1][j])
            comb_lis[i].append(1)
    return comb_lis
"""
def print_triangle(triangle):
    comment
    Print the triangle
    comment
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(10))*"""