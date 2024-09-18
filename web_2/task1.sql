-- Create the customer table
CREATE TABLE IF NOT EXISTS customer (
    Email TEXT PRIMARY KEY, 
    FirstName TEXT, 
    LastName TEXT, 
    ContactNumber TEXT, 
    DOB DATE, 
    Address TEXT
);

-- Create the customer_rental table
CREATE TABLE IF NOT EXISTS customer_rental (
    ID INTEGER PRIMARY KEY, 
    Email TEXT,
    StartDate DATE, 
    EndDate DATE,
    FOREIGN KEY (Email) REFERENCES customer(Email)
);

-- Create the product table
CREATE TABLE IF NOT EXISTS product (
    CatalogueNumber TEXT PRIMARY KEY, 
    Category TEXT, 
    Brand TEXT, 
    Size TEXT, 
    Fee REAL
);

-- Create the product_rental table
CREATE TABLE IF NOT EXISTS product_rental (
    ID INTEGER, 
    CatalogueNumber TEXT, 
    Returned TEXT,
    PRIMARY KEY (ID, CatalogueNumber),
    FOREIGN KEY (ID) REFERENCES customer_rental(ID),
    FOREIGN KEY (CatalogueNumber) REFERENCES product(CatalogueNumber)
);
