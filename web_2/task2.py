import sqlite3

# Function to read and clean the text files
def read_pretty(file): 
    with open(file, 'r') as f:
        data = f.readlines()
        header = data[0].split(',')
        header = [h.strip() for h in header]
        records = []
        for line in data[1:]:
            record = line.split(',')
            record = [r.strip() for r in record]
            records.append(record)
    return header, records

# Connect to the SQLite database
conn = sqlite3.connect("JPFashion.db")
c = conn.cursor()

# Insert data into the customer table
header, data = read_pretty('CUSTOMER.TXT')
c.execute(f"""
    CREATE TABLE IF NOT EXISTS customer (
        Email TEXT PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        ContactNumber TEXT,
        DOB DATE,
        Address TEXT
    )
""")
for row in data:
    c.execute(f"""
    INSERT OR REPLACE INTO customer ({', '.join(header)}) VALUES (?, ?, ?, ?, ?, ?)
    """, tuple(row))

# Insert data into the customer_rental table
header, data = read_pretty('CUSTOMERRENTAL.TXT')
c.execute(f"""
    CREATE TABLE IF NOT EXISTS customer_rental (
        ID INTEGER PRIMARY KEY,
        Email TEXT,
        StartDate DATE,
        EndDate DATE,
        FOREIGN KEY (Email) REFERENCES customer(Email)
    )
""")
for row in data:
    c.execute(f"""
    INSERT OR REPLACE INTO customer_rental ({', '.join(header)}) VALUES (?, ?, ?, ?)
    """, tuple(row))

# Insert data into the product table
header, data = read_pretty('PRODUCT.TXT')
c.execute(f"""
    CREATE TABLE IF NOT EXISTS product (
        CatalogueNumber TEXT PRIMARY KEY,
        Category TEXT,
        Brand TEXT,
        Size TEXT,
        Fee REAL
    )
""")
for row in data:
    c.execute(f"""
    INSERT OR REPLACE INTO product ({', '.join(header)}) VALUES (?, ?, ?, ?, ?)
    """, tuple(row))

# Insert data into the product_rental table
header, data = read_pretty('PRODUCTRENTAL.TXT')
c.execute(f"""
    CREATE TABLE IF NOT EXISTS product_rental (
        ID INTEGER,
        CatalogueNumber TEXT,
        Returned TEXT,
        PRIMARY KEY (ID, CatalogueNumber),
        FOREIGN KEY (ID) REFERENCES customer_rental(ID),
        FOREIGN KEY (CatalogueNumber) REFERENCES product(CatalogueNumber)
    )
""")
for row in data:
    c.execute(f"""
    INSERT OR REPLACE INTO product_rental ({', '.join(header)}) VALUES (?, ?, ?)
    """, tuple(row))

# Commit the changes and close the connection
conn.commit()
conn.close()
