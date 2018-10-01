import time
import datetime
import json

class Pool_Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.status = "NOT OCCUPIED"
        self.start_rent_time = "00:00:00"
        self.stop_rent_time = "00:00:00"
        self.total_time_rented_seconds = 0
        self.total_time_rented_minutes = 0
        self.total_time_rented_hours = 0
        self.cost = 0

pool_tables = []
pool_tables_summary =[]

table_number = 0
for index in range(0,12):
    table_number += 1
    pool_table = Pool_Table(table_number)
    pool_tables.append(pool_table)

def print_tables():
    for index in range(len(pool_tables)):
        print (f'{pool_tables[index].table_number}. Table {pool_tables[index].table_number} \n               Status: {pool_tables[index].status}    Rent Time Start: {pool_tables[index].start_rent_time}    Rent Time End: {pool_tables[index].stop_rent_time}    Total Time Rented: {pool_tables[index].total_time_rented_hours}h {pool_tables[index].total_time_rented_minutes}m {pool_tables[index].total_time_rented_seconds}s    Total Rental Cost: ${pool_tables[index].cost}\n')

def start_rent_table():
    while True:
        try:
            ask_table = int(input('\nEnter table number: '))
            if 1 <= ask_table <= len(pool_tables):
                if pool_tables[ask_table - 1].table_number == ask_table:
                    ask_table = (ask_table - 1) 
                    if pool_tables[ask_table].status != "OCCUPIED":
                        pool_tables[ask_table].status = "OCCUPIED"
                        ts = time.time()
                        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        pool_tables[ask_table].start_rent_time = st
                        break
                    else:
                        print(f'\nERROR:  Pool Table {pool_tables[ask_table].table_number} is currently occupied') 
            else:
                print(f'\nERROR: Enter a number between 1 and {len(pool_tables)}\n')
        except ValueError:
            print(f'\nERROR: Enter a number between 1 and {len(pool_tables)}\n')

def stop_rent_table():
    while True:
        try:
            ask_table = int(input('\nEnter table number: '))
            if 1 <= ask_table <= len(pool_tables):
                if pool_tables[ask_table - 1].table_number == ask_table: 
                    ask_table = (ask_table - 1)
                    if pool_tables[ask_table].status != "NOT OCCUPIED":
                        pool_tables[ask_table].status = "NOT OCCUPIED" 
                        ts = time.time()
                        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        pool_tables[ask_table].stop_rent_time = st
                        stop_time = pool_tables[ask_table].stop_rent_time.replace(":","")
                        start_time = pool_tables[ask_table].start_rent_time.replace(':',"")
                        stop_minutes_rented = (int((stop_time[0:2]) * 60)) + (int((stop_time[2:4])))
                        stop_seconds_rented = ((stop_minutes_rented * 60) + (int((stop_time[4:6]))))
                        start_minutes_rented = ((int((start_time[0:2]) * 60)) + (int((start_time[2:4]))))
                        start_seconds_rented = ((start_minutes_rented * 60) + (int((start_time[4:6]))))
                        seconds_rented = (stop_seconds_rented - start_seconds_rented)
                        minutes_rented = (seconds_rented // 60)
                        hours_rented = (seconds_rented // 3600)
                        seconds_rented = (seconds_rented % 60)
                        pool_tables[ask_table].total_time_rented_seconds += seconds_rented
                        pool_tables[ask_table].total_time_rented_minutes += minutes_rented
                        pool_tables[ask_table].total_time_rented_hours += hours_rented
                        if hours_rented == 0:
                            cost = 30
                        elif hours_rented > 0 and minutes_rented > 0:
                            cost = (hours_rented * 30) + 30
                        elif hours_rented > 0 and minutes_rented == 0:
                            cost = (hours_rented * 30)
                        pool_tables[ask_table].cost += cost
                        pool_tables_summary.append(f'Table: {pool_tables[ask_table].table_number} Rental Start Time: {pool_tables[ask_table].start_rent_time} Rental End Time: {pool_tables[ask_table].stop_rent_time} Total Time Rented: {pool_tables[ask_table].total_time_rented_hours}h {pool_tables[ask_table].total_time_rented_minutes}m {pool_tables[ask_table].total_time_rented_seconds}s Rental Cost: {pool_tables[ask_table].cost}')
                        break
                    else:
                        print(f'\nERROR:  Pool Table {pool_tables[ask_table].table_number} is currently unoccupied.')       
            else:
                print(f'\nERROR: Enter a number between 1 and {len(pool_tables)}\n')
        except ValueError:
            print(f'\nERROR: Enter a number between 1 and {len(pool_tables)}\n')

def menu():
    while True:
        try:  
            menu = int(input('\n******** Pool Table App Menu *********\n\n1. Press 1 to rent table\n2. Press 2 to stop renting table\n3. Press 3 to view current table status\n4. Press 4 to quit and submit report\n\nEnter your choice: '))
            if menu == 1:
                print ('\n\nWhat table would you like to occupy?\n')
                print_tables()
                start_rent_table()
            elif menu == 2:
                print ('\n\nWhat table are you unoccupying?\n')
                print_tables()
                stop_rent_table()
            elif menu == 3:
                print ('\n\nCurrent Table Status\n')
                print_tables()
            elif menu == 4:
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%Y')
                file_name = st + ".json"
                with open(file_name,"w") as file_object:
                    json.dump(pool_tables_summary,file_object)
                break
            else: 
                print('\nERROR: Please enter a number between 1 and 4.\n')
        except ValueError:
            print('\nERROR:  Please enter a number between 1 and 4.\n')

menu()

print('\nThank you for using the pool table app\n')
                
                
    
