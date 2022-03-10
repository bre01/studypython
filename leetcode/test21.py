def mergeTwoLists( list1, list2):
        list=[]
        while list1 and list2:
            if list1[0]>list2[0]:
                list.append(list2[0])
                list2.remove(list2[0])
            else:
                list.append(list1[0])
                list1.remove(list1[0])
        for i in list1:
            list.apepnd(i)
        for i in list2:
            list.append(i)
        return list 
print(mergeTwoLists([1,2,3,4,5,6,8],[2,5,6,8]))