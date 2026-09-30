# -----------------------------------------------
# Movie Ticket Booking System
# Simple Console VITyarthi Project
# -----------------------------------------------


rows = ["A", "B", "C", "D"]
seats_per_row = 5


def make_seats():
    
    seats = {}
    for r in rows:
        for n in range(1, seats_per_row + 1):
            seats[r + str(n)] = False
    return seats



movies = [
    {"name": "3 Idiots", "time": "10:00 AM", "price": 150, "seats": make_seats()},
    {"name": "Interstellar", "time": "01:30 PM", "price": 200, "seats": make_seats()},
    {"name": "Piku", "time": "06:00 PM", "price": 180, "seats": make_seats()},
]


bookings = []


booking_counter = 101




def get_number(message):
    
    while True:
        text = input(message)
        if text.isdigit():
            return int(text)
        print("Please enter numbers only!")


def count_free_seats(movie):
    
    free = 0
    for booked in movie["seats"].values():
        if booked == False:
            free = free + 1
    return free


def choose_movie():
    
    while True:
        choice = get_number("Enter movie number: ")
        if choice >= 1 and choice <= len(movies):
            return choice - 1
        print("Invalid movie number, try again.")


def calculate_amount(number_of_tickets, price):
    
    return number_of_tickets * price


def find_booking(booking_id):
    
    for b in bookings:
        if b["id"] == booking_id:
            return b
    return None




def show_movies():
    print("\n------------ AVAILABLE MOVIES ------------")
    print("No.  Movie          Time       Price  Free Seats")
    for i in range(len(movies)):
        m = movies[i]
        free = count_free_seats(m)
        print(f"{i + 1:<4} {m['name']:<14} {m['time']:<10} Rs.{m['price']:<4} {free}")


def show_seats(movie):
    print("\nSeats for", movie["name"], "(" + movie["time"] + ")")
    print("-------- SCREEN THIS SIDE --------")
    for r in rows:
        line = ""
        for n in range(1, seats_per_row + 1):
            seat = r + str(n)
            if movie["seats"][seat] == True:
                line = line + "[XX] "      
            else:
                line = line + "[" + seat + "] "   
        print(line)
    print("[XX] = already booked")


def show_booking(b):
    print("\n------------ BOOKING DETAILS ------------")
    print("Booking ID    :", b["id"])
    print("Movie         :", b["movie_name"])
    print("Show time     :", b["time"])
    print("Seats         :", ", ".join(b["seats"]))
    print("No. of tickets:", len(b["seats"]))
    print("Total amount  : Rs.", b["total"])


def book_ticket():
    global booking_counter

    show_movies()
    index = choose_movie()
    movie = movies[index]

    
    if count_free_seats(movie) == 0:
        print("Sorry, this show is housefull!")
        return

    show_seats(movie)

    
    while True:
        text = input("\nEnter seat numbers separated by comma (example A1,A2) or 0 to go back: ")
        if text == "0":
            print("Booking cancelled.")
            return

        chosen = []       
        problem = ""      

        for s in text.split(","):
            s = s.strip().upper()     
            if s == "":
                continue
            if s not in movie["seats"]:
                problem = s + " is not a valid seat."
            elif movie["seats"][s] == True:
                problem = s + " is already booked."
            elif s in chosen:
                problem = s + " was entered twice."
            else:
                chosen.append(s)

        if problem != "":
            print("Error:", problem, "Please try again.")
        elif len(chosen) == 0:
            print("You did not select any seat. Try again.")
        else:
            break   

    total = calculate_amount(len(chosen), movie["price"])


    print("\n------------ BOOKING SUMMARY ------------")
    print("Movie          :", movie["name"])
    print("Seats          :", ", ".join(chosen))
    print("No. of tickets :", len(chosen))
    print("Total amount   : Rs.", total)

    confirm = input("Confirm booking? (y/n): ").lower()
    if confirm != "y":
        print("Booking not done.")
        return


    for s in chosen:
        movie["seats"][s] = True


    booking = {
        "id": booking_counter,
        "movie_index": index,
        "movie_name": movie["name"],
        "time": movie["time"],
        "seats": chosen,
        "total": total,
    }
    bookings.append(booking)
    booking_counter = booking_counter + 1

    print("\nBooking successful! Your booking ID is", booking["id"])


def view_booking():
    if len(bookings) == 0:
        print("\nNo bookings have been made yet.")
        return
    booking_id = get_number("Enter your booking ID: ")
    b = find_booking(booking_id)
    if b == None:
        print("No booking found with this ID.")
    else:
        show_booking(b)


def cancel_booking():
    if len(bookings) == 0:
        print("\nNo bookings to cancel.")
        return
    booking_id = get_number("Enter your booking ID to cancel: ")
    b = find_booking(booking_id)
    if b == None:
        print("No booking found with this ID.")
        return

    show_booking(b)
    confirm = input("Are you sure you want to cancel this booking? (y/n): ").lower()
    if confirm == "y":

        movie = movies[b["movie_index"]]
        for s in b["seats"]:
            movie["seats"][s] = False
        bookings.remove(b)
        print("Booking cancelled. Seats are available again.")
    else:
        print("Cancellation stopped. Your booking is safe.")


def display_seats_menu():
    show_movies()
    index = choose_movie()
    show_seats(movies[index])




def main():
    print("=====================================")
    print("   WELCOME TO MOVIE TICKET BOOKING   ")
    print("=====================================")

    while True:
        print("\n------------- MAIN MENU -------------")
        print("1. Display movies")
        print("2. Display available seats")
        print("3. Book tickets")
        print("4. View booking details")
        print("5. Cancel booking")
        print("6. Exit")

        choice = get_number("Enter your choice (1-6): ")

        if choice == 1:
            show_movies()
        elif choice == 2:
            display_seats_menu()
        elif choice == 3:
            book_ticket()
        elif choice == 4:
            view_booking()
        elif choice == 5:
            cancel_booking()
        elif choice == 6:
            print("\nThank you for using the system. Bye!")
            break
        else:
            print("Please choose a number between 1 and 6.")


main()
