from models.linked_list import LinkedList


def main():
    llist1 = LinkedList()

    llist1.insert_at_beginning(10)
    llist1.insert_at_beginning(6)
    llist1.insert_at_beginning(8)
    llist1.insert_at_beginning(1)

    llist2 = LinkedList()
    llist2.insert_at_beginning(6)
    llist2.insert_at_beginning(9)
    llist2.insert_at_beginning(7)
    llist2.insert_at_beginning(3)
    llist2.insert_at_beginning(22)
    llist2.insert_at_beginning(1)

    llist1.bubble_sort()
    llist2.bubble_sort()

    llist1.print_list()
    llist2.print_list()

    print("Merged list:")

    merged_list = llist1.merge_sorted_lists(llist2)
    merged_list.print_list()

    print("Reversed list:")

    merged_list.reverse()
    merged_list.print_list()


if __name__ == "__main__":
    main()
