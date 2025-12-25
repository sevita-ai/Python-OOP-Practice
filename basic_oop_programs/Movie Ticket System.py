class Movie:
    def __init__ (self, name,total_seats):
        self.name = name
        self.total_seats = total_seats
        self.available_seats = total_seats #When movie starts all the seats are available so no need to pass the no.of available seats separately
    def book_ticket (self,count):
        if count <= 0:
            return "Invalid input no.of seats!"
        if count <=self.available_seats:
            self.available_seats -= count
            return f"{count} tickets booked successfully"
        else:
            return "Insufficient no.of seats"
    def cancel_ticket (self,count):
        if count <= 0:
            return "Invalid input"
        if self.available_seats + count < self.total_seats:
            self.available_seats += count
            return f"{count} tickets cancelled successfully"
        else:
            return "Cannot cancel more no.of tickets than booked"
    def show_available_seats (self):
        return self.available_seats
movie = Movie("Hi Nanna",100)
print(movie.book_ticket(3))
print(movie.cancel_ticket(1))
print(movie.book_ticket(99))
print(movie.show_available_seats())
