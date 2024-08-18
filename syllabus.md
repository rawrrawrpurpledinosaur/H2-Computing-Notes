## H2 Computing Syllabus for lab 

### 1.2.1 Implement sort algorithms
- Bubble sort ✅
- Bubble sort using last exchange index 
- Insertion sort ✅
- Quick sort ✅
- Merge sort 

### 1.2.3 Implement search algorithms
- Linear search ✅
- Binary search ✅
- Hash table search ✅

### 1.3.3 Create, insert and delete operations for stack and queue (linear and ciruclar) 

### 1.3.4 Understand the concept of a free space list

### 1.3.5 Create, update(edit, insert, delete) and serach operations for linear linked list
Exclude: doubly linked list and ciruclar linked list

### 1.3.6 Create, update(edit, insert, delete) and search operations for binary search tree
Exclude: deletion of nodes from binary search tree

### 1.3.7 Understand pre-order, in-order and post-order tree traversal; and application of in-order tree traversal to binary search tree 
pre-order: root, left, right
in-order: left, root, right
post-order: left, right, root

application of in-order traversal: 
- Display all nodes in ascending order (sorted output) 

application of pre-order traversal:
- Copy a tree

application of post-order traversal:
- Deletion of nodes (out of scope)

### 2.1.2 Naming convetions 

### 2.1.3 Write comments 

### 2.2.1 Types: integer, real, char, string, bool, arrays (1d and 2d)

### 2.2.2 Library functions for I/O, string and mathematical operations
``` py
import csv 
with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import json 
with open('file.json', 'r') as f:
    data = json.load(f)
    print(data)
```

### 2.4.1 Explain the difference between data validation and verification 
Data validation: Checks if the data meets specific criteria or rules before it is processed, stored or used.
Done using: 
- range checks
- format check
- lengths check 
- presence check
- check digit

Data verification: Cecks that data has been accurately and correctly transferred, copied or processed. 
- Comparing 2 copies of data to ensure they are identical 
- Cross checking data in a database with original source data

### 2.4.4 Test cases using normal, abnroaml and extreme data or testing and debugging programs

## 2.5 OOP 

### 2.5.2 Understand encapsulation and how classes support information hiding and implementation independence

### 2.5.3 Understand inheritance and how it promotes software reuse

### 2.5.4 Understand polymorphism and how it enables code generalisation
Exclude: method overload and multiple inheritance

### 3.1.2 Write programs to perform the conversion of positive ints between binary, denary and hexadecimal

## 3.3 DBMS

1. Attributes of DB: table, record, field
2. Purpose and use of primary, secondary, composite and foreign keys


