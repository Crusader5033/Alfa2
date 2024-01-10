
from UI import CLI

if __name__ == "__main__":
    try:
        cli = CLI()
        cli.run()
    except Exception as e:
        raise  # Re-raise the exception for further debugging or handling
