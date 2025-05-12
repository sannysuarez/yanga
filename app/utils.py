import re

''' Clean user input  '''
def clean_name_input(name, max_lenght=15):
    name = name.strip() # Remove leading/trailing whitespace
    name = re.sub(r"[^a-zA-Z\-']", '', name) # Keep letters, hyphens and apostrophes; remove other special characters and digits.
    name = name.lower()
    return name[:max_lenght] # Truncate to Max_lenght

def is_valid_email(email):
    """
    Matches Email pattern using regular expressions. (covers most common cases).
    ^[a-zA-Z0-9._%+-]+: Allows common characters in the local part (before @)
    @[a-zA-Z0-9.-]+: Accepts domain characters (letters, numbers, hyphen, dot)
    \.[a-zA-Z]{2,}$: Requires a top-level domain of at least 2 letters (e.g., .com, .org, .ng)
    """
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is not None

def clean_phone_number(tel, max_length=11):
    tel = re.sub(r'\D', '', tel) # Remove all non-digit characters
    if len(tel) == 11 and tel.startswith('0'):
        return tel
    elif len(tel) == 10 and not tel.startswith('0'):
        return '0' + tel
    else:
        return tel[:max_length]

def get_state():
    return [
        "Abuja (FCT)",
        "Abia",
        "Adamawa",
        "Akwa Ibom",
        "Anambra",
        "Bauchi",
        "Bayelsa",
        "Benue",
        "Borno",
        "Cross River",
        "Delta",
        "Ebonyi",
        "Edo",
        "Ekiti",
        "Enugu",
        "Gombe",
        "Imo",
        "Jigawa",
        "Kaduna",
        "Kano",
        "Katsina",
        "Kebbi",
        "Kogi",
        "Kwara",
        "Lagos",
        "Nassarawa",
        "Niger",
        "Ogun",
        "Ondo",
        "Osun",
        "Oyo",
        "Plateau",
        "Rivers",
        "Sokoto",
        "Taraba",
        "Yobe",
        "Zamfara"
    ]