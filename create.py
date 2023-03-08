import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_script():
    script_name = input("What do you want to call your script? ")
    script_name = script_name.replace(" ", "_")
    num_options = int(input("How many menu options do you want? "))
    options = []
    func_names = []
    for i in range(num_options):
        option_name = input(f"Name of option {i+1}: ")
        while option_name == "exit":
            print("Note: 'exit' is already included as an option and does not need to be added.")
            option_name = input(f"Name of option {i+1}: ")
        func_name = option_name.lower().replace(" ", "_").replace("-", "").replace(".", "")
        options.append(option_name)
        func_names.append(func_name)

    options.append("Exit")
    func_names.append("exit_menu")

    with open(f"{script_name}.py", "w") as f:
        f.write("#!/usr/bin/env python\n\n")
        f.write("###===Import Modules Go Here===###")
        f.write(f"\n")
        f.write("import os\n")
        f.write(f"\n")
        f.write("###===Separator Function For Pretty Menu===###")
        f.write(f"\n")
        f.write(f"def print_separator():\n")
        f.write("    print(\"=\" * 50)\n\n")
        f.write(f"###===Your Viewable Menu===###")
        f.write(f"\n")
        f.write(f"def menu():\n")
        f.write("    clear_screen()\n")
        f.write(f"    print('{script_name.replace('_', ' ').title()}')\n")
        f.write("    print_separator()\n")
        for i in range(num_options):
            f.write(f"    print('{i+1}. {options[i].title()}')\n")
        f.write(f"    print('(exit) Exit')\n\n")
        f.write("###===Making Clear Screen Work On Windows And Linux===###")
        f.write(f"\n")
        f.write(f"def clear_screen():\n")
        f.write("    os.system('cls' if os.name == 'nt' else 'clear')\n\n")
        f.write("###===When You Choose An Option It Runs One Of These===###")
        f.write(f"\n")
        for i in range(num_options):
            # Get function name based on option name
            func_name = func_names[i]
            f.write(f"def {func_name}():\n")
            f.write(f"    print('You selected {options[i]}')\n")
            f.write("    input('Press enter to return to menu...')\n\n")
        f.write(f"def exit_menu():\n")
        f.write("    print('Goodbye!')\n")
        f.write("    exit()\n\n")
        f.write("###===Enter Your Choice And Then It Will Activate That Option===###")
        f.write(f"\n")
        f.write(f"if __name__ == '__main__':\n")
        f.write("    while True:\n")
        f.write("        menu()\n")
        f.write("        choice = input('Enter your choice: ')\n")
        for i in range(num_options):
            f.write(f"        if choice == '{i+1}':\n")
            func_name = func_names[i]
            f.write(f"            {func_name}()\n")
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
