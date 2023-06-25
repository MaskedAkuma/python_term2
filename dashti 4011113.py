import time
users_g = {}
books_g = {}
reserved = {}
reserved_infos = {}
universal_ids = []
not_reserved = []
def book_res_display(reserved):
    if len(reserved) == 0:
        print("there are not any books reserved!")
    else:
        for x, y in reserved.items():
            print(f"{x} =")
            for i, j in y.items():
                print(f"{i,j}")
            print("........#...........")
    for l,m in books_g.items():
        for z,t in m.items():
            if z == "book name":
                for s in reserved.keys():
                    if t != s :
                        not_reserved.append(t)
    print(f"{not_reserved}")
def book_res(books_g,users_g):
    while True:
        p_code = input("please enter your library code or (back) : ")
        if p_code == "back":
            break
        if int(p_code) in list(users_g.keys()):
            res_name = input("pls enter name of the book you wanna reserve : ")
            for y,x in books_g.items():
                for i,j in x.items():
                    if i == "book name":
                        if res_name == j :
                            seconds = time.time()
                            date = time.ctime(seconds)
                            reserved_infos = {
                                "library_code":p_code,
                                "universal_book_ids":y,
                                "date":date
                            }
                            reserved[res_name] = reserved_infos                            
        else :
            print("there are no user with this code !")  
    return(reserved)                              
def book_search(books_g):
    count = 0
    while True:
        met = input("pls enter your search method : ")
        met = null_finder(met)
        if met == "genre":
            genre = input("pls enter book's genre : ")
            for y,x in books_g.items():
                for i,j in x.items():
                    if i == "book's genre":
                        if genre == j :
                            print(books_g[y])
                            count = count + 1
            if count == 0 :
                print("there are no books in this genre!")
            break
        elif met == "name":
            name = input("pls enter book's name : ")
            for y,x in books_g.items():
                for i,j in x.items():
                    if i == "book name":
                        if name == j :
                            print(books_g[y])
                            print("...........#.........")
                            count = count + 1
            if count == 0 :
                print("there are no books with this name!")
            break
        else :
            print(f"{met}: not found!")
def null_finder(the_v):
    while True:
        if the_v == "":
            the_v = input("you should type smth : ")
        else : 
            return(the_v)
def add_user (users_g,universal_ids):
    if len(users_g) == 0:
        library_code = 78979
    else :
        library_code = list(users_g)[-1] + 1
    user = {}
    flag = 1
    
    while flag:
        uni_code = input("pls enter your universal code or (back) : ")
        uni_code = str(null_finder(uni_code))
        if uni_code == "back" :
            flag = 0
        elif uni_code in universal_ids :
            print("another user with this natinal code already exists !")
        else:
            universal_ids.append(uni_code)
            name = input("pls enter your name : ")
            name = null_finder(name)
            l_name = input("pls enter your last name : ")
            l_name = null_finder(l_name)
            while True:
                try :
                    birth_date_d = int(input("please enter your birthday day (dd) : "))
                    birth_date_m = int(input("please enter your birthday month (mm) : "))
                    birth_date_y = int(input("please enter your birthday year (yyyy) : "))
                    birth_date = (str(birth_date_y)+"/"+str(birth_date_m)+"/"+str(birth_date_d))
                    break
                except :
                    print("your birth date should be integers")
            address = input("pls enter your address : ")
            address = null_finder(address)
            seconds = time.time()
            date = time.ctime(seconds)
            user = {
                "uni_code":uni_code,
                "name":name,
                "l_name":l_name,
                "birth_date":birth_date,
                "address":address,
                "date":date,
            }
            users_g[library_code] = user
            return (users_g)
def book_display(books_g):
    if len(books_g) == 0:
        print("there are not any books available!")
    else:
        for x, y in books_g.items():
            print(f"{x} =")
            for i, j in y.items():
                print(f"{i,j}")
            print("........#...........")
def user_display(users_g):
    if len(users_g) == 0:
        print("there are not any users available!")
    else:
        for x, y in users_g.items():
            print(f"{x} = ")
            for i, j in y.items():
                print(f"{i,j}")
            print("........#...........")
def edit_user(users_g):
    user_ed = int(input("pls enter your library code :"))
    if user_ed in users_g.keys():
        print("editing section :")
        uni_code = input("pls enter your new universal code: ")
        uni_code = null_finder(uni_code)
        name = input("pls enter your new name : ")
        name = null_finder(name)
        l_name = input("pls enter your new last name : ")
        l_name = null_finder(l_name)
        while True:
            try :
                birth_date_d = int(input("please enter your new birthday day (dd) : "))
                birth_date_m = int(input("please enter your new birthday month (mm) : "))
                birth_date_y = int(input("please enter your new birthday year (yyyy) : "))
                birth_date = (str(birth_date_y)+"/"+str(birth_date_m)+"/"+str(birth_date_d))
                break
            except :
                print("your birth date should be integers")
        address = input("pls enter your new address : ")
        address = null_finder(address)
        user = {
            "uni_code":uni_code,
            "name":name,
            "l_name":l_name,
            "birth_date":birth_date,
            "address":address,
        }
        users_g.update({user_ed:user})
    else :
        print("there aren't any users with this code!")
    return (users_g)
def remove_books(books_g):
    book = int(input("pls enter the book's library code : "))
    book = null_finder(book)
    if book in books_g.keys():
        for x in list(books_g.keys()):
            if book == x :
                books_g.pop(book)
    else :
        print("there aren't any books with this code!")
    return(books_g)
def remove_user(users_g):
    user = int(input("pls enter your library code : "))
    user = null_finder(user)
    if user in users_g.keys():
        for x in list(users_g.keys()):
            if user == x :
                users_g.pop(user)
    else :
        print("there aren't any users with this code!")
    return(users_g)
def add_book(books_g):
    if len(books_g) == 0:
        universal_book_ids = 1234
    else :
        universal_book_ids = list(books_g)[-1] + 1
    book={}
    flag = 1
    while flag:
        book_nm = input("pls enter the book name or type(back) : ")
        book_nm = str(null_finder(book_nm))
        if book_nm == "back":
            flag = 0
        else:
            book_nm = null_finder(book_nm)
            writer = input("pls enter the writer's name : ")
            writer = null_finder(writer)
            while True:
                try :
                    publish_y = int(input("please enter the book's publish year (yyyy) : "))
                    break
                except :
                    print("the books's publish year should be integers")
            genre = input("pls enter the book's genre : ")
            genre = null_finder(genre)
            book = {
                "book name":book_nm,
                "writer":writer,
                "publish year":publish_y,
                "book's genre":genre,
            }
            books_g[universal_book_ids] = book
            return(books_g)
def book_edit(books_g):
    book_ed = int(input("pls enter book's library code :"))
    if book_ed in books_g.keys():
        print("editing section :")
        book_nm = input("pls enter book's new name : ")
        book_nm = null_finder(book_nm)
        writer = input("pls enter book's new writer name : ")
        writer = null_finder(writer)
        while True:
            try :
                publish_y = int(input("please enter the book's publish year (yyyy) : "))
                break
            except :
                print("book's publish year should be integers")
        genre = input("pls enter book's new genre : ")
        genre = null_finder(genre)
        book = {
            "book name":book_nm,
            "writer":writer,
            "publish year":publish_y,
            "book's genre":genre,
        }
        books_g.update({book_ed:book})
    else :
        print("there aren't any books with this code!")
    return (books_g)
while True:
    oprt = input("please enter your opration or type (help) :")
    oprt = str(null_finder(oprt))
    if oprt == "help" :
        print("1.book_add : you could add books!\n")
        print("2.user_add : you could add users!\n")
        print("3.book_remove : you could remove books!\n")
        print("4.user_remove : you could remove users!\n")
        print("5.book_search : you could search books!\n")
        print("6.user_display : you could display users!\n")
        print("7.books_display : you could display books!\n")
        print("8.user_edit : you could edit books!\n")
        print("9.book_edit : you could edit users!\n")
        print("10.book_res : you could reserve books!\n")
        print("11.book_res_display : you could display reserved books!\n")
        print("12.exit : closes the program!\n")   
    elif oprt == "book_add" :
        books_g = add_book(books_g)
    elif oprt == "user_add" :
        users_g = add_user(users_g,universal_ids)
    elif oprt == "user_remove" :
        user_display(users_g)
        users_g = remove_user(users_g)
    elif oprt == "book_remove" :
        book_display(books_g)
        books_g = remove_books(books_g)
    elif oprt == "user_edit" :
        user_display(users_g)
        users_g = edit_user(users_g)
    elif oprt == "book_edit" :
        books_g(books_g)
        books_g = book_edit(books_g)
    elif oprt == "book_res" :
        book_display(books_g)
        reserved = book_res(books_g,users_g)
    elif oprt == "user_display" :
        user_display(users_g)
    elif oprt == "book_display" :
        book_display(books_g)
    elif oprt == "book_search" :
        book_search(books_g)
    elif oprt == "book_res_display":
        book_res_display(reserved)
    elif oprt == "exit" :
        break
    else :
        print(f"{oprt}:command not found!")
