# Python Driver Code

def solve(n: int) -> str:
  primes = [];
 
# Generating all the prime numbers
# from 2 to n.
def SieveofEratosthenes(n):
 
    visited = [False] * (n + 2);
    for i in range(2, n + 2):
        if (visited[i] == False):
            for j in range(i * i, n + 2, i):
                visited[j] = True;
            primes.append(i);
 
def specialPrimeNumbers(n, k):
 
    SieveofEratosthenes(n);
    count = 0;
    for i in range(len(primes)):
        for j in range(i - 1):
 
            # If a prime number is Special
            # prime number, then we increments
            # the value of k.
            if (primes[j] +
                primes[j + 1] + 1 == primes[i]):
                count += 1;
                break;
 
        # If at least k Special prime numbers
        # are present, then we return 1.
        # else we return 0 from outside of
        # the outer loop.
        if (count == k):
            return True;
 
    return False;
 
# Driver Code
n = 16;
k = 18;
if (specialPrimeNumbers(n, k)):
    print("YES");
else:
    print("NO");
  # n is the given input
  return "Special"

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
