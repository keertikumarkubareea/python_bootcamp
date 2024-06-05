"""
PyPi - The Python Package Index - install and use published Python packages using the python Package Index
For example - Pretty Table - create tables in ASCII format easily

pip install PrettyTable or PyCharm - settings - Project - Interpreter - {search for desired package}
"""

import prettytable
from prettytable import PrettyTable

table = PrettyTable()
# printing an empty table - no data ASCII table skeleton
print(table)

# Adding columns with related data
# using methods associated with the 'table' object
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

# Tapping into the object's attribute called 'align'
table.align = "r"  # Can be r for right alignment, l for left or c for center
print(table)



