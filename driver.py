import sodokuSolver
import copy

if __name__ == "__main__":
    textFile = raw_input("Name of your file: ")
    test = []
    temp = []
    with open(textFile) as fileobj:
        for line in fileobj:
            for ch in line:
                if ch != '\n' and ch != ' ':
                    temp.append(ch)
            test.append(temp)
            temp = []
    before = copy.deepcopy(test)
    sodokuSolver.search(test)
    sodokuSolver.print_before_after(before, test)
