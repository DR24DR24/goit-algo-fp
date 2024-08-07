import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next
        print()

    def compare_list(self,ref):
        current=self.head
        i=0
        len_ref=len(ref)
        while current and len_ref>i:
            if ref[i]<=current.data:
                return False
            i+=1
            current=current.next
        if len(ref)!=i or (current is not None):
            return False
        return True
    
    def linkedList2list(self):
        current = self.head
        l=[]
        while current:
            l.append(current.data)
            current = current.next
        return l
    
    def llist_merging(self,ll:Node):
        virtual_node1=Node(None)
        virtual_node2=Node(None)
        virtual_node3=Node(None)
        virtual_node1.next=self.head
        virtual_node2.next=ll.head
        self.merging(virtual_node1,virtual_node2,virtual_node3)
        self.head=virtual_node1.next 

    @staticmethod
    def merging(start_seg1,start_seg2,next_seg):
        current1=start_seg1.next
        current2=start_seg2.next
        after_seg=next_seg.next
        current_res=start_seg1
        while (current1!=start_seg2.next) and (current1!=None) \
            and (current2!=next_seg.next) and( current2!= None):
            if current1.data>current2.data:
                current_res.next=current2
                current2=current2.next
            else:
                current_res.next=current1
                current1=current1.next
            current_res=current_res.next
        if (current1!=start_seg2.next) and (current1!=None): 
            current_res.next=current1
            start_seg2.next=after_seg
            return start_seg2
        else:
            current_res.next=current2
            return next_seg
            


                
        
    
    def define_segment_and_merging(self, segment_length:int):
        flag_size=False
        virtual_node=Node(None)
        virtual_node.next=self.head       
        i1=0
        start_segment1=virtual_node 
        current = virtual_node.next
        
        state=0
   
        while current:
            match state:
                case 0:
                    i1+=1
                    if i1==segment_length:
                        start_segment2=current
                        i1=0
                        state=1
                case 1: 
                    i1+=1
                    if i1==segment_length:
                        current=self.merging(start_segment1,start_segment2,current)
                        start_segment1=current
                        i1=0
                        state=0   
                        flag_size=True
            current=current.next
        if (state==1):# and (i1!=0): 
            virtual_node1=Node(None)               
            self.merging(start_segment1,start_segment2,virtual_node1)  
        self.head=virtual_node.next     
        return flag_size              


    def mergesort(self):
        segment_length=1
        while self.define_segment_and_merging(segment_length):
            segment_length*=2



                

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаєм елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)



ll1 = LinkedList()
k=16
n=random.randint(0,16)
l1=[random.randint(0,n) for _ in range (n)]
#l1.sort()
for i in l1:
    ll1.insert_at_end(i) 

ll1.print_list()


#ll1.define_segment_and_merging(4)
ll1.mergesort()
ll1.print_list()

