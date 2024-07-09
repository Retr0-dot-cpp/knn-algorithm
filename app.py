import math

#just insert your data in x y and classes they belong to

x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [2, 2, 1, 0, 2, 1, 1, 0, 1, 1] 


info = list(zip(x, y, classes))
len = len(x)
output = []

def neighbors(x1,y1, neighbours):
    for i in range(len):
        dif1 = x1-x[i]
        dif2 = y1-y[i]
        equation = math.sqrt(dif1**2 + dif2**2)
        output.append(equation)
        i+=1
    zipped = list(zip(output, info))
    zipped.sort()

    o = [(t[0], *t[1]) for t in zipped]

    test_neighbours = o[:neighbours]

    classifier = [tup[-1] for tup in test_neighbours]

    identifier = max(classifier, key=classifier.count)

    print(f"point {x1},{y1} belongs to class {identifier}")
    

neighbors()

