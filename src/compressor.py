class Compressor:
    def __init__(self, logger):
        self.logger = logger
        self.dictionary = {}


    def compress_file(self, input_file, output_file, dictionary_file):
        try:
            with open(input_file, 'r') as infile:
                content = infile.read()

            words = content.split()

            compressed_words = []
            for word in words:
                if len(word) > 3:
                    acronym = word[:2]
                    compressed_words.append(acronym)
                    self.dictionary[acronym] = word
                else:
                    compressed_words.append(word)

            compressed_content = ' '.join(compressed_words)

            with open(output_file, 'w') as outfile:
                outfile.write(compressed_content)

            with open(dictionary_file, 'w') as dict_file:
                for acronym, original_word in self.dictionary.items():
                    dict_file.write(f"{acronym}: {original_word}\n")
            self.logger.log_info("Compression process completed successfully.")
        except Exception as e:
            self.logger.log_error(f"An error occurred: {str(e)}")
            raise



