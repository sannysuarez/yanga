import re

''' Reject if name has spaces or special characters (allow only letters) and control the Max length. '''
def is_valid_name(name, max_length=15):
    if len(name) > max_length:
        return False, "Name must be at most {max_length} characters."
    if " " in name:
        return False, f"Name cannot contain spaces."
    if not re.match("^[a-zA-Z'-]+$", name): # Allows letters, apostrophes, and hyphens.
        return False, "Name contains invalid characters."
    return True, "" # No error

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

