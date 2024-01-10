import configparser


class Path_Loader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_paths_config(self):
        input_file_path = self.config.get('PATHS', 'input_file_path')
        output_file_path = self.config.get('PATHS', 'output_file_path')
        dictionary_file_path = self.config.get("PATHS", "dictionary_file_path")
        decompiled_file_path = self.config.get("PATHS", "decompiled_file_path")

        return input_file_path, output_file_path, dictionary_file_path, decompiled_file_path
