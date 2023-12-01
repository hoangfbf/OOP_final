"""
CPRG 216 N
Instructor: ILES WADE

Assignment: Project: Classes

Date: Nov 30, 2023
Member list:
    Chenyi Lee 
    Jiashuo Xing 
    Khush-Bakht Khan 
    Sinh Hoang Tran 

"""

"""
Program Description:
    The "Jojo's Hair Salon Appointment Management System" is a Python program created to streamline the scheduling process
    for Jojos Hair Salon. The system enables the tracking of customer appointments, offering features such as scheduling,
    cancellation, and viewing of appointments. It provides a user-friendly interface for salon staff to manage appointments
    efficiently.

Inputs:
    - The program prompts the user to input essential information for appointment scheduling, including client name,
      client phone number, type of appointment, day of the week, and start time.
    - Users have the option to load previously booked appointments, providing flexibility in managing existing schedules.
    - Various menu functions such as scheduling, finding appointments, printing calendars, canceling appointments, and exiting
      the system are initiated based on user input.

Processing:
    - The program processes user inputs to create, modify, or cancel appointments within the appointment management system.
    - It utilizes the Appointment class, implemented in Part 1, to handle appointment-related attributes and methods.
    - The Appointment Management Module, developed in Part 2, structures and manages a week's worth of appointments,
      utilizing the Appointment class for data representation.

Outputs:
    - The program outputs a user-friendly display of the appointment system, including one-week calendars with available
      time slots for scheduling.
    - Messages are generated to inform users of successful appointment scheduling, cancellations, or errors in the process.
    - The system displays appointment details, such as client name, phone number, appointment type, day, and start time,
      ensuring clear communication and organization.

Additional Features:
    - The program provides a revenue summary, detailing the number of appointments and total revenue for each appointment type.
    - Users can save and load appointments from a file, enhancing data persistence and facilitating long-term management.

"""



# ANSI color codes for text formatting

RED = "\033[91m"
GREEN = "\033[1;32m"
BLUE = "\033[94m"
RESET = "\033[0m"

class Appointment:
    def __init__(self, day_of_week: str, start_time_hour: int) -> None:
                # Initialize Appointment object with day of the week and start time
        self.__day_of_week = day_of_week.capitalize()          # string INIT
        self.__start_time_hour = start_time_hour  # integer INIT
                                                  # start hour will be in the 24hour format, ie:
                                                  # 9,10,11,12,13,14,15,16 (To keep things simple)

        self.__client_name = ""                  # string DEFAULT
        self.__client_phone = ""                 # string DEFAULT
        self.__appt_type = 0                      # integer DEFAULT
        return

 # Getter and setter methods for client name
    def get_client_name(self) -> str:
        return self.__client_name
    def set_client_name(self, client_name: str) -> None:
        self.__client_name = client_name
        return

# Getter and setter methods for client phone number
    def get_client_phone(self) -> str:
        return self.__client_phone
    def set_client_phone(self, phone_number: str) -> None:
        self.__client_phone = phone_number
        return

    # Getter and setter methods for appointment type
    def get_appt_type(self) -> int:
        return self.__appt_type
    def set_appt_type(self, appt_type: int) -> None:
        self.__appt_type = appt_type
        return

    
    # Method to get a textual description of the appointment type
    def get_appt_type_desc(self) -> str:
        match self.__appt_type:  # appt_type should be integer
            case 0: return "Available"
            case 1: return f"{BLUE}Mens Cut{RESET}"
            case 2: return f"{BLUE}Ladies Cut{RESET}"
            case 3: return f"{BLUE}Mens Colouring{RESET}"
            case 4: return f"{BLUE}Ladies Colouring{RESET}"
            case _: return "Error"

    # Getter and setter methods for the day of the week
    def get_day_of_week(self) -> str:
        return self.__day_of_week
    def set_day_of_week(self, day: str) -> None:  # not sure why this function is required.
        self.__day_of_week = day.capitalize()
        return

    # Getter and setter methods for the start time hour
    def get_start_time_hour(self) -> int:
        return self.__start_time_hour
    def set_start_time_hour(self, start_hour: int) -> None:  # not sure why this function is required.
        self.__start_time_hour = start_hour
        return

    # Method to get the end time hour based on the start time
    def get_end_time_hour(self) -> int:
        return self.__start_time_hour + 1  # follow 24hr format. if Start time = 12, end time will be 12 + 1 = 13

    # Method to schedule an appointment with the provided information
    def schedule(self, name: str, phone: str, app_type: int) -> None:
        self.set_client_name(name)
        self.set_client_phone(phone)
        self.set_appt_type(app_type)
        return

    # Method to cancel an appointment by resetting attributes to default values
    def cancel(self) -> None:
        self.schedule("", "", 0)  # book an appointment with "" and 0, leaving the: day, start_hour untouched.
        return

    # Method to format the appointment information for storage purposes
    def format_record(self) -> str:
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{ self.__start_time_hour}"

    # Method to create a string representation of the appointment for display purposes
    def __str__(self) -> str:
        # Format the appointment information for display, with optional color for booked appointments
        app_string = f"{self.__client_name:<18} {self.__client_phone:<16} {self.__day_of_week:<10} {self.__start_time_hour:>3} - {self.get_end_time_hour():<4} {self.get_appt_type_desc():<30}"
        if self.__appt_type != 0 :
            app_string = f"{BLUE}{app_string}{RESET}"
        return app_string




