print("while loop:")
def fibSeq(n):
    fib = []
    if n == 0:
        fib = [0]
    if n == 1:
        fib = [0, 1]
    i = 2
    fib =[0, 1]
    while i < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib

print("Fib sequences generated:")
print(fibSeq(10))

print("recursive method:")
def fibSeqRe(n):
    if n < 2:
        return n
    return fibSeqRe[n - 1] + fibSeqRe[n - 2] 
print("Fib sequences generated:")
print(fibSeq(10))