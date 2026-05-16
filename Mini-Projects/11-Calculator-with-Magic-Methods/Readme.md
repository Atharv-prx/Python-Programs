# Advanced Calculator Using Magic Methods

Built as part of my Python learning journey.
A console-based calculator project.

# Features

## Arithmetic Operations
- Addition, Subtraction
- Multiplication, Division
- Power calculations

## Comparison Operations
- Equal to (`==`)
- Greater than (`>`)
- Less than (`<`)

## Unary Operations
- Negative values
- Absolute values

## In-Place Operations
- `+=`
- `-=`
- `*=`
- `/=`

## Validation System
- Type validation using `isinstance()`
- Zero division prevention
- Safe user input handling

## User Interactive System
- Menu driven calculator
- Continuous loop system
- Input validation helper functions

## History System
- Stores all calculations performed during runtime
- Displays previous operations and results

# Concepts Practiced

This project helped practice and understand:

- Object-Oriented Programming (OOP)
- Magic Methods / Dunder Methods
- Operator Overloading
- Helper Methods
- Abstraction
- Input Validation
- Exception Handling
- Boolean Comparisons
- In-place Operators
- Program State Management

# Magic Methods Used

| Magic Method | Purpose |
|---|---|
| `__add__` | Addition |
| `__sub__` | Subtraction |
| `__mul__` | Multiplication |
| `__truediv__` | Division |
| `__pow__` | Power |
| `__neg__` | Negative object |
| `__abs__` | Absolute value |
| `__eq__` | Equality comparison |
| `__lt__` | Less than comparison |
| `__gt__` | Greater than comparison |
| `__iadd__` | In-place addition |
| `__isub__` | In-place subtraction |
| `__imul__` | In-place multiplication |
| `__itruediv__` | In-place division |
| `__str__` | User-friendly string output |
| `__repr__` | Developer/debug representation |

# Version History

## Version 1
- Basic calculator class
- Simple arithmetic magic methods
- Basic object interaction

## Version 2
- Added more magic methods
- Added comparison operators
- Added unary operators
- Added `__str__` and `__repr__`

## Version 3
- Added validation system
- Added helper function `_get_value()`
- Added support for integers and floats
- Added in-place operators (`+=`, `-=`, etc.)

## Version 4
- Added user interaction
- Added menu system
- Added helper functions for validated input
- Added exception handling

## Version 5 (Current)
- Added calculation history system
- Added persistent runtime memory using lists
- Improved overall structure and readability

---

# Improvements to be done by future me

- Scientific calculator features
- Square roots and logarithms
- Trigonometric functions
- Save history to file
- GUI version using Tkinter or PyQt
- Memory system (M+, M-, MR, MC)
- Decimal precision settings
- Expression parsing

---