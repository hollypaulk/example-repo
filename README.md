Shoe Inventory Management System

Overview: 

The Shoe Inventory Management System is a Python application that allows users to manage and maintain shoe inventory records. The program reads inventory data from a text file, stores the information as objects, and provides a menu-driven interface for viewing, searching, updating, and analyzing stock levels.

The application uses Object-Oriented Programming (OOP) principles through a Shoe class, making the code organized, reusable, and easy to maintain.

Features: 

•	Load shoe inventory data from an external inventory.txt file.
•	View all shoes currently stored in the inventory.
•	Add new shoe records to the inventory.
•	Search for a shoe using its unique product code.
•	Identify the shoe with the lowest stock quantity and restock it.
•	Calculate and display the total value of each inventory item.
•	Identify the shoe with the highest stock quantity and mark it as available for sale.
•	Automatically save inventory updates back to the inventory.txt file.
•	Error handling for invalid user input and missing files.

Technologies Used: 

•	Python 3

File Structure:

•	inventory.txt
•	inventory.py

File Format for Inventory File “inventory.txt”:

country,code,product,cost,quantity
South Africa,SKU44386,Air Max 90,2300.0,20
China,SKU90000,Jordan 1,3200.0,50
Vietnam,SKU63221,Blazer,1700.0,19

How to Run:

1.	Ensure Python 3 is installed on your computer.
2.	Place the inventory.txt file in the same directory as the Python script.
3.	Open a terminal or command prompt.
4.	Navigate to the project folder.
5.	Run the program: python inventory.py

Menu Options:

1.	View all shoes
2.	Add new shoe
3.	Search shoe by code
4.	Restock lowest quantity shoe
5.	View value per shoe
6.	View highest quantity (FOR SALE)
7.	Exit

Author: 
Developed as a Python inventory management project to demonstrate OOP, file handling, and data management techniques.
