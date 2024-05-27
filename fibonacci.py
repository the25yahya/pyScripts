def febonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else :
        return febonacci(n -1) + febonacci(n - 1)
    
while True:
    febonacci(0)