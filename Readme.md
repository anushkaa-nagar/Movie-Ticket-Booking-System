# Movie Ticket Booking System

A simple console-based movie ticket booking system written in Python.
Made as a first-semester project.

## Features
- Display movies (name, show time, price, free seats)
- Display seat layout (free seats and booked seats)
- Book one or more tickets (double booking is blocked)
- Automatic total amount calculation and booking summary
- View booking details using booking ID
- Cancel a booking with confirmation (seats become free again)
- Menu-driven, keeps running until Exit
- Basic input validation

## How to Run
1. Install Python 3 from https://www.python.org
2. Put `Code.py` in a folder.
3. Open a terminal / command prompt in that folder and run:

```
python Code.py
```

(On some systems use `python3 Code.py`.)

## How to Use
| Menu option | What it does |
|---|---|
| 1 | Shows all movies with time, price and free seats |
| 2 | Shows the seat layout of a movie you choose |
| 3 | Books tickets: pick a movie, type seats like `A1,A2`, confirm |
| 4 | Shows booking details for a booking ID |
| 5 | Cancels a booking using its ID |
| 6 | Exits the program |

Seats are named by row and number (A1 to D5). `[XX]` means the seat is already booked.
Booking IDs start from 101.

## Project Structure
```
Movie_Ticket_Booking_Project/
|-- Code.py            (source code)
|-- Readme.md          (this file)
|-- Statement.md       (problem statement)
|-- Project_Report.docx (project report)
|-- Screenshots/       (output screenshots)
```

## Concepts Used
Variables, lists, dictionaries, functions, loops, if/elif/else, string methods,
input validation, and basic input/output.

## Limitations
- Bookings are lost when the program is closed (no file or database).
- Only three sample movies and 20 seats per show.

## Future Improvements
- Save bookings in a file
- Store customer name and phone number
- Different prices for different rows
- Admin option to add new movies
