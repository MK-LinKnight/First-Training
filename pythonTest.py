import timeit
import cProfile
# import matplotlib
print(timeit.timeit("x = 2 + 2"))
print(timeit.timeit("x= sum(range(10))"))

def main():
    print("#######",1)

print(cProfile.run('main()'))