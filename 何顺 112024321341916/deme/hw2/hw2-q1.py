# 3.python代码

###链表类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


###删除重复元素
def deleteDuplicates(head):
    # 头节点
    current = head

    # 遍历链表
    while current.next is not None:
        # 如果当前节点的值和下一个相同
        if current.val == current.next.val:
            # 删除下一个节点
            current.next = current.next.next
        else:
            # 继续遍历
            current = current.next

    return head


###将链表转化为数组
def list_to_array(head):
    result = []
    current = head

    # 遍历链表，将节点值添加到数组中
    while current:
        result.append(current.val)
        current = current.next

    return result


### 将数组转化为链表
def array_to_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


### 例
# 首先将数组转化为链表
head = array_to_list([1, 1, 2, 3, 3])
# 然后删除重复元素
head = deleteDuplicates(head)
# 最后将链表转化为数组并输出
print(list_to_array(head))
