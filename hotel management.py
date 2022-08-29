

# final
import datetime
import pandas as pd

dic_rooms_ac = {"401": 0, "402": 0, "403": 0, "404": 0, "201": 0, "202": 0, "203": 0, "204": 0}
dic_rooms_nonac = {"101": 0, "102": 0, "103": 0, "104": 0, "301": 0, "302": 0, "303": 0, "304": 0,
                   "501": 0, "502": 0, "503": 0, "504": 0}
# record={"ph no.":[name,ph no.,adres,room no.,roomprice,checkin,food]}
temp_record = {}
per_name = []
per_phone = []
per_address = []
per_room = []
per_check_in = []
per_check_out = []
per_bill = []


def home():
    print("\n\n...........welcome to Hotel ABC.........\n\n")
    x = input("Enter 1 for customer services\nEnter 2 for staff purpose\n")
    if int(x) == 1:
        y = input("Enter 1 for room booking\nEnter 2 for restaurant service\nEnter 3 for payment\n")
        if int(y) == 1:
            Booking()
        elif int(y) == 2:
            restaurant()
        elif int(y) == 3:
            payment()
    elif int(x) == 2:
        for i in range(3):
            psw = input("Enter password :  # pwd is 123456")
            if psw == "123456":
                z = input("Enter 1 for total customer data\nEnter 2 for present customer's data")
                if int(z) == 1:
                    customer_data()
                elif int(z) == 2:
                    print(temp_record)
                break
            else:
                print("Sorry ! Wrong password. You have " + str(2 - i) + "left")
        home()


def name_check():
    x = input("Enter your name:")
    if x != "":
        return x
    elif x == "":
        print("                    !!!   Name cant be empty")
        return name_check()


def ph_no_check():
    x = input("Enter your mobile no:")
    if len(x) == 10:
        try:
            int(x)
            return str(x)
        except:
            print("                   !!!   Enter valid mobile no:")
            return ph_no_check()
    else:
        print("                    !!!   Enter a valid mobile no.")
        return ph_no_check()


def ad_check():
    x = input("Enter your address:")
    if x != "":
        return x
    elif x == "":
        print("                    !!!   Address cant be empty")
        return ad_check()


def in_datetime_check():
    try:
        ci_d = input("Enter check in date and time in the format: date/month/year hours:minutes  ")
        check_in = datetime.datetime.strptime(ci_d, "%d/%m/%Y %H:%M")
        return check_in
    except:
        print("       !!!   Enter valid date and time in specified format ")
        return in_datetime_check()


def out_datetime_check(mob_no):
    try:
        check_in = temp_record[mob_no]["check_in"]
        co_d = input("Enter check out date and time in the format: date/month/year hours:minutes  ")
        check_out = datetime.datetime.strptime(co_d, "%d/%m/%Y %H:%M")
        no_of_days = check_out - check_in
        if int(no_of_days.days) >= 0:  # and int(no_of_days.seconds)>0:
            return check_out
        else:
            print("Check out datetime must fall after check in datetime")
            return out_datetime_check(mob_no)
    except:
        print("          !!!   Enter valid date and time in specified format")
        return out_datetime_check(mob_no)


def Booking():
    print("...ROOM BOOKING...")
    name = name_check()
    ph_no = ph_no_check()
    ad = ad_check()
    temp_record[ph_no] = {}

    roomtype = input(
        "...select Room type.....\nEnter 1 for AC room : Rs 1000\nEnter 2 for non-AC room : Rs 500\nPress any other number to to exit")

    def room(roomtype):
        ac_rooms_available = []
        nonac_rooms_available = []
        for i in dic_rooms_ac:
            if dic_rooms_ac[i] == 0:
                ac_rooms_available.append(i)

        for i in dic_rooms_nonac:
            if dic_rooms_nonac[i] == 0:
                nonac_rooms_available.append(i)

        if len(ac_rooms_available) == 0 and len(nonac_rooms_available) == 0:
            print("Sorry . All the rooms are occupied")
            home()

        else:

            if int(roomtype) == 1:

                if len(ac_rooms_available) == 0:
                    print("sorry. All the rooms are occupied ")
                    print("Do you want to go for non-ac room?   ")
                    x = input("Enter 1 if YES .. 2 if NO")
                    if int(x) == 1:
                        room(2)
                    else:
                        home()
                else:
                    print("These are the rooms available : ")
                    print(ac_rooms_available)
                    room_no_alloted = input("Enter the room no. that u want.")
                    dic_rooms_ac[room_no_alloted] = 1
                    temp_record[ph_no]["name"] = name
                    temp_record[ph_no]["phone"] = ph_no
                    temp_record[ph_no]["address"] = ad
                    temp_record[ph_no]["room"] = room_no_alloted
                    temp_record[ph_no]["roomprice"] = 1000

                    check_in = in_datetime_check()
                    temp_record[ph_no]["check_in"] = check_in
                    print("...ROOM BOOKED SUCCESSFULLY ...")
                    home()

            elif int(roomtype) == 2:

                if len(nonac_rooms_available) == 0:
                    print("sorry. All the rooms are occupied ")
                    print("Do want to go for AC ?")
                    y = input("Enter 1 if YES  ... 2 if NO ")
                    if int(y) == 1:
                        room(1)
                    else:
                        home()
                else:
                    print("These are the rooms available : ")
                    print(nonac_rooms_available)
                    room_no_alloted = input("Enter the room no. that u want.")
                    dic_rooms_nonac[room_no_alloted] = 1
                    temp_record[ph_no]["name"] = name
                    temp_record[ph_no]["phone"] = ph_no
                    temp_record[ph_no]["address"] = ad
                    temp_record[ph_no]["room"] = room_no_alloted
                    temp_record[ph_no]["roomprice"] = 500

                    check_in = in_datetime_check()
                    temp_record[ph_no]["check_in"] = check_in
                    print("...ROOM BOOKED SUCCESSFULLY...")
                    home()


            else:
                print("  !!!  Invalid input  ")
                Booking()

    room(roomtype)


def menu_card():
    print("**Menu Card**")
    print("-----------------------------------------------------------------------")

    print("STARTERS                                 ICE CREAM           ")
    print("----------------------------------       ------------------------------------")
    print("1.Tandoori Paneer Tikka.......220.00     38.Vanilla.....................60.00")
    print("2.Malai Paneer Tikka..........220.00     39.Strawberry..................60.00")
    print("3.Soya Tandoori Tikka ........175.00     40.Pineapple...................60.00")
    print("4.Tandoori Aloo...............179.00     41.Butter Scotch...............60.00")
    print("5.Punjabi Soya Chap...........179.00     42.plane ice...................40.00")
    print("6.Hare-Bhare Kabab............162.00                                         ")
    print("7.Dahi ke Kabab...............179.00     NORTH INDIAN")
    print("8.Platter.....................325.00     ------------------------------------")
    print("                                         43.Aloo Matar.................140.00")
    print("ALL TIME FAVOURITE                       44.Malai Kofta................140.00")
    print("----------------------------------       45.Jeera Aloo.................140.00")
    print("9.french Fries................106.00     46.Mix Veg....................140.00")
    print("10.Chilli Cheese Toast.........115.00    47.Matar Mushroom.............140.00")
    print("11.Chilli Cheese Gralic Toast..115.00    48.Chilli Paneer..............140.00")
    print("12.Garlic Bread.................98.00    49.Handi Paneer...............120.00")
    print("13.Garlic Bread with Cheese....119.00    50.Palak Paneer...............120.00")
    print("                                         51.Kadai Paneer...............110.00")
    print("SANDWICH")
    print("----------------------------------       SOUTH INDIAN")
    print("14.Plain Sandwich..............175.00    ------------------------------------")
    print("15.Grilled Sandwich............175.00    52.Sambhar Vada...............140.00")
    print("16.Club Sandwich...............175.00    53.Rice Idli..................130.00")
    print("                                         54.Paneer Dosa................130.00")
    print("SALADS                                   55.Masala Dosa................130.00")
    print("----------------------------------       56.Onion Dosa.................110.00")
    print("17.Russian Salad / Maccroni....119.00    57.Plain Dosa.................100.00")
    print("                                      ")
    print("BURGERS                                  SOUPS")
    print("----------------------------------       ------------------------------------")
    print("18.Veg. Burger..................72.00    58.Veg. Munchow...............110.00")
    print("                                         59.Sweet Corn.................110.00")
    print("BAKES & MEALS (SERVED WITH 3PCS. OF GARLIC BREAD)")
    print("----------------------------------       60.Veg. Noodle Soup...........110.00")
    print("19.Maccroni Hotpot.............205.00    61.Hot & Sour.................110.00")
    print("20.Veg. Augratin...............205.00    62.Tomato Soup................110.00")
    print("")
    print("SUBZIYAN                                 BREADS")
    print("----------------------------------       ------------------------------------")
    print("21.Shahi Paneer................210.00    63.Tandoori Roti...............30.00")
    print("22.Kadhai Paneer ..............210.00    64.Roomali Roti................17.00")
    print("23.Paneer Butter Masala........210.00    65.Butter Roti.................36.00")
    print("24.Mushroom Masala ............215.00    66.Plain Naan..................43.00")
    print("25.Malai Kofta.................210.00    67.Butter Naan.................58.00")
    print("                                         68.Garlic Naan Butter..........60.00")
    print("DALS                                     69.Tawa Parantha...............53.00")
    print("----------------------------------       70.Laccha Parantha.............53.00")
    print("26.Dal Makhani.................192.00    71.Pudina Parantha.............53.00")
    print("27.Yellow Dal..................141.00    72.Stuffed Kulcha (Aloo).......65.00")
    print("28.Rajma ......................141.00    73.Stuffed Kulcha (Paneer).....65.00")
    print("29.Chole ......................141.00    74.Papad.......................15.00")
    print("                                         ")
    print("TEA & COFFEE	                            SMOOTHIES & MOCKTAILS")
    print("----------------------------------       ------------------------------------")
    print("30.Tea.........................40.00     75.Red Sea....................150.00")
    print("31.Coffee Mocachino............51.00     76.Virgin Colada..............150.00")
    print("32.Coffee Americano (Black) ...55.00     77.Love Valley................150.00")
    print("33.Coffee Espresso.............60.00     78.Watermelon Mojito..........150.00")
    print("34.Ice Tea (Lemon).............51.00     79.White Rosy.................150.00")
    print("35.Coffee Cappuccino...........51.00     80.Virgin Guava...............150.00")
    print("36.Espresso (Black)............55.00     81.Litchi Smoothie............150.00")
    print("37.Cold-Coffee (Frappe)........70.00     82.Peach Apricot..............150.00")


def item_sel():
    x = []
    bill = []
    list_all_items = {}
    items = (("Tandoori Paneer Tikka", 220.00), ("Malai Paneer Tikka", 220.00), ("Soya Tandoori Tikka", 175.00),
             ("Tandoori Aloo", 179.00), ("Punjabi Soya Chap", 179.00), ("Hare-Bhare Kabab", 162.00),
             ("Dahi ke Kabab", 179.00), ("Platter", 325.00), ("french Fries", 106.00), ("Chilli Cheese Toast", 115.00),
             ("Chilli Cheese Gralic Toast", 115), ("Garlic Bread", 98), ("Garlic Bread with Cheese", 119),
             ("Plain Sandwich", 175), ("Grilled Sandwich", 175.00), ("Club Sandwich", 175),
             ("Russian Salad""/ Maccroni", 119), ("Veg. Burger", 72), ("Maccroni Hotpot", 205), ("Veg. Augratin", 205),
             ("Shahi Paneer", 210), ("Kadhai Paneer", 210), ("Paneer Butter Masala", 210), ("Mushroom Masala", 215),
             ("Malai Kofta", 210), ("Dal Makhani", 192), ("Yellow Dal", 141), ("Rajma", 141), ("Chole", 141),
             ("Tea", 40), ("Coffee Mocachino", 51), ("Coffee Americano (Black)", 55), ("Coffee Espresso", 60),
             ("Ice Tea (Lemon)", 51), ("Coffee Cappuccino", 51), ("Espresso (Black)", 55), ("Cold-Coffee (Frappe)", 70),
             ("Vanilla", 60), ("Strawberry", 60), ("Pineapple", 60), ("Butter Scotch", 60), ("plane ice", 40),
             ("Aloo Matar", 140), ("Malai Kofta", 140), ("Jeera Aloo", 140), ("Mix Veg", 140), ("Matar Mushroom", 140),
             ("Chilli Paneer", 140), ("Handi Paneer", 120), ("Palak Paneer", 120), ("Kadai Paneer", 110),
             ("Sambhar Vada", 140), ("Rice Idli", 130), ("Paneer Dosa", 130), ("Masala Dosa", 130), ("Onion Dosa", 110),
             ("Plain Dosa", 100), ("Veg. Munchow", 110), ("Sweet Corn", 110), ("Veg. Noodle Soup", 110),
             ("Hot & Sour", 110), ("Tomato Soup", 110), ("Tandoori Roti", 30), ("Roomali Roti", 17),
             ("Butter Roti", 36), ("Plain Naan", 43), ("Butter Naan", 58), ("Garlic Naan Butter", 60),
             ("Tawa Parantha", 53), ("Laccha Parantha", 53), ("Pudina Parantha", 53), ("Stuffed Kulcha (Aloo)", 65),
             ("Stuffed Kulcha (Paneer)", 65), ("Papad", 15), ("Red Sea", 150), ("Virgin Colada", 150),
             ("Love Valley", 150), ("Watermelon Mojito", 150), ("White Rosy", 150), ("Virgin Guava", 150),
             ("Litchi Smoothie", 150), ("Peach Apricot", 150))
    try:
        order = int(input("enter the food number you wanted to order from the menu card = "))

        if order in range(1, 83):
            bill.append(items[order - 1][1])
            if order not in x:
                list_all_items[items[order - 1][0]] = 1
                x.append(order)
            elif order in x:
                list_all_items[items[order - 1][0]] = list_all_items[items[order - 1][0]] + 1

            def cont_order(nxt):
                try:
                    # int(nxt)
                    order = int(nxt)
                    if order in range(1, 83):
                        bill.append(items[order - 1][1])
                        if order not in x:
                            list_all_items[items[int(order) - 1][0]] = 1
                            x.append(order)
                        elif order in x:
                            list_all_items[items[order - 1][0]] += 1

                        a = input("give the respective item number to place the order\nto stop ordering enter:stop"
                                  "\nto show ur orders enter: list \n  ")
                        cont_order(a)

                    elif order not in range(1, 83):
                        b = input("sorry the item number you entered is in not in menu. Please enter from the menu card:")
                        cont_order(b)


                except:
                    str(nxt).lower()
                    if nxt == "stop":
                        print("the food items you ordered")
                        print(list_all_items)

                    elif nxt == "list":
                        print("the food items you ordered")
                        print(list_all_items)
                        d = input("give the respective item number to place the order\nto stop ordering enter:stop"
                                  "\nto show ur orders enter: list \n  ")
                        cont_order(d)
                    else:
                        d = input("give the respective item number to place the order\nto stop ordering enter:stop"
                                  "\nto show ur orders enter: list \n  ")
                        cont_order(d)

            cont = input("give the respective item number to place the order\nto stop ordering enter:stop"
                         "\nto show ur orders enter: list \n  ")
            cont_order(cont)
            sum = 0.0
            for i in bill:
                sum = sum + i
            return sum

        elif order not in range(1, 83):
            print("sorry the item number you entered is in not in menu. Please enter from the menu card:")
            k = item_sel()
            return k
    except:
        print("..!Invalid input")
        q=item_sel()
        return q


def restaurant():
    print("Welcome to restaurant section ")
    ph_no = ph_no_check()
    if ph_no in temp_record:
        menu_card()
        p = item_sel()
        temp_record[ph_no]["food"] = p
        home()
    elif ph_no not in temp_record:
        name = name_check()
        menu_card()
        s = item_sel()
        print(".......BILL......")
        print("Name : ", name)
        print("Mobile No : ", ph_no)
        print("Amount : Rs", s)
        Opt = input("choose the mode of payment :\n 1- Credit/Debit Cardcash\n2- Using UPI \n 3- Cash:  ")
        if Opt == 1:
            input("Enter card holder name:")
            print("amount:{}".format(s))
        elif Opt == 2:
            input("Enter UPI:")
            print("amount:{}".format(s))
        else:
            print("the bill is {}".format(s))
        print("Your payment is successfully done\n .....THANK YOU.....")
        home()


def payment():
    print("....Welcome to the payment section....")
    mob_no = ph_no_check()
    if mob_no in temp_record:
        print("Your check in date and time : ", temp_record[mob_no]["check_in"])
        check_out = out_datetime_check(mob_no)
        days_spent = check_out - temp_record[mob_no]["check_in"]
        if int(days_spent.days) == 0:
            price = int(temp_record[mob_no]["roomprice"])
        elif int(days_spent.days) >= 1:
            if int(days_spent.seconds) > 3600:  # int(days_spent.days)*int(86400)>3600:
                price = (int(days_spent.days) + 1) * int(temp_record[mob_no]["roomprice"])
            else:
                price = int(days_spent.days) * int(temp_record[mob_no]["roomprice"])

        total_price = price + int(temp_record[mob_no].get("food", 0))
        print("your bill for room: " + str(price))
        print("your bill for food: " + str(temp_record[mob_no].get("food", 0)))
        print("Your total bill is: " + str(total_price))
        Opt = input("choose the mode of payment :\n 1- Credit/Debit Cardcash\n2- Using UPI \n 3- Cash:  ")
        if Opt == 1:
            input("Enter card holder name:")
            print("amount:{}".format(str(total_price)))
        elif Opt == 2:
            input("Enter UPI:")
            print("amount:{}".format(str(total_price)))
        else:
            print("the bill is {}".format(str(total_price)))
        print("Your payment is successfully done\n .....THANK YOU.....")
        if temp_record[mob_no]["roomprice"] == 1000:
            dic_rooms_ac[str(temp_record[mob_no]["room"])] = 0
        elif temp_record[mob_no]["roomprice"] == 500:
            dic_rooms_nonac[str(temp_record[mob_no]["room"])] = 0

        per_name.append(temp_record[mob_no]["name"])
        per_phone.append(mob_no)
        per_address.append(temp_record[mob_no]["address"])
        per_room.append(temp_record[mob_no]["room"])
        per_check_in.append(temp_record[mob_no]["check_in"])
        per_check_out.append(check_out)
        per_bill.append(total_price)

        del (temp_record[mob_no])

    else:
        print("U have no dues \n Thank you")

    home()


def customer_data():
    data = pd.DataFrame({"names": per_name, "mobile no": per_phone, "address": per_address, "room no": per_room,
                         "check in": per_check_in,
                         "check out": per_check_out, "bill": per_bill})
    print(data)
    home()


home()