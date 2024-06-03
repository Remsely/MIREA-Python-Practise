def main(table):
    table = remove_empty_rows(table)
    table = remove_duplicates_rows(table)
    table = remove_duplicates_columns(table)
    table = transform_first_column(table)
    table = transform_second_column(table)
    table = transform_third_column(table)
    table = transform_fourth_column(table)
    table = sorted(table, key=lambda row: row[0])
    return table


def remove_empty_rows(table):
    table = filter(len, map(lambda row: list(filter(bool, row)), table))
    return table


def remove_duplicates_rows(table):
    unique_rows = []
    for row in table:
        if row not in unique_rows:
            unique_rows.append(row)
    return unique_rows


def remove_duplicates_columns(table):
    transposed_table = list(zip(*table))
    transposed_table = remove_duplicates_rows(transposed_table)
    return [list(row) for row in zip(*transposed_table)]


def transform_first_column(table):
    new_table = []
    for row in table:
        first_column_item = row[0]
        parts = first_column_item.split()
        transformed_name = \
            (f'{parts[-1]} '
             f'{" ".join(name[0] + "." for name in parts[:-1])}')
        new_row = [transformed_name] + row[1:]
        new_table.append(new_row)
    return new_table


def transform_second_column(table):
    new_table = []
    for row in table:
        row[1] = f"{int(float(row[1]) * 100)}%"
        new_table.append(row)
    return new_table


def transform_third_column(table):
    new_table = []
    for row in table:
        row[2] = row[2].replace("[at]", "@")
        new_table.append(row)
    return new_table


def transform_fourth_column(table):
    new_table = []
    for row in table:
        flag = int(row[3])
        if (flag == 1):
            row[3] = 'Выполнено'
        elif (flag == 0):
            row[3] = 'Не выполнено'
        new_table.append(row)
    return new_table


input_table_example_1 = [
    ["Э.А. Нубский", "0.1", "nubskij35[at]yahoo.com", "1", "nubskij35[at]yahoo.com"],
    ["С.Т. Чадозский", "0.2", "cadozskij8[at]gmail.com", "1", "cadozskij8[at]gmail.com"],
    [None, None, None, None, None],
    ["С.Т. Чадозский", "0.2", "cadozskij8[at]gmail.com", "1", "cadozskij8[at]gmail.com"],
    ["Г.Р. Саферян", "0.6", "saferan23[at]yahoo.com", "0", "saferan23[at]yahoo.com"],
    ["С.Т. Чадозский", "0.2", "cadozskij8[at]gmail.com", "1", "cadozskij8[at]gmail.com"],
]

transformed_table_example_1 = main(input_table_example_1)
for row in transformed_table_example_1:
    print(row)
