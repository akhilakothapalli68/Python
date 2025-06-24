'''Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  2 to 5, print Not Weird
If  is even and in the inclusive range of  6 to 20 , print Weird
If  is even and greater than , print Not Weird'''
'''
n=3--->weird
n=24--->not weird
n=4--->not weird
'''
# n=int(input())
# if n%2==1:
#     print('weird')
# elif n%2==0 and range(2,5):
#     print('not weird')
# elif n%2==0 and range(6,20):
#     print('weird')
# elif n%2==0 and n>20:
#     print('not weird')
'''or'''
# n = int(input())
# if(n % 2 ==1):
#     print("Weird")
# elif(2 <= n <= 5):
#         print("Not weird")
# elif(6 <= n <= 20):
#     print("Weird")
# else:
#     print("Not Weird")
'''or'''
# n=int(input().strip())
# if n%2==0:
#     if 2<=n<=5 or n>20:
#         print('not weird')
#     else:
#         print('weird')
# else:
#     print('weird')


