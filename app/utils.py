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

def get_state():
    return [
        ("FC","Abuja (FCT)"),
        ("AB", "Abia"),
        ("AD", "Adamawa"),
        ("AK", "Akwa Ibom"),
        ("AN", "Anambra"),
        ("BA", "Bauchi"),
        ("BY", "Bayelsa"),
        ("BE", "Benue"),
        ("BO", "Borno"),
        ("CR", "Cross River"),
        ("DE", "Delta"),
        ("EB", "Ebonyi"),
        ("ED", "Edo"),
        ("EK", "Ekiti"),
        ("EN", "Enugu"),
        ("GO", "Gombe"),
        ("IM", "Imo"),
        ("JI", "Jigawa"),
        ("KD", "Kaduna"),
        ("KN", "Kano"),
        ("KT", "Katsina"),
        ("KE", "Kebbi"),
        ("KO", "Kogi"),
        ("KW", "Kwara"),
        ("LA", "Lagos"),
        ("NA", "Nassarawa"),
        ("NI", "Niger"),
        ("OG", "Ogun"),
        ("ON", "Ondo"),
        ("OS", "Osun"),
        ("OY", "Oyo"),
        ("PL", "Plateau"),
        ("RI", "Rivers"),
        ("SO", "Sokoto"),
        ("TA", "Taraba"),
        ("YO", "Yobe"),
        ("ZA", "Zamfara"),
    ]
