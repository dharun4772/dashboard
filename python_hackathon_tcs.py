class Book:
    def __init__(self,bookId,bookName,bookTechnology,bookPrice,authorname):
        self.bookId=bookId
        self.bookName=bookName
        self.bookTechnology=bookTechnology
        self.bookPrice=bookPrice
        self.authorname=authorname
    
class BookStore:
    def __init__(self,bookdb,bookStoreName):
        self.bookdb=bookdb
        self.bookStoreName=bookStoreName

    def searchByName(self,title):
        l=[]
        for k,v in self.bookdb.items():
            if(v.bookName==title):
                l.append(v)
        if(len(l)):
            return l
        return None

    def calculatePriceByTechnology(self,bookTechnology):
        sum_book=0
        for k,v in self.bookdb.items():
            if(v.bookTechnology==bookTechnology):
                sum_book+=v.bookPrice
        if(sum_book!=0):
            disc_price=sum_book-(sum_book*10)/100
            return disc_price
        return 0.0


n=int(input())
dick={}
i=1
while(i<=n):
    bookId=int(input())
    bookName=input()
    bookTechnology=input()
    bookPrice=float(input())
    authorname=input()
    obj=Book(bookId,bookName,bookTechnology,bookPrice,authorname)
    dick[i-1]=obj
    i+=1
title=input()
booktech_search=input()
obj1=BookStore(dick,"sample")
l=obj1.searchByName(title)
if(l!=None):
    for i in l:
        print(i.bookId)
        print(i.bookName)
        print(i.bookTechnology)
        print(int(i.bookPrice))
        print(i.authorname)
else:
    print("No Book Exists with the BookName")
price=obj1.calculatePriceByTechnology(booktech_search)
if(price==0.0):
    print(0.0)
else:
    print(price)
