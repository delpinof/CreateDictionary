import string

def string_to_list(string):
    list1=[]
    list1[:0]=string
    return list1

def main():
    characters = string_to_list(string.ascii_uppercase+string.digits)
    file = open("dictionary.txt", "a")
    for l1 in characters:
        for l2 in characters:
            for l3 in characters:
                for l4 in characters:
                    for l5 in characters:
                        for l6 in characters:
                            file.write(l1+l2+l3+l4+l5+l6+"D49F\n")

if __name__ == "__main__":
    main()