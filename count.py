grid1 = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
"+           +                 +        +     +",
"++ +++++++ ++++++++++++++ ++++++++++++++++++++",
"++ ++    + ++           + ++                 +",
"++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
"++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
"++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
"++ ++   ++ ++             ++          +++ ++e+",
"++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
"++    + ++                   ++              +",
"+++++ + +++++++++++++++++++++++ ++++++++++++ +",
"++ ++ +                   ++          +++ ++ +",
"++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
"++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
"++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
"++                     ++ ++ ++              +",
"+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++++",
"++++++++++++++++++++++++++++++++++++++++++++++",
]

# Counting vertices and edges
vertices = 0
edges = 0

# Iterate through the grid and count vertices and edges
for row in grid1:
    for char in row:
        if char in [' ', 's', 'e']:  # ' ', 's', 'e' are vertices
            vertices += 1
            # Check for edges with adjacent cells
            edges += (row.count(' ') + row.count('s') + row.count('e'))
            if char == ' ':
                if row[row.index(char) - 1] == ' ':
                    edges -= 1  # Adjust for overlapping edges (same edges counted twice)
        if char == ' ':  # Additional edge counting for rows with empty spaces
            edges += (row.count(' ') - 1)

# Divide the total edges by 2 (to account for double-counting each edge)
edges //= 2

print(f"Number of vertices: {vertices}")
print(f"Number of edges: {edges}")
