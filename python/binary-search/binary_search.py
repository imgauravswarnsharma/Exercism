def find(search_list, value):
    start = 0
    end = len(search_list)-1

    while start<=end:
        mid = (start+end)//2
        if value == search_list[mid]:
            return mid
        elif value > search_list[mid]:
            start = mid+1
        else:
            end = mid-1
    raise ValueError("value not in array")