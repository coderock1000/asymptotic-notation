def OnTime(n):
    iterations = 0
    for i in range (1, n+1):
        iterations += 1
    print('when n is ', n ,'Iterations = ', iterations)

OnTime(10)
OnTime(20)
OnTime(42)

print("\n with every 'n' the time taken and iterations will increase")