# Bane of the theory paper: Pseudocode 

## 1. Style Guide 
- CAPSLOCK for keywords, such as ```IF, REPEAT, PROCEDURE ```
- camelCase for identifiers (variables, functions, etc.) such as ```myVariable, myFunction()```
- Indentation 
- Comment using ```//```

## 2. Nitty Gritty 
### 2.1 Declaring variables 
```DECLARE myVariable: INTEGER ```  
```DECLARE myArray: ARRAY[1:10] OF INTEGER```  
```DECLARE my2DArray: ARRAY[1:10, 1:10] OF INTEGER```  
```CONSTANT myConstant = 69```

### 2.2 Assignment 
```myVariable <- 69```  
```myVariable <- myVariable + 1```

### 2.3 Accessing arrays 
```myArray[1] <- 69```  
```my2DArray[1, 1] <- "*"```

### 2.4 Input/Output (to "console")
```INPUT myVariable```  
```OUTPUT myVariable```  
```OUTPUT "Goodbye World"```


### 2.5 Operations 
1. Arithmetic: ```+, -, *, /```
2. Integer division: ```MOD, DIV```
3. Relational: ```=, <> (not eq), <, >, <=, >=```
4. Logical: ```AND, OR, NOT```

### 2.6 String slicing 
- Must be done using a loop, python style slicing is not allowed

## 3. Control Structures
### 3.1 If 
```
IF <condition> 
  THEN 
    <statements> 
  ELSE
    <statements>
ENDIF 
```

### 3.2 Case 
```
CASE OF myVariable 
  <value1>: <statements>
  OTHERWISE: <statements> 
ENDCASE
```

### 3.3 For loop
```
// Loop on INTEGER
FOR i <- 1 to 10 STEP <increment> (optional, can be negative)
  <statement>
ENDFOR 
// Loop on STRING or ARRAY 
FOR i <- 1 to LENGTH(myString)
  <statement using myString[i]> 
ENDFOR
```

### 3.4 Conditional loops
```
REPEAT 
  <statements>
UNTIL <condition>

WHILE <condition> DO 
  <statements>
ENDWHILE 
```

## 4 Useful stuff
### 4.1 Procedures (does not return anything) 
```
PROCEDURE myProcedure(param1: INTEGER, param2: INTEGER)
  <statements>
ENDPROCEDURE 

CALL myProcedure(1, 2)
```
### 4.2 Function 
```
FUNCTION myFunction(param1: INTEGER, param2: INTEGER) RETURNS INTEGER
  <statements>
  RETURN <something> 
ENDFUNCTION 
```





