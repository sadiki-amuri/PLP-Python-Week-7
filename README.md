# PLP Academy Python Week 7 Assignment: Working with Lists

This repository covers list manipulation techniques, runtime menu loops, boundary checking, and custom optimization algorithms in Python.

## File Descriptions
* **`list_warmup.py`**: Explores simple positional elements using list indices, mutations via append and remove actions, and matrix structural size checks using `len()`.
* **`shopping_list.py`**: Implements an interactive control flow engine that processes sequential mutations safely against validation constraints.
* **`list_report.py`**: Loops through text collections manually to derive statistical properties and track structural item parameters without built-in shortcut methods.

## Why is it safer to check membership with 'in' before calling '.remove()'?
In Python, calling `.remove()` on an element that is missing instantly triggers a fatal `ValueError` exception and halts execution. Checking membership with the `in` logical parameter acts as a guard rule that enables the engine to handle errors gracefully, skipping modification tasks safely if an entry doesn't exist.
