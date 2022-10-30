def last_index_of(head, search_val):
    index = 0
    result = -1
    while head!=None:
        if head.data==search_val:
            result = index
        index += 1
        head = head.next
    return result