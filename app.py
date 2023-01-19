#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

class Car:
    def __init__(self):
        self.seats = 4
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.seats:
            self.booked_seats += 1
            print("Seat booked successfully!")
        else:
            print("Sorry, all seats are booked.")

car = Car()

while True:
    print("Enter 1 to book a seat, 2 to exit.")
    choice = int(input())
    if choice == 1:
        car.book_seat()
    elif choice == 2:
        break
    else:
        print("Invalid choice, please try again.")
