import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_script():
    script_name = input("What do you want to call your script? ")
    script_name = script_name.replace(" ", "_")
    num_options = int(input("How many menu options do you want? "))
    options = []
    for i in range(num_options):
        option_name = input(f"Name of option {i+1}: ")
        while option_name == "exit":
            print("Note: 'exit' is already included as an option and does not need to be added.")
            option_name = input(f"Name of option {i+1}: ")
        options.append(option_name)

    options.append("Exit")

    with open(f"{script_name}.py", "w") as f:
        f.write("#!/usr/bin/env python\n\n")
        f.write("import os\n\n")
        f.write(f"def menu():\n")
        f.write("    clear_screen()\n")
        f.write(f"    print('{script_name.replace('_', ' ').title()} Menu')\n")
        for i in range(num_options):
            f.write(f"    print('{i+1}. {options[i].title()}')\n")
        f.write(f"    print('(exit) Exit')\n\n")
        f.write(f"\n")
        f.write(f"def clear_screen():\n")
        f.write("    os.system('cls' if os.name == 'nt' else 'clear')\n\n")
        for i in range(num_options):
            f.write(f"def option_{i+1}():\n")
            f.write(f"    print('You selected {options[i]}')\n")
            f.write("    input('Press enter to return to menu...')\n\n")
        f.write(f"def exit_menu():\n")
        f.write("    print('Goodbye!')\n")
        f.write("    exit()\n\n")
        f.write(f"if __name__ == '__main__':\n")
        f.write("    while True:\n")
        f.write("        menu()\n")
        f.write("        choice = input('Enter your choice: ')\n")
        for i in range(num_options):
            f.write(f"        if choice == '{i+1}':\n")
            f.write(f"            option_{i+1}()\n")
        if "exit" in options:
            f.write("        elif choice.lower() == 'exit' or choice == '0':\n")
        else:
            f.write("        elif choice.lower() == 'exit':\n")
        f.write("            exit_menu()\n")
        f.write("        else:\n")
        f.write("            print('Invalid choice. Try again.')\n")

    print(f"Script '{script_name}.py' created successfully!")

clear_screen()
create_script()
