def _sum_of_rows_sample_(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(sum(item))
    return mylist

x= [[1,2,3],[4,5,6],[7,8,9]]
print (_sum_of_rows_sample_(x))
