from bibtex_format import Bibtex

class Ui:
    def __init__(self, reference_writer, io):
        self.reference_writer = reference_writer
        self.io = io

        self.commands = {
            0: self.show_commands,
            1: self.add_book_citation,
            2: self.create_new_file,
            9: self.exit_app,
                        }
        self.loop = True

    def show_commands(self):
        self.io.write("0: Show all available operation commands")
        self.io.write("1: Add book citation")
        self.io.write("2: Create new BibTex file")
        self.io.write("9: Exit application")

    def add_book_citation(self):
        self.io.write("Please add the following information")
        key = self.io.read("Add key (enter 'q' to exit): ")
        if key.lower() == 'q':
            return
        title = self.io.read("Add title: ")
        author = self.io.read("Add author: ")
        year = self.io.read("Add year: ")
        publisher = self.io.read("Add publisher: ")
        address = self.io.read("Add address: ")

        citation = Bibtex().book(title, author, year, publisher, address)
        if self.reference_writer.write(citation):
            self.io.write("Book citation added succesfully")
        else:
            self.io.write("Citation could not be added")
        self.loop = True

    def exit_loop(self):
        self.loop = False

    def run(self):
        self.menu()

        while self.loop:
            self.io.write("")
            command = self.io.read("""
                Select the operation you want to perform (enter 0 to show all): 
                """)
            try:
                operation = int(command)
                if operation in self.commands:
                    self.commands[operation]()
                else:
                    self.io.write("Invalid, please try again with correct command")
            except ValueError:
                self.io.write("Please enter a valid number")

    def menu(self):
        self.io.write("Welcome to the app!")
        self.io.write("")
        self.io.write("Available commands")
        self.show_commands()

    def exit_app(self):
        raise SystemExit

    def create_new_file(self):
        new_filename = self.io.read("Please enter a new filename:")
        self.reference_writer.new_filename(new_filename)
