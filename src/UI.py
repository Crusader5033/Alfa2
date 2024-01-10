from compressor import Compressor
from decompressor import Decompressor
from logger import Logger
from path_loader import Path_Loader

class CLI:
    def __init__(self):
        self.logger = Logger('../conf/config.ini')
        self.path_loader = Path_Loader('../conf/config.ini')
        self.compiler = Compressor(self.logger)
        self.decompiler = Decompressor(self.logger)

    def display_menu(self):
        print("\nMenu:")
        print("1. Compress")
        print("2. Decompress")
        print("3. Log")
        print("4. Help")
        print("0. Exit")

    def run(self):
        print("\nWelcome to TextCompresserJecna 1.0\n-----------------------------------")
        print("Before using the program make sure you have set up configuration file with correct paths.\nFor "
                      "more info use HELP option.")
        while True:
            try:


                self.display_menu()
                choice = input("Enter your choice: ")

                if choice == '1' or choice.lower() == "compress":
                    self.compress()
                elif choice == '2'or choice.lower() == "decompress":
                    self.decompress()
                elif choice == '3'or choice.lower() == "log":
                    print("Do you want to see all logs or filter?\n")
                    log_choice = input("log/filter: ")
                    if log_choice.lower() == "log":
                        self.display_log_all()
                    elif log_choice.lower() == "filter":
                        level_filter = input("Enter type of message (INFO/ERROR): ")
                        filter_string = f"{level_filter}"
                        self.display_log_filter(filter_string)
                    else:
                        print("Invalid choice")

                elif choice == '4'or choice.lower() == "help":
                    self.display_help()
                elif choice == '0'or choice.lower() == "exit":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again. \n")

            except Exception as e:
                print(f"Warning: An error occurred - {str(e)}")

    def compress(self):
        input_file_path, output_file_path, dictionary_file_path, decompiled_file_path = self.path_loader.get_paths_config()
        self.compiler.compress_file(input_file_path, output_file_path, dictionary_file_path)
        self.logger.log_info("Compression process completed successfully.")


    def display_log_all(self):
        self.logger.display_logs()

    def display_log_filter(self,filter_string):
        self.logger.display_logs(filter_string)

    def decompress(self):
        input_file_path, output_file_path, dictionary_file_path, decompiled_file_path = self.path_loader.get_paths_config()
        self.decompiler.load_dictionary(dictionary_file_path)
        self.decompiler.decompile_file(output_file_path, decompiled_file_path)
        self.logger.log_info("Decompression process completed successfully.")


    def display_help(self):
        print("\nHelp:")
        print("This is a simple CLI program for compressing and decompressing text files.")
        print("Choose an option from the menu to perform the desired operation.\n-------------------------------")
        print("Type 1 or compress --> compression of a file.")
        print("Type 2 or decompress --> decompression of a file.")
        print("Type 3 or log --> see a log where are all logs of commpression, decompression and if they were "
              "succesfull and if not theres log of error that occured.")
        print("Type 4 or help --> get here.")
        print("Type 0 or exit --> exit the program.\n-------------------------------")
        print("Setting up configuration file !IMPORTANT! \n")
        print("All paths are saved in /conf/config.ini this includes path to file that will be compressed and path for "
              "all output files.(You can of course use any "
              "path you want just replace the default with your own.)\n AFTER ANY CHANGE TO CONFIGURATION FILE THE PROGRAM NEEDS TO BE RESTARTED\n-------------------------------")
        print("1. Select path to file for compression --> Insert your file to folder input.Then open config.ini and "
              "type name of your file on end of input_file_path.\nE.g. ../input/TestFile.txt .")
        print("2. Select path where compressed file will be located and its name, on default its in folder output "
              "named output.txt recommended to keep it like that.")
        print("3. Select path where decoding file will be located and its name, on default its in folder output "
              "named dictionary.txt recommended to keep it like that.")
        print("4. Select path where decompressed file will be located and its name, on default its in folder output "
              "named decompiled.txt recommended to keep it like that.")


        print("\nGood luck :)")


