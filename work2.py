def print_operation_table(operation, num_rows=6, num_columns=6):
    print("Operation Table:")
    
    header = [" "] + [str(col) for col in range(1, num_columns + 1)]
    print("\t".join(header))
    
    for row in range(1, num_rows + 1):
        row_data = [str(row)]
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            row_data.append(str(result))
        print("\t".join(row_data))

def multiplication(x, y):
    return x * y

print_operation_table(multiplication)