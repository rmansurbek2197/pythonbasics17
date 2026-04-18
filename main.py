def remove_duplicates(input_list):
    output_list = []
    for element in input_list:
        if element not in output_list:
            output_list.append(element)
    return output_list

def main():
    input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
    print("Original list: ", input_list)
    output_list = remove_duplicates(input_list)
    print("List after removing duplicates: ", output_list)

main()