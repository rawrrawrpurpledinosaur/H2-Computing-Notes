import sqlite3

conn = sqlite3.connect("Trip.db")
c = conn.cursor()

# update flight data
c.execute(
    """
    UPDATE Flight 
    SET DepartTime = '1815', ArrivalTime = '0015' 
    WHERE FlightNO = 'TR808'
    """
)

conn.commit()

print("Flights departing from Singapore: ")
query = c.execute(
    "SELECT * FROM Flight WHERE DepartCity = 'Singapore' ORDER BY DepartTime"
).fetchall()
for r in query:
    print(r)

# delete ticket number 1023 1024
print("Cancelling tickets 1023 and 1024")
c.execute("DELETE FROM Ticket WHERE TicketNo IN ('1023', '1024')")
