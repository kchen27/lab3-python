# Author: Kyle Chen kvc5823@psu.edu
# Collaborator: Aaron Hester amh7806@psu.edu
# Collaborator: Jiarou Deng dpj5243@psu.edu
# Collaborator: Livia Moore lmm6882psu.edu 
# Section: 10
# Breakout: 11

def sum_n(n):
  if n == 0:
    return n
  else:
    return n + sum_n(n-1)

def print_n (s, n):
  if n <= 0:
    return
  else:
    print (s)
    print_n(s, n-1)

def run():
  num = input("Enter an int: ")
  num_int = int(num)
  print(f"sum is {sum_n(num_int)}.")
  string = input("Enter a string: ")

  print_n(string, num_int)

if __name__ == "__main__":
  run()
