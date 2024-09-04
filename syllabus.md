## H2 Computing Syllabus

## 1.1 Algorithmic Representation 
[comment]: Refer to Introduction.pdf (add link)
Refer to [Introduction](https://github.com/rawrrawrpurpledinosaur/revision_py_files/static/Introduction.pdf)

## 1.2 Fundamental Algorithms <a name="1.2"></a>
### 1.2.1 Implement sort [algorithms](https://github.com/rawrrawrpurpledinosaur/revision_py_files/blob/main/algorithms/sorting.py)
- Bubble sort 
- Bubble sort using last exchange index 
- Insertion sort  
- Quick sort 
- Merge sort 

### 1.2.3 Implement search [algorithms](https://github.com/rawrrawrpurpledinosaur/revision_py_files/blob/main/algorithms/searching.py)
- Linear search 
- Binary search 
- Hash table search 

### 1.2.2 & 1.2.4 Use examples to explain sort and search alogrithms

### 1.2.5 Compare and describe the efficiencies of the sort and search algorithms using Big-O notation for time complexity (worst case)
<!Generate a table of time complexities>
| Algorithm | Time Complexity (worst case) | Space Complexity (Not tested) |
|-----------|------------------------------|--------------------------------|
| Bubble sort | O(n^2) | O(1) |
| Bubble sort using last exchange index | O(n^2) | O(1) |
| Insertion sort | O(n^2) | O(1) |
| Quick sort | O(n^2) | O(log n) |
| Merge sort | O(n log n) | O(n) |

## 1.3 Data Structures <a name="1.3"></a>

### 1.3.1 - 1.3.2 Understand the concept of static and dynamic allocation of memory 
Static allocation: Memory is allocated before the program runs (compile time). Therefore, size and type of memory must be known in advance.
Dynamic allocation: Memory is allocated at runtime as needed.

### 1.3.3 Create, insert and delete operations for [stack](https://github.com/rawrrawrpurpledinosaur/revision_py_files/blob/main/data_structures/stack.py) and [queue](https://github.com/rawrrawrpurpledinosaur/revision_py_files/blob/main/data_structures/queue.py) (linear and ciruclar) 

### 1.3.4 Understand the concept of a free space list
Free space list: A list of memory locations that are not in use and are available for allocation.

### 1.3.5 Create, update(edit, insert, delete) and serach operations for [linear linked list](https://github.com/rawrrawrpurpledinosaur/revision_py_files/blob/main/data_structures/linkedlist.py)
Exclude: doubly linked list and ciruclar linked list

### 1.3.6 Create, update(edit, insert, delete) and search operations for binary search tree
Exclude: deletion of nodes from [binary search tree](https://github.com/rawrrawrpurpledinosaur/revision_py_files/blob/main/data_structures/tree.py)

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

## 2.1 Coding Standards
### 2.1.1 - 2.1.3 
<li> Use Indentation and white space </li>
<li> Use naming conventions </li>
<li> Write comments </li>

### 2.2.1 Types: integer, real, char, string, Boolean, arrays (1d and 2d)

### 2.2.2 Library functions for I/O, string (concatenation and slicing) and mathematical operations (+-*/%**)
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
### 2.2.5 Understand the concept of recursion
```py 
def factorial(n):
    if n == 0: # Base case 
        return 1
    else:
        return n * factorial(n-1) # Call itself
```

### 2.2.6 Trace the steps and list results of recursive and non-recursive programs
Example for above function, where n = 4:
| n | factorial(n) |
|---|--------------|
| 4 | 4 * factorial(3) |
| 3 | 3 * factorial(2) |
| 2 | 2 * factorial(1) |
| 1 | 1 * factorial(0) |
| 0 | 1 |

### 2.2.7 Understand the use of stacks in recursive programming
The result of each recursive call is stored in a stack frame (which stores data necessary to execute the recursive function) until the base case is reached. The results are then popped off the stack frame and returned. </br>
Refer to above table, when n = 0, factorial(0) = 1. This result is popped off the stack frame and returned to the previous call, where n = 1.


## 2.3 Implementing Algorithms and Data Structures
Literally everything in [1.2](#"1.2") and [1.3](#"1.3")

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
