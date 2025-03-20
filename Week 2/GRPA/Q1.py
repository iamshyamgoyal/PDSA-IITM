def combinationSort(strList):
    # Sorting L1 manually
    L1 = []
    for char in range(ord('a'), ord('z') + 1):  # Iterate from 'a' to 'z'
        for item in strList:
            if item[0] == chr(char):  # Check if the first character matches
                L1.append(item)

    # Sorting L2 manually
    L2 = []
    current_char = None
    temp_group = []

    for item in L1:
        char, num = item[0], int(item[1:])

        # If a new group starts
        if char != current_char:
            if temp_group:
                # Sort the previous group manually in descending numerical order
                for _ in range(len(temp_group)):
                    max_item = temp_group[0]
                    max_value = int(max_item[1:])
                    for t in temp_group:
                        if int(t[1:]) > max_value:
                            max_item = t
                            max_value = int(t[1:])
                    L2.append(max_item)
                    temp_group.remove(max_item)
            temp_group = [item]  # Start a new group
            current_char = char
        else:
            temp_group.append(item)

    # Process the last group manually
    if temp_group:
        for _ in range(len(temp_group)):
            max_item = temp_group[0]
            max_value = int(max_item[1:])
            for t in temp_group:
                if int(t[1:]) > max_value:
                    max_item = t
                    max_value = int(t[1:])
            L2.append(max_item)
            temp_group.remove(max_item)

    return L1, L2
