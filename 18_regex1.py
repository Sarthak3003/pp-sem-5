import re

def is_rgm_identifier(s: str) -> bool:
    regex = r"^[a-k][0369][a-zA-Z0-9#]*$"

    return bool(re.match(regex, s))


print(is_rgm_identifier("a3"))    # True

##Aise 5-6 examples aur bata dena.