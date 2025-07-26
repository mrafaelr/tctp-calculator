import sys
import messages
from workouts import ctsTest

KNOWN_COMMANDS = ["-h", "-cts"]

def main():
    parseArgs(sys.argv)

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
    command = 'error'
    for arg in args:
        if arg in KNOWN_COMMANDS:
            command = arg
        
    return command



if __name__ == "__main__":
    main()