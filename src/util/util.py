from . import messages
from workouts import ctsTest

def parseArgs(args):
    if len(args) < 2:
        messages.displayHelp()
    else:
        match extractCommand(args):
            case "-h":
                messages.displayHelp()
            case "-cts":
                print(ctsTest())
            case "error":
                messages.displayUnknownCommand()
                messages.displayHelp()

def extractCommand(args):
    KNOWN_COMMANDS = ["-h", "-cts"]

    command = 'error'
    
    for arg in args:
        if arg in KNOWN_COMMANDS:
            command = arg
        
    return command