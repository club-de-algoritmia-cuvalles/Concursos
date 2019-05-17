#La Tribu problem 4
#Yes
from sys import stdin, stdout

serie = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
         2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
         317811, 514229, 832040, 1346269]

if __name__ == "__main__":
    num = int(stdin.readline())

    if not num in serie:
        stdout.write("The number is not valid\n")

    else:
        ind =  serie.index(num)
        if ind > (len(serie)-3):
            stdout.write("The number is valid in the sequence of the series and is\n{}/{}. The successor is {}/{}\n".format(serie[ind -1], serie[ind], serie[ind], serie[ind+1]))

        else:
            stdout.write("The number is valid in the sequence of the series and is\n{}/{}. The successor is {}/{}\n".format(serie[ind], serie[ind+1], serie[ind+1], serie[ind+2]))
    
            

            
