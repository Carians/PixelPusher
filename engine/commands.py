class commands:
    def __init__(self):
        self.commands = {}

    def execute(self, command, message):
        if command in self.commands:
            self.commands[command](message)
        else:
            print('Command not found')

    def register(self, command, function):
        self.commands[command] = function
        self.commands.add(command)
