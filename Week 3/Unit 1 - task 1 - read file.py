import os
path = r'C:\Users\as564\PycharmProjects\pythonProject'
filename = 'Pride and pred.txt'
prideAndPrejudice = os.path.join(path,filename)
try:
    my_file = open(prideAndPrejudice)
    for line in my_file.readlines():
        print(line)
finally:
    my_file.close()


#use function to find chapters
def chapters(path, filename):
    try:
        count = 0
        book = open(path + "\\" + filename)
        for line in book.readlines():
                if line[0:7] == "Chapter" or line[0:7] == "CHAPTER":
                    count += 1
        print("Chapters:", count)
    finally:
            book.close()

chapters(r"C:\Users\as564\PycharmProjects\pythonProject", "Pride and pred.txt")