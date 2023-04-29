# n=int(input())
# my_list=[]
# for i in range(0,n):
#     elements=my_list(map(int, input().split()))
#     my_list.append(elements)
#     my_tuple=tuple(my_list)
# print(hash(my_tuple))

if __name__ == "__main__":
    n=int(input())
    mylist = []        # empty list 
 
    for i in range(n): 
        x = int(input("Enter a number: ")) 
        mylist.append(x)        # append the number into list 
    
    mytuple = tuple(mylist)        # convert list into tuple 
    
    print(hash(mytuple)) 