CREATE DATABASE Trip;


CREATE TABLE IF NOT EXISTS Flight(
    FlightNO INT PRIMARY KEY,
    DepartCity TEXT, 
    ArrivalCity TEXT,
    DepartTime TEXT,
    ArrivalTime TEXT,
)

CREATE TABLE IF NOT EXISTS Customer( 
  CustomerNO INT PRIMARY KEY,
  Name TEXT,
  Gender TEXT,
  DOB TEXT, 
)

CREATE TABLE IF NOT EXISTS Ticket(
  TicketNO INT PRIMARY KEY,
  CustomerNO INT FOREIGN KEY REFERENCES Customer(CustomerNO),
  FlightNO INT FOREIGN KEY REFERENCES Flight(FlightNO),
  Date TEXT, 
  Seat TEXT,
)


