# Type your code here
def twoD(list_of_numbers):

    total_sum = 0                                #initialize total sum to be zero
    
    number_of_rows = len(list_of_numbers)        #Get the length of rows
    number_of_columns = len(list_of_numbers[0])  #Get the length of columns (assumes same in all)
    
    rows = 0                                     #Initialize row index to zero
    
    while rows < number_of_rows:                 #Produce row indices 0,1,2,...number_of_rows
        columns  = 0                             #For each row, initialize the column index to zero
        while columns < number_of_columns:       #Produce column indices 0,1,2, ...number_of_columns
            total_sum = total_sum + list_of_numbers[rows][columns] #Add the elemnte to totalsum
            columns = columns + 1                  #Increment columns by 1
        rows = rows + 1                          #Increment rows by 1
    return total_sum                             #Return total sum
        
    
    
#TEST

x = [[1,2,3],[4,5,6],[7,8,9]]
print (twoD(x))
