class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def  __init(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    #Adding data in the front
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insertafter(self,prevnode,data):
        if prevnode is None:
            print("Node not Found")
            return 0
        new_node=Node(data)
        new_node.next=prevnode.next
        prevnode.next=new_node

if __name__ == '__main__':
    
    llist=Linkedlist()

    llist.head=Node(2)
    second=Node(30)
    third=Node(40)

    llist.head.next=second;
    second.next=third
    third.next=None

    llist.printlist()

    print("Adding in front: \n")
    llist.push(10)

    llist.printlist()

    print("\nAdding in Between: \n")
    llist.insertafter(second,90)
    llist.printlist()

