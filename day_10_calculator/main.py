from replit import clear

def format_name(f_name, l_name):
    """Take a first and the last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide a name."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

format_name()

clear()
print(format_name(input("What is your First Name? "), input("What is your Last Name? ")))