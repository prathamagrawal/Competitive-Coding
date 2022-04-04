from pydoc import classname
from re import S


class Node:
    def __init__(self,data,name):
        self.data=data
        self.name=name
        self.next=None

class Linkedlist:
    def  __init(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            print(temp.name)
            temp=temp.next

if __name__ == '__main__':
    
    llist=Linkedlist()

    llist.head=Node(2,"A")
    second=Node(30,"B")
    third=Node(40,"C")

    llist.head.next=second;
    second.next=third
    third.next=None

    print(second.data)
    print(third.name)

    llist.printlist()

