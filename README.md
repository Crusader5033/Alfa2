# TextCompressorJecna

TextCompressorJecna is a Python command-line interface (CLI) program designed for compressing and decompressing text files. It offers essential features such as compression, decompression, logging, and a help menu. This README provides an overview of the project, its file structure, and usage instructions.

## File Structure

- **conf**: Configuration directory.
  - `config.ini`: Configuration file storing paths for input, output, dictionary, and decompiled files.
- **doc**: Documentation directory.
- **input**: Directory for storing input text files.
- **log**: Directory for storing log files.
- **output**: Directory for storing compressed, dictionary, and decompiled output files.
- **src**: Source code directory.
  - `UI.py`: User interface class handling user interactions.
  - `Main.py`: Main class initializing the application.
  - `PathLoader.py`: Class for loading paths from the configuration file.
  - `Logger.py`: Class for configuring and managing logging functionality.
  - `Compressor.py`: Class for compressing text data.
  - `Decompressor.py`: Class for decompressing text data.
- **tests**: Directory for test files.

## Usage

1. **Configuration File Setup**: Before using the program, set up the `config.ini` file in the `conf` directory. Update paths for input, output, dictionary, and decompiled files.

   ```ini
   [PATHS]
   input_file_path = ../input/TestFile.txt
   output_file_path = ../output/output.txt
   dictionary_file_path = ../output/dictionary.txt
   decompiled_file_path = ../output/decompiled.txt

   [LOGGING]
   filename = ../log/log.log
   level = INFO
   format = %(asctime)s - %(levelname)s - %(message)s
-*Note: After any changes to the configuration file, restart the program.
-By default there is a exammple text file for demonstration.
## Menu Options:

-Type 1 or compress to compress a file.
-Type 2 or decompress to decompress a file.
-Type 3 or log to view logs. Choose between displaying all logs or applying a filter.
-Type 4 or help to view the help menu.
-Type 0 or exit to exit the program.
## Help Menu:

-View help menu for detailed instructions on setting up the configuration file.
-Follow the instructions for selecting paths for compression, output, dictionary, and decompiled files.

## Logging:

-Logs are stored in the log directory.__
-Filter logs by choosing to display all logs or applying a filter based on log type (INFO/ERROR).

## Running the Program:
-Open cmd.
-Move to directory where the program is, then move to src folder.
-Execute main.py to run the program. Just type : python main.py
-Follow the on-screen menu instructions to perform the desired operation.
