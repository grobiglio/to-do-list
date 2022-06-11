class Menu:
    """Manages user menus.

    Methods:
    --------
    - set_menu: Set menu based on defined options.
    - get_menu: Provides menu with user options.
    - request_opcion: Request option to the user.
    """

    def __init__(self, options) -> None:
        self.menu = ""
        self.valid_options = []
        self.set_menu(options)

    def set_menu(self, options: str) -> None:
        """Set user menu and valid user options.
        
        Parameters:
        -----------
        options: str
            Menu options according to the following format:

            Option 1
            Option 2
            Option 3
            .
            Option n
        """
        opt_lines = options.splitlines()
        opt_lines.pop(0)
        opt_lines.append('Exit')
        for opt_no, opt_line in enumerate(opt_lines, start=1):
            self.menu += f"[yellow bold]{opt_no}[/] - {opt_line}\n"
        self.valid_options = range(1, len(opt_lines)+1)

    def get_menu(self) -> str:
        return self.menu

    def request_option(self) -> int:
        """Requests the user a menu option.
        Check if it is a valid option.
        
        Return:
        -------
        chosen_option: int
            User input.
            None if the input is not a valid option.
        """
        try:
            chosen_option = int(input("Input option number: "))
        except ValueError:
            chosen_option = None
        option_is_valid = chosen_option in self.valid_options
        if option_is_valid:
            if chosen_option == self.valid_options[-1]:
                return "Exit"
        else:
            print("Input a valid option.")
        return chosen_option
        
            
        
