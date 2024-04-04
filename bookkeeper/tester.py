items = [[1,2,3], [4,5,6], [7,8,9]]

def get_by_value_at_pos(items, value, pos ):
    idx = items.index(lambda x: x[pos] == value)
    return idx
def is_value_at_pos(a, value, pos):
    return a[pos] == value

def index_of_first(lst, pred, *args):
    print(*args)
    for i, v in enumerate(lst):
        if pred(v,  *args):
            return i
    return None

print(index_of_first(items, is_value_at_pos, 6, 2))