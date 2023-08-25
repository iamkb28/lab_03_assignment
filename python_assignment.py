class Process:
    def __init__(self, p_id, process_name, start_time, priority):
        self.p_id = p_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_p_id(self):
        self.processes.sort(key=lambda process: process.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)

    def sort_by_priority(self):
        priority_order = {"Low": 1, "MID": 2, "High": 3}
        self.processes.sort(key=lambda process: priority_order[process.priority])

    def print_table(self):
        print("P_ID   Process     Start Time  Priority")
        print("---------------------------------------")
        for process in self.processes:
            print(f"{process.p_id}   {process.process_name}    {process.start_time}          {process.priority}")

# Creating instances of Process
processes = [
    Process("P1", "VSCode", 100, "MID"),
    Process("P23", "Eclipse", 234, "MID"),
    Process("P93", "Chrome", 189, "High"),
    Process("P42", "JDK", 9, "High"),
    Process("P9", "CMD", 7, "High"),
    Process("P87", "NotePad", 23, "Low"),
]

# Creating FlightTable instance and adding processes
flight_table = FlightTable()
for process in processes:
    flight_table.add_process(process)

# User input for sorting parameter
print("Sort Options:")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
print("3. Sort by Priority")
choice = int(input("Enter your choice: "))

# Sorting and printing the table based on user choice
if choice == 1:
    flight_table.sort_by_p_id()
elif choice == 2:
    flight_table.sort_by_start_time()
elif choice == 3:
    flight_table.sort_by_priority()

flight_table.print_table()