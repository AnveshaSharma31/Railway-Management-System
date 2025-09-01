# Railway-Management-System
A Python + MySQL-based Railway Reservation System that allows users to view train details, make reservations, and check booking information. This project simulates a simple railway ticket booking system with a database backend.
✨ Features

📋 View Train Details – Displays all available trains (from the database).
🎫 Make Reservation – Allows users to enter passenger details, generates a unique PNR, and assigns a seat number automatically.
🔍 Check Reservation – Search and display passenger details using a PNR number.
💾 Database Integration – Uses MySQL to store and manage reservation data.

🛠️ Tech Stack
Programming Language: Python
Database: MySQL
Library Used: mysql.connector, random

📂 Database Schema
Database: railway
Table: passenger_details
Column	          |      Type	       |          Description
train_no	            VARCHAR(100)	            Train number
name	                VARCHAR(200)	            Passenger full name
phno	                VARCHAR(100)            	Phone number
age                   VARCHAR(50)	              Passenger age
gender	              VARCHAR(100)	            Gender
from_city	            VARCHAR(100)	            Starting city
to_city	              VARCHAR(200)	            Destination city
date_of_departure	    DATE	                    Departure date
pnr_no	              VARCHAR(100)	            Unique Passenger ID (PNR)
seat_no	              VARCHAR(20)	              Seat number
