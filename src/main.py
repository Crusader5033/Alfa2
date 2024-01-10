from compressor import Compressor
from decompressor import Decompressor
from logger import Logger
from path_loader import Path_Loader
from UI import CLI

if __name__ == "__main__":
    try:
        cli = CLI()
        cli.run()
    except Exception as e:
        raise  # Re-raise the exception for further debugging or handling
