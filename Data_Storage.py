import pickle
from Music_Library import MusicLibrary


class DataStorage:
    @staticmethod
    def save_library(library, filename="library.pkl"):
        """
        Save the MusicLibrary instance to a file using pickle.
        :param library: The MusicLibrary instance to save.
        :param filename: The file to save the library to (default: 'library.pkl').
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(library, file)
            print(f"Library successfully saved to '{filename}'.")
        except Exception as e:
            print(f"Error saving library: {e}")

    @staticmethod
    def load_library(filename="library.pkl"):
        """
        Load the MusicLibrary instance from a file using pickle.
        If the file doesn't exist, return a new MusicLibrary instance.
        :param filename: The file to load the library from (default: 'library.pkl').
        :return: A MusicLibrary instance.
        """
        try:
            with open(filename, "rb") as file:
                library = pickle.load(file)
                print(f"Library successfully loaded from '{filename}'.")
                return library
        except FileNotFoundError:
            print(f"No existing library found. Creating a new library.")
            return MusicLibrary()
        except Exception as e:
            print(f"Error loading library: {e}")
            return MusicLibrary()
