import pytest
import random
import logging
import task1

# Настройка логгера
logger=None
def setup_module():
    ''' Setup for the entire module '''
    global logger
    #logging.basicConfig(level=logging.DEBUG)
    
    logging.basicConfig(level=logging.DEBUG, filename="test_1.log",filemode="w")
    logger = logging.getLogger(__name__) 
    
    logger.info('Inside Setup')
    # Do the actual setup stuff here
    pass

def test_llist_merging():
    llist1 = task1.LinkedList()
    llist1.insert_at_beginning(6)
    llist1.insert_at_beginning(4)
    llist1.insert_at_beginning(2)

    llist2 = task1.LinkedList()
    llist2.insert_at_beginning(5)
    llist2.insert_at_beginning(3)
    llist2.insert_at_beginning(1)

    llist1.print_list()

    llist2.print_list()

    llist1.llist_merging(llist2)
    llist1.print_list()
    l=llist1.linkedList2list()
    assert l==[1,2,3,4,5,6]

def test_llist_merging_random():
    k=100
    res=0
    for _ in range(k):
        n=random.randint(0,5)
        m=random.randint(0,5)
        ll1= task1.LinkedList()
        l1=[random.randint(0,n+m) for _ in range (n)]
        l1.sort()
        for i in l1:
            ll1.insert_at_end(i) 
        ll2= task1.LinkedList()
        l2=[random.randint(0,n+m) for _ in range (m)]
        l2.sort()
        for i in l2:
            ll2.insert_at_end(i)  
        ll1.llist_merging(ll2)     
        l_from_ll=ll1.linkedList2list()
        l12=l1+l2
        l12.sort()
        assert l12==l_from_ll
        if l12==l_from_ll:
            res+=1
    assert res==k

def test_llist_merging_empty():
    llist1 = task1.LinkedList()

    llist2 = task1.LinkedList()

    llist1.print_list()

    llist2.print_list()

    llist1.llist_merging(llist2)
    llist1.print_list()
    l=llist1.linkedList2list()
    assert l==[]

def test_mergesort():
    k=16
    for i in range(k):
        n=random.randint(0,16)
        l1=[random.randint(0,n) for _ in range (n)]
        #l1.sort()
        ll1 = task1.LinkedList()
        for i in l1:
            ll1.insert_at_end(i) 

        ll1.print_list()


        #ll1.define_segment_and_merging(4)
        ll1.mergesort()
        ll1_sort=ll1.linkedList2list()
        l1_sort=sorted(l1)
        logger.info(f"n {n}")
        logger.debug(f" source     : {l1_sort}")
        logger.debug(f"Linked list : {ll1_sort}")
        assert ll1_sort==l1_sort