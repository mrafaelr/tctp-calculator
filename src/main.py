import sys
import messages

KNOWN_COMMANDS = ["-h"]

def main():
    parseArgs(sys.argv)

def parseArgs(args):
    if len(args) < 2:
        messages.displayHelp()
    else:
        match extractCommand(args):
            case "-h":
                messages.displayHelp()
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