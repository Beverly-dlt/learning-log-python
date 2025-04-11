
#libManage.py: Library management code 
#
from library import Author, comedy, fiction, sciencefiction

def main():
        booklist = []
        print("\t\t Welcome to Libraray management")
        fileobj = open('Books.csv', 'r')
        books = fileobj.readlines()
    
        fileobj.close()
        for book in books:
            temp = None 
            sline = [s for s in book.strip().split(',')]
            auth = [a for a in sline[2].split(':')]
            tempauth = Author(auth[0],auth[1])
            if sline[0] == 'Comedy':
                temp = comedy(sline[1], tempauth, sline[3], sline[0])
            elif sline[0] == 'Fiction':
                temp = fiction(sline[1], tempauth, sline[3], sline[0])
            elif sline[0] =='Science Fiction':
                temp = sciencefiction(sline[1], tempauth, sline[3], sline[0])
            else:
               print(sline[0], ' unidentified book type')
            if temp:
                booklist.append(temp)

        for b in booklist:
            b.displayBook()
if __name__ =='__main__':
    main()

            
