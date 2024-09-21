import sqlite3

conn = sqlite3.connect("Trip.db")
c = conn.cursor()

c.execute(
    """
CREATE TABLE IF NOT EXISTS Flight(
    FlightNO INT PRIMARY KEY,
    DepartCity TEXT, 
    ArrivalCity TEXT,
    DepartTime TEXT,
    ArrivalTime TEXT
)
        """
)

c.execute(
    """
CREATE TABLE IF NOT EXISTS Customer( 
  CustomerNO INT PRIMARY KEY,
  Name TEXT,
  Gender TEXT,
  DOB TEXT 
)"""
)


c.execute(
    """ 
    CREATE TABLE IF NOT EXISTS Ticket(
      TicketNO INT PRIMARY KEY,
      CustomerNO INT,
      FlightNO INT,
      Date TEXT,
      Seat TEXT,
      FOREIGN KEY (CustomerNO) REFERENCES Customer(CustomerNO),
      FOREIGN KEY (FlightNO) REFERENCES Flight(FlightNO)
    )
    """
)
with open("FLIGHT.txt", "r") as flight:
    for line in flight:
        line = line.strip().split(",")
        c.execute(
            "INSERT INTO Flight(FlightNO, DepartCity, ArrivalCity, DepartTime, ArrivalTime) VALUES (?, ?, ?, ?, ?)",
            (line[0], line[1], line[2], line[3], line[4]),
        )
        print(line)

with open("CUSTOMER.txt", "r") as customer:
    for line in customer:
        line = line.strip().split(",")
        c.execute(
            "INSERT INTO Customer (CustomerNO, Name, Gender, DOB) VALUES (?, ?, ?, ?)",
            (line[0], line[1], line[2], line[3]),
        )
        print(line)

with open("TICKET.txt", "r") as ticket:
    for line in ticket:
        line = line.strip().split(",")
        c.execute(
            "INSERT INTO Ticket (TicketNO, CustomerNO, FlightNO, Date, Seat) VALUES (?, ?, ?, ?, ?)",
            (line[0], line[1], line[2], line[3], line[4]),
        )
        print(line)

conn.commit()
conn.close()
