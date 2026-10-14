
class User:

    def __init__(self, email: str, name: str):
        self.email = email
        self.name = name

    def welcome_message(self) -> str:
        return f"Hello {self.name}, thanks for signing up!"
