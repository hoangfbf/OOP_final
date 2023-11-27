BLUE = "\033[94m"
RESET = "\033[0m"

class Appointment:
    def __init__(self, day_of_week: str, start_time_hour: int) -> None:
        self.__day_of_week = day_of_week.capitalize()          # string INIT
        self.__start_time_hour = start_time_hour  # integer INIT
                                                  # start hour will be in the 24hour format, ie:
                                                  # 9,10,11,12,13,14,15,16 (To keep things simple)

        self.__client_name = ""                  # string DEFAULT
        self.__client_phone = ""                 # string DEFAULT
        self.__appt_type = 0                      # integer DEFAULT

    def get_client_name(self) -> str:
        return self.__client_name
    def set_client_name(self, client_name: str) -> None:
        self.__client_name = client_name

    def get_client_phone(self) -> str:
        return self.__client_phone
    def set_client_phone(self, phone_number: str) -> None:
        self.__client_phone = phone_number

    def get_appt_type(self) -> int:
        return self.__appt_type
    def set_appt_type(self, appt_type: int) -> None:
        self.__appt_type = appt_type
    def get_appt_type_desc(self) -> str:
        match self.__appt_type:  # appt_type should be integer
            case 0: return "Available"
            case 1: return f"{BLUE}Mens Cut{RESET}"
            case 2: return f"{BLUE}Ladies Cut{RESET}"
            case 3: return f"{BLUE}Mens Colouring{RESET}"
            case 4: return f"{BLUE}Ladies Colouring{RESET}"
            case _: return "Error"

    def get_day_of_week(self) -> str:
        return self.__day_of_week
    def set_day_of_week(self, day: str) -> None:  # not sure why this function is required.
        self.__day_of_week = day.capitalize()

    def get_start_time_hour(self) -> int:
        return self.__start_time_hour
    def set_start_time_hour(self, start_hour: int) -> None:  # not sure why this function is required.
        self.__start_time_hour = start_hour

    def get_end_time_hour(self) -> int:
        return self.__start_time_hour + 1  # follow 24hr format. if Start time = 12, end time will be 12 + 1 = 13

    def schedule(self, name: str, phone: str, app_type: int) -> None:
        self.set_client_name(name)
        self.set_client_phone(phone)
        self.set_appt_type(app_type)

    def cancel(self) -> None:
        self.schedule("", "", 0)  # book an appointment with "" and 0, leaving the: day, start_hour untouched.

    def format_record(self) -> str:
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{ self.__start_time_hour}"

    def __str__(self) -> str:
        app_string = f"{self.__client_name:<18} {self.__client_phone:<16} {self.__day_of_week:<10} {self.__start_time_hour:>3} - {self.get_end_time_hour():<4} {self.get_appt_type_desc():<30}"
        if self.__appt_type != 0 :
            app_string = f"{BLUE}{app_string}{RESET}"
        return app_string

    pass



