def search_element(my_list, element_to_search):
    if element_to_search in my_list:
        return f"{element_to_search} is present in the list at index {my_list.index(element_to_search)}."
    else:
        return f"{element_to_search} is not present in the list."

my_list = input("Enter the elements of the list separated by space: ").split()

element_to_search = input("Enter the element to search: ")

result = search_element(my_list, element_to_search)
print(result)
