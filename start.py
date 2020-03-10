import requests
from lib.checkDb import create_db, data_terminals
from lib.dbTerminal import Db_terminal



exit = False
while not exit:
    print("========= DB Terminal =============")
    print("""
    1. Create DB Terminal
    2. Get data by City
    3. Insert Data in to DB
    4. Select by city
    5. Select by street
    0. Exit
    """)
    choice = int(input())
    if choice == 1:
        # two = Db_terminal(("localhost", "root", "", "bank"))
        create_db()
         
            
       
    elif choice == 2:
        data_terminals()
        
        
    elif choice == 3:
        two = Db_terminal("localhost", "root", "", "bank")
        two.insert_data()
       

        
    elif choice == 4:
        three = Db_terminal("localhost", "root", "", "bank")
        result = three.get_city()
        if result:
            for item in result:
                print("{}\n{}\n{}\n{}\n{}" .format(item[0], item[1], item[2], item[3], item[4]))
                print ("==============================================")
        elif not result:
            print("City is not in base. Add a city:")
            three.insert_data()
            
            
       
    elif choice == 5:
        four = Db_terminal("localhost", "root", "", "bank")
        result = four.get_street()
        for item in result:
            print("{}\n{}\n{}\n{}\n{}" .format(item[0], item[1], item[2], item[3], item[4]))
            print ("==============================================")





    elif choice == 0:

        exit = True
    else:
        print("read manual")
