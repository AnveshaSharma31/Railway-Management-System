import random
import mysql.connector

# Establish connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='anvesha31',
    charset='utf8mb4'
)
cursor = db.cursor()

# Initialize database and table
cursor.execute('CREATE DATABASE IF NOT EXISTS railway')
cursor.execute('USE railway')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passenger_details (
        train_no VARCHAR(100),
        name VARCHAR(200),
        phno VARCHAR(100),
        age VARCHAR(50),
        gender VARCHAR(100),
        from_city VARCHAR(100),
        to_city VARCHAR(200),
        date_of_departure DATE,
        pnr_no VARCHAR(100),
        seat_no VARCHAR(20)
    )
''')

print('*' * 25, 'Welcome to Railway Reservations', '*' * 25)

# Function to show train details
def show_train_details():
    try:
        cursor.execute('SELECT * FROM train_details')
        trains = cursor.fetchall()
        if trains:
            for train in trains:
                print(train)
        else:
            print("No train data found.")
    except Exception as e:
        print("Error fetching train details:", e)

# Function to make reservation
def make_reservation():
    try:
        total = int(input('Enter number of reservations to make: '))
        print('*' * 5, 'Please enter the required information', '*' * 5)

        for _ in range(total):
            train_no = input('Enter train number: ')
            name = input('Enter your full name: ')
            phone = input('Enter your phone number: ')
            age = input('Enter your age: ')
            gender = input('Enter your gender: ')
            from_city = input('Enter the starting city: ')
            to_city = input('Enter your destination: ')
            departure_date = input('Enter departure date (YYYY-MM-DD): ')
            pnr_no = train_no + str(random.randint(100, 999))
            seat_no = str(random.randint(1, 50))

            # Insert record
            cursor.execute('''
                INSERT INTO passenger_details 
                (train_no, name, phno, age, gender, from_city, to_city, date_of_departure, pnr_no, seat_no)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (train_no, name, phone, age, gender, from_city, to_city, departure_date, pnr_no, seat_no))
            db.commit()

            # Print ticket
            print('\n' + '_' * 98)
            print('*' * 35, 'Reservation Confirmed', '*' * 35)
            print(f"Train Number: {train_no} \t PNR Number: {pnr_no}")
            print(f"Name: {name} \t From: {from_city} To: {to_city}")
            print(f"Age: {age} \t Gender: {gender} \t Date: {departure_date}")
            print(f"Phone: {phone} \t Seat No: {seat_no}")
            print('_' * 98)

    except Exception as e:
        print("Error during reservation:", e)

# Function to check reservation details
def check_details():
    try:
        pnr_input = input('Enter your PNR number: ')
        cursor.execute('SELECT * FROM passenger_details WHERE pnr_no = %s', (pnr_input,))
        record = cursor.fetchone()
        if record:
            print('\nReservation Details:')
            print(record)
        else:
            print("No reservation found with that PNR number.")
    except Exception as e:
        print("Error fetching reservation details:", e)

# Main program loop
def main():
    while True:
        print('\n', '*' * 5, 'Menu', '*' * 5)
        print('1. View Train Details')
        print('2. Make a Reservation')
        print('3. Check Reservation Details')
        print('4. Exit')
        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            show_train_details()
        elif choice == '2':
            make_reservation()
        elif choice == '3':
            check_details()
        elif choice == '4':
            print('Thank you for using Railway Reservation System!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
