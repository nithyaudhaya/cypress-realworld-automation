from dataclasses import dataclass
class ConfigURLdetails:
    URL = "http://localhost:3000/"

@dataclass
class Cypressconfig:
    firstname = "Jian"
    lastname  = "Robert"
    username = "jrobertqui"
    password = "Test@321Test"
    confirm_password = password