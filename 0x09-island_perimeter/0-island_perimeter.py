def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check the left side of the current cell
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1

                # Check the right side of the current cell
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

                # Check the top side of the current cell
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1

                # Check the bottom side of the current cell
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1

    return perimeter
