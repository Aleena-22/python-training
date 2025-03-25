def checkprime(n):
    for i in range(2, n):
        if (n%i == 0):
            return False
    return True

def highPrime(m, n):
    for i in range(n, m-1, -1):
        if(checkprime(i)):
            return i
    return None

def getAllprime(m, n):
    count = 0
    primeNumbers = []
    for x in range(m, n + 1):
        if(checkprime(x)):
            count += 1
            primeNumbers.append(x)
    return count, primeNumbers

if __name__ == "__main__":
    print("10 ", checkprime(10))

    print("100, 200 ", highPrime(100, 200))

    print(getAllprime(100, 200))
