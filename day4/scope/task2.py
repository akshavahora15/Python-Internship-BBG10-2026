def make_greeting(language):
    def greet(name):
        if language == "hindi":
            print(f"Namaste, {name}")
        else:
            print(f"Hello, {name}")
    return greet

hindi_greet = make_greeting("hindi")
english_greet = make_greeting("english")

hindi_greet("Aksha")
english_greet("Aksha")