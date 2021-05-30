def first_repeated_element(elements):
    """Returns first repeated element.

    Keyword arguments:
    elements -- list of elements

    """

    repetitive_elements = []
    for element in elements:
        if element in repetitive_elements:
            return element
        else:
            repetitive_elements.append(element)
    else:
        return "Current list haven't repetitive elements"


if __name__ == "__main__":
    print(first_repeated_element(["a", "b", "c", "c", "a"]))
