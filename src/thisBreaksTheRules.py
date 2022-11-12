class tooManyNestedBlocks():
    def __init__(self):
        for i in range(2):
            for j in range(2):
                for x in range(2):
                    print("this breaks the max blocks rule")
        for i in range(2):
            for j in range(2):
                for x in range(2):
                    print("this breaks the max blocks rule")
        for i in range(2):
            for j in range(2):
                for x in range(2):
                    print("this breaks the max blocks rule")

def tooManySentences():
    a = 0
    b = 1
    c = 2
    d = 3
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    a = b + c / a
    
        