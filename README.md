
# Factorial & Fibonacci Project

## 🔄 Working Flow
Start
Repeat continuously:
Display menu:
1 → Factorial
2 → Fibonacci
3 → Exit
Input user choice
If choice = 1:
Input number n
Compute factorial
Display result
Else if choice = 2:
Input number of terms n
Generate Fibonacci sequence
Display sequence
Else if choice = 3:
Exit program
Else:
Display invalid choice
End

## 🧠 Pseudocode
START

WHILE TRUE DO

    DISPLAY "Choose an option:"
    DISPLAY "1. Factorial"
    DISPLAY "2. Fibonacci"
    DISPLAY "3. Exit"

    INPUT choice

    IF choice == 1 THEN
        INPUT n
        SET factorial = 1

        FOR i FROM 1 TO n DO
            factorial = factorial * i
        END FOR

        PRINT factorial

    ELSE IF choice == 2 THEN
        INPUT n
        SET a = 0, b = 1

        FOR i FROM 1 TO n DO
            PRINT a
            SET next = a + b
            SET a = b
            SET b = next
        END FOR

    ELSE IF choice == 3 THEN
        PRINT "Exiting program..."
        BREAK

    ELSE
        PRINT "Invalid choice"

    END IF

END WHILE

END
## 🐍 Python Code
See main.py

## ▶️ How to Run
Run the program using Python.
