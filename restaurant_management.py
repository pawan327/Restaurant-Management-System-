import random

class Table:
    def _init_(self, location, number_of_sits):
        self.location = location
        self.number_of_sits = number_of_sits
        self.is_reserved = False
        self.time = None
    
    def reserve(self, time):
        self.is_reserved = True
        self.time = time
    
class Restaurant:
    def _init_(self, number_of_tables):
        self.number_of_tables = number_of_tables
        self.tables = self._create_tables()

    def _create_tables(self):
        tables = dict()
        for table_num in range(1, self.number_of_tables + 1):
            location = f"location {table_num}"
            number_of_sits = random.choice([2,4,6])
            tables[table_num] = Table(location, number_of_sits)
        return tables
    
    def filter_by_size_equal_to(self, size):
        filtered_table_result = []
        for table in self.tables.values():
            if table.number_of_sits == size:
                filtered_table_result.append(table)
        return filtered_table_result

    def filter_by_time_period(self, start_time, end_time):
        filtered_table_result = []
        for table in self.tables.values():
            if table.time:
                if table.time >= start_time and table.time <= end_time:
                    filtered_table_result.append(table)
        return filtered_table_result
        

    def reserve_table(self, table_num, time):
        table = self.tables[table_num]
        table.reserve(time)
        self.tables[table_num] = table
        return table


def book_table(tables):
    for table in tables:
        print(f"{table.location}")
    table_num = int(input("Please enter table number to book a table : "))
    time = input("Please enter time in hh:mm format : ")
    return table_num, time

def reservation_form(restaurant):
    print("RESTAURANT MANAGEMENT SYSTEM")
    print("Main Screen")
    action = int(input("Press 1 , to book tables ,\n or press 2 to filter tables [press 0 to EXIT ] : "))
    if action == 1:
        table_num, time = book_table(restaurant.tables.items())
        table = restaurant.reserve_table(table_num, time)
        print(f"Table {table.location} is booked for {table.time}")
    elif action == 2:
        print('Filter Menu')
        print(' 1 - Filter by size')
        print(' 2 - Filter by reservation period')
        filter_action = int(input("Enter your choice [press 0 to EXIT ] : "))
        if filter_action == 1:
            size = int(input('Enter the size of tables [2,4,6] : '))
            tables = restaurant.filter_by_size_equal_to(size)
            table_num, time = book_table(tables)
            table = restaurant.reserve_table(table_num, time)
            print(f"Table {table.location} is booked for {table.time}")
        elif filter_action == 2:
            period = input("Enter time period in this format HH:MM - HH:MM \n -> ")
            try:
                start_time, end_time = period.split("-")            
                start_time, end_time = start_time.strip(), end_time.strip()
            except Exception:
                print("Wrong format of time period . Exiting !!")
            tables = restaurant.filter_by_time_period(start_time, end_time)
            table_num, time = book_table(tables)
            table = restaurant.reserve_table(table_num, time)
            print(f"Table {table.location} is booked for {table.time}")
        


restaurant = Restaurant()

reservation_form(restaurant)