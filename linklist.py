"""
重点代码，要求自己会写！！！！
思路分析：
    1.创建一个节点类，生成节点对象，包含数据和下一个节点的引用
    2.创建一个链表类，生成链表对象，可以对链表进行数据操作
    3.
"""
print("what's the fuck")


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 链表类
class Linklist:
    """
    建立链表模型
    进行链表操作
    """

    def __init__(self):
        """
        初始化链表，生成一个头节点
        """
        self.head = Node(None)

    # 初始添加一组链表
    def init_list(self, list_):
        self.list_ = list_
        p = self.head
        for i in self.list_:
            p.next = Node(i)
            p = p.next

    # 遍历列表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.data, end='----')
            p = p.next
        print()  # 换行

    # 获取链表长度
    def get_length(self):
        n = 0
        p = self.head
        while p.next is not None:
            n += 1
            p = p.next
        return n

    # 判断链表是否为空
    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入新节点
    def append(self,date):
        node = Node(date)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node

    #选择位置插入节点
    def insert(self,index,data):
        node = Node(data)  #生成节点
        if index<0 or index>self.get_length():
            raise IndexError("索引超出范围")
        p = self.head
        for i in range(index):
            p = p.next
        #插入，先吧后面数据与插入数据链接，防止后边数据丢失，在讲插入数据与前方数据链接
        node.next = p.next
        p.next = node

    #删除节点
    def delete(self,data):
        p = self.head
        while p.next and p.next.data != data:
            p = p.next
        if p.next is None:
            raise ValueError("没有找到数据")
        else:
            p.next = p.next.next

    #获取节点值
    def get_item(self,index):
        if index < 0 or index >= self.get_length():
            raise IndexError("索引超出范围")
        p = self.head.next
        for i in range(index):
            p = p.next
        return p.data




















# 链表对象
link = Linklist()
l = [1, 2, 3, 4, 5]
link.init_list(l)
link.show()
# print(link.get_length())
# print(link.is_empty())
# print(link.clear())
link.append(6)
link.show()
link.insert(4,100)
link.show()
link.delete(100)
link.show()
print(link.get_item(2))



