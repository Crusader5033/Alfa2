class Decompressor:
    def __init__(self, logger):
        self.logger = logger
        self.dictionary = {}

    def load_dictionary(self, dictionary_file):
        try:
            with open(dictionary_file, 'r') as dict_file:
                for line in dict_file:
                    acronym, original_word = line.strip().split(": ")
                    self.dictionary[acronym] = original_word
        except Exception as e:
            self.logger.log_error(f"An error occurred while loading the dictionary: {str(e)}")
            raise

    def decompile_file(self, input_file, output_file):
        try:
            with open(input_file, 'r') as infile:
                content = infile.read()

            compressed_words = content.split()

            original_words = []
            for compressed_word in compressed_words:
                if compressed_word in self.dictionary:
                    original_words.append(self.dictionary[compressed_word])
                else:
                    original_words.append(compressed_word)

            original_content = ' '.join(original_words)

            with open(output_file, 'w') as outfile:
                outfile.write(original_content)

            self.logger.log_info("Decomression process completed successfully.")
        except Exception as e:
            self.logger.log_error(f"An error occurred: {str(e)}")
            raise
