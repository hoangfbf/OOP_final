from appointment import *


#============================================================================================================
# This method/function creates the structure you defined above and prepopulates the
# structure with a new (and available) appointment for each hour (9:00am to 4:0pm)
# of each day (Monday to Saturday).   The method returns the prepopulated calendar structure.

# We will use a FLAT LIST to represent the weekly calendar structure:

BUSINESS_DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
BUSINESS_HOURS = (9, 10, 11, 12, 13, 14, 15, 16)
RED = "\033[91m"
RESET = "\033[0m"

def create_weekly_calendar() :
    weekly_calendar = []

    for day in BUSINESS_DAYS:
        for hour in BUSINESS_HOURS:
            appointment = Appointment(day, hour)
            weekly_calendar.append(appointment)

    return weekly_calendar  # return a Flat List of Appointment Objects

# =============================================================================================
# This method returns an appointment object corresponding to the provided day and time from
# within the calendarStructure.
def find_appointment_by_daytime (weekly_calendar, day: str, start_hour: int) -> Appointment:
    for an_appointment in weekly_calendar:
        if (an_appointment.get_day_of_week() == day) and (an_appointment.get_start_time_hour() == start_hour):
            return an_appointment
    print ("Error: cannot find such appointment") # for error checking.

# ===============================================================================
# This method returns a LIST of appointment objects corresponding to the provided day
# from within the calendarStructure.
def find_appointment_by_day (weekly_calendar, day):
    day_calendar = []
    for an_appointment in weekly_calendar:
        if an_appointment.get_day_of_week() == day:
            day_calendar.append(an_appointment)
    return day_calendar
#==========================================================================
#=================Helper Function: not required:
# this function will take in a list of Appoinment Objects and neatly print out
# all appointment objects in that list
def print_appointment_list(a_list: list[Appointment]) -> None:
    for appointment in a_list:
        print(appointment)
    pass


#===============================================================================
#  This method returns a LIST of appointment objects by scanning the entire calendarStrucutre
# for matches for the name of the customer. Matches are NOT case-sensitive, and can be partial
#  (“sal” will match “Sally”)
def find_appointment_by_name(weekly_calendar, name):
    appointment_list_by_name = []
    for an_appointment in weekly_calendar:
        client_name = an_appointment.get_client_name()  # get the client name
        if name.lower() in client_name.lower():
            appointment_list_by_name.append(an_appointment)

    return appointment_list_by_name

#===============================================================================================
# This method loads the calendar items from a text file and returns a populated calendar structure
# (similar to the create_weekly_calendar()). If a block of time is not in the file, the calendar
# will show that the period as available
# ASSUMPTION: the FILE is in the correct format: (eg: “Harvey,403-233-3944,1,Saturday,09”)
# any LINE that does not follow the format may be ignored.
def load_scheduled_appointments(filename) -> list[Appointment]:
    a_weekly_calendar = create_weekly_calendar()

    try:
        with open(filename, 'r') as file:
            for a_line in file:  # Iterate over each line in the file, each line is a string like:
                                # Stephanie,368-999-1111,2,Saturday,10
                #===== process a customer appointment =========================
                a_line = a_line.strip()  # trim a line for process

                result_list = a_line.split(',')  # split items of a line into a list in  the form:
                                                 # [Stephanie,368-999-1111,2,Saturday,10]
                                                 # and will operate on the string elements of the list

                name = result_list[0]                          # extrac client name into STRING
                phone = result_list[1]                         # extract phone into STRING
                appt_type_int = int(result_list[2])            # extract appt type in the form INT
                day_of_week = result_list[3]                   # extract day of week into STRING
                start_hour_int = int(result_list[4])           # extract start hour into INT

                # at this line should have a customer information as well as
                # their appointment information ready to process:
                match_appointment = find_appointment_by_daytime(a_weekly_calendar, day_of_week, start_hour_int)
                match_appointment.schedule(name, phone, appt_type_int)

            print(f"Successfully loaded data from {filename}")
                #============= end process a cusstomer appoinment
    except Exception as e:
        print(f"An error occurred: {e}")

    return a_weekly_calendar


# a_week = load_scheduled_appointments("appointments1.csv")

#=========================================================
def save_scheduled_appointments(weekly_calender, filename):
    string_to_write = ""

    for appointment in weekly_calender:
        if appointment.get_appt_type() != 0:
            a_string = appointment.format_record()
            string_to_write += a_string + "\n"

    with open(filename, 'w') as file:
        file.write(string_to_write)
        print(f"Successfully written data to {filename}")

    pass
# ================================

#==================== BUILDING A MENU=======================

# This function get_int_choice_from_menu takes in a STRING represent a menu and an INTEGER that represent the range of
# the valid choices. It will loop, show the given menu, ask user for input until the user enter a valid integer that is
# within the range from 1 up to the given Integer.
# For example, when given a Main_menu and an integer 5, the function will loop and keep asking the user for
# the input, show the user the Main_menu, until the user enter an integer number that is one of : 1,2,3,4,5.
# the function will always return an INTEGER, in the range from 1 to max_choice, inclusive.
# this is a helper function that is not required:
def get_int_choice_from_menu(menu: str, max_choice: int) -> int:
    while True:
        user_input: str = input(menu)
        if user_input.isdigit() and (int(user_input) in range(1, max_choice+1)):
            return int(user_input)
        print(f"{RED}*****ERROR**** You entered '{user_input}', which is not a valid choice. Try again{RESET}")

#=====================================================
MAIN_MENU = """=======================================================================

WELCOME TO OUT APPOINTMENT PROGRAM, SELECT FROM ONE OF THE FOLLOWING:
1.  Add Appointment 
2.  Remove Appointment 
3.  Save Appointments 
4.  Load Appointments
5.  Show Appointments by Day 
6.  Show Appointments by Name 
7.  Show Revenue 
8.  Quit
(Input Must be from 1->8). Your Input: """
MAX_CHOICE_MAIN_MENU = 8

# This function will loop the main MENU until user provide a VALID input
# The function then stop the loop, and return the VALID INPUT.
def get_menu_selection() -> int:
    user_choice = get_int_choice_from_menu(MAIN_MENU, MAX_CHOICE_MAIN_MENU)
    return user_choice
#=======================================================
# Just a basic get file name, no special requirement.

def get_filename() -> str:
    return input("Please enter a file name: ")

#=================================================

MENU_DAY = """>>>>>>> PLEASE SELECT A VALID DAY for your appointment <<<<<<<
1 for "Monday"
2 for "Tuesday" 
3 for "Wednesday"
4 for "Thursday"
5 for "Friday"
6 for "Saturday"
Your Input MUST BE FROM 1 to 6, Your Input: """
MAX_CHOICE_MENU_DAY = 6
# This method displays a list of days and allows the user to select a day.
# The function returns only when user enters a valid entry.
# This function return a String that represent the day.
def get_day() -> str:
    int_user_choice: int = get_int_choice_from_menu(MENU_DAY, MAX_CHOICE_MENU_DAY)
    match int_user_choice:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"

#=====================================================================

MENU_TIME_HOUR = """>>>>>>> PLEASE ENTER A VALID APPOINTMENT START HOUR <<<<<<
1 for 9:00-10:00, 
2 for 10:00-11:00, 
3 for 11:00-12:00, 
4 for 12:00-1:00, 
5 for 13-00-14:00 (1:00-2:00), 
6 for 14:00-15:00 (2:00-3:00, 
7 for 15:00-16:00 (3:00-4:00, 
8 for 16:00-17:00 (4:00-5:00,
Input must be from 1 to 8 (inclusive). Your input: """
MAX_CHOICES_MENU_HOUR = 8
# This function ask user for a valid time input.
# This function will return an integer between 9 --> 16
def get_time() -> int:
    user_choice = get_int_choice_from_menu(MENU_TIME_HOUR, MAX_CHOICES_MENU_HOUR)

    start_hour = user_choice + 8  # convert user_choice to the actual starting hour:
                                  # for example, if user entered 2, that means the start hour is 2 + 8 = 10
                                  #              if user entered 5, that means the start hour is 5 + 8 = 13
                                  # we are using 24-hour format.
    return start_hour

#===============================================
MENU_SERVICE_TYPE = """>>>>>> Please select type of appointment <<<<<<
1.	Mens cut $50
2.	Ladies cut $80
3.	Mens Colouring $50
4.	Ladies Colouring $120
Your input: """
MAX_CHOICE_SERVICE_TYPE = 4

def get_service_type() -> int:
    user_choice = get_int_choice_from_menu(MENU_SERVICE_TYPE, MAX_CHOICE_SERVICE_TYPE)
    return user_choice

#+==================================================

MENU_INIT = """
Would you like to load schedule from a file? 
Press y to load schedule from a file. You will be prompted a file name. 
Press any other key and/or Enter will skip this step, the program will build an empty database.
Your input: """

MENU_BEFORE_QUIT = """
Would you like to save current schedule to a file before quiting? 
Press y and Enter to save current schedule to a file. You will be prompted a file name to save your data.
Press any other key and/or Enter will exit the program without saving. 
Your input: """

#===========================================

def get_phone() -> str:
    return input("Please enter the phone number: ")

def get_name() -> str:
    return input("Please enter the name: ")

#======================================
# === This function takes in the database( which is a flat list of appointments,
# then it calculate and show a detailed revenuew reports.

MEN_CUT_UNIT_PRICE = 50
LADY_CUT_UNIT_PRICE = 80
MEN_COLOR_UNIT_PRICE = 50
LADY_COLOR_UNIT_PRICE = 120


def show_revenue(database: list[Appointment]) -> None:
    men_cut_counter, men_cut_revenue = 0, 0
    lady_cut_counter, lady_cut_revenue = 0, 0
    men_color_counter, men_color_revenue = 0, 0
    lady_color_counter, lady_color_revenue = 0, 0

    for an_appointment in database:
        match an_appointment.get_appt_type():
            case 1:
                men_cut_counter += 1
            case 2:
                lady_cut_counter += 1
            case 3:
                men_color_counter += 1
            case 4:
                lady_color_counter += 1

    # AT this step, should have the number of orders for each service type ready:

    men_cut_revenue = men_cut_counter * MEN_CUT_UNIT_PRICE
    lady_cut_revenue = lady_cut_counter * LADY_CUT_UNIT_PRICE
    men_color_revenue = men_color_counter * MEN_COLOR_UNIT_PRICE
    lady_color_revenue = lady_color_counter * LADY_COLOR_UNIT_PRICE

    total_orders = men_cut_counter + lady_cut_counter + men_color_counter + lady_color_counter
    total_revenue = men_cut_revenue + lady_cut_revenue + men_color_revenue + lady_color_revenue

    print("================================REPORT =========================================")

    print(f"{'Type':<6} {'Description':<20} {'Appointments':>20} {'Revenue':>15}")
    print("----------------------------------------------------------------")
    print(f"{'1':<6} {'Mens Cut':<20} {men_cut_counter:>20} {men_cut_revenue:>15.2f}")
    print(f"{'2':<6} {'Ladies Cut':<20} {lady_cut_counter:>20} {lady_cut_revenue:>15.2f}")
    print(f"{'3':<6} {'Mens Colouring':<20} {men_color_counter:>20} {men_color_revenue:>15.2f}")
    print(f"{'4':<6} {'Ladies Colouring':<20} {lady_color_counter:>20} {lady_color_revenue:>15.2f}")
    print("----------------------------------------------------------------")
    print(f"Total{total_orders:>43} {total_revenue:>15.2f}")

    pass

#=================================================

SERVICE_TYPE_DICTIONARY = {
    1: "Mens Cut",
    2: "Ladies Cut",
    3: "Mens Colouring",
    4: "Ladies Colouring"
}

def main():
    current_database = create_weekly_calendar()    # a flat list of Appointments Available and Booked

    # Ask user if they want to load from file
    match input(MENU_INIT).lower():
        case "y":
            filename = get_filename()
            current_database = load_scheduled_appointments(filename)
        case _:
            print(f"{RED}Program starts from scratch without loading any file.{RESET}")

    while True:
        user_choice = get_menu_selection()
        match user_choice:
            case 1:
                print("(You selected: Add Appointment)")
                day = get_day(); print(f"You selected {RED} {day} {RESET}")
                time = get_time(); print(f"You selected the time slot: {RED} {time}->{time+1} {RESET} ")

                a_slot = find_appointment_by_daytime(current_database, day, time)
                if a_slot.get_appt_type() != 0:
                    print(f"{RED}Error: The slot is booked, booking failed{RESET}")
                else:
                    print(f"{RED}Good ! Slot is available to book.{RESET}")
                    service_type = get_service_type(); print(f"You selected: {RED} {SERVICE_TYPE_DICTIONARY[service_type]} {RESET}")
                    name = get_name()
                    phone = get_phone()
                    a_slot.schedule(name, phone, service_type)
                    print(f"Successful: Appointment booked. Detail: {a_slot}")

            case 2:
                print("(You selected: remove appointment)")
                day = get_day(); print(f"You selected {RED} {day} {RESET} ")
                time = get_time(); print(f"You selected the time slot: {RED} {time}->{time+1} {RESET} ")
                a_slot = find_appointment_by_daytime(current_database, day, time)
                if a_slot.get_appt_type() != 0:
                    a_slot.cancel()
                    print("Successful: Found Appointment, appointment cancelled")
                else:
                    print(f"{RED}Error: Appointment doesn't exist{RESET} ")
                pass
            case 3:
                print("(You selected: save appointment to file)")
                filename = get_filename()
                save_scheduled_appointments(current_database, filename)
                print(f"{RED}The database has been successfully saved to {filename} {RESET}")
            case 4:
                print("You selected 'Load Appointments'")
                filename = get_filename()
                current_database = load_scheduled_appointments(filename)
                pass
            case 5:
                print("You selected: Show Appointments by Day")
                day = get_day()
                day_appointment_list = find_appointment_by_day(current_database, day)
                print_appointment_list(day_appointment_list)
            case 6:
                print("You selected: Show Appointments by Name")
                name = get_name()
                appointment_list_by_name = find_appointment_by_name(current_database,name)
                print_appointment_list(appointment_list_by_name)
            case 7:
                print("You selected: Show revenue")
                show_revenue(current_database)
            case 8: break

    match input(MENU_BEFORE_QUIT).lower():
        case "y":
            filename = get_filename()
            save_scheduled_appointments(current_database, filename)
            print(f"{RED} Program End. All Data was saved to a file. {RESET}")
        case _:
            print(f"{RED}Program Ended Without Saving{RESET}")
    pass

#=======================================

main()