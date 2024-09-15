import random

def random_results(n):
    results = [f'T{i:02d}' for i in range(1, n+1)]
    random.shuffle(results) #Random results generation
    return results[0]

def random_tbl():
    results2 = [f'n{i:02d}' for i in range(1,21)]
    random.shuffle(results2) #participant number
    return results2[0]
    

def main():
    n = int(input("Enter the limit n: "))
    m = 0
    randomized_results = -2
    exception = []
    done = False
    
    #while m != -1:
    #    m = int(input("Enter not returned list number: "))
    #    exception.append(m)
    
    randomized_results = random_results(n)
    randomized_number = random_tbl()
    
    print("La fiche gagnante est " + randomized_results)
    print("Le numero gagnant est " + randomized_number)


if __name__ == "__main__":
    main()
