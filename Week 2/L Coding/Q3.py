def subordinates(lst):
    no_people = 1
    
    def divide_sort(lst):
        nonlocal no_people
        if len(lst) <= 1:
            return lst
        
        if len(lst) == 2:
            return [min(lst), max(lst)]
            
        no_people += 2
        mid = len(lst) // 2
        left = divide_sort(lst[:mid])
        right = divide_sort(lst[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        sorted_list = []
        
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            
            else:
                sorted_list.append(right[j])
                j += 1
        
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list
    
    return (divide_sort(lst), no_people)
    
    
print(subordinates(eval(input())))