def displayUnknownCommand():
    print(
"""
Error: A valid command was not supplied.
""")

def displayHelp():
    print(
"""
To use the TCTP calculator, run the following command:

$ python3 main.py <command [<parameter-name> <parameter-value>]*>

--- Commands:

-h      Display help
-cts    Supplies the workout description for the CTS test, used to determine the intensity used in the programs.
    
""")