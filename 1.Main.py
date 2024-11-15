from Track import Track
from Music_Library import MusicLibrary
from Playlist import Playlist
from Queue import Queue
from Data_Storage import DataStorage

# MENUS dictionary holds all the menu options for different sections of the program
MENUS = {
    "main": {
        1: "Manage Library",
        2: "Manage Playlists",
        3: "Manage Queue",
        4: "Exit"
    },
    "library": {
        1: "Add Track",
        2: "View Tracks",
        3: "Search Tracks",
        4: "Go back to main menu"
    },
    "playlist": {
        1: "Create Playlist",
        2: "View Playlists",
        3: "Add Track to Playlist",
        4: "View Playlist",
        5: "Go back to main menu"
    },
    "queue": {
        1: "Add to Queue",
        2: "Next Track",
        3: "Previous Track",
        4: "Display Queue",
        5: "Go back to main menu"
    }
}

def showMenu(target: str, inline: int = None):
    """Display the menu for a specific section.
    
    Args:
        target (str): The section of the program to display the menu for (e.g., 'main', 'library', 'playlist', 'queue').
        inline (int): The number of items to display per line (optional).
    """
    print("\n<-----Menu----->")
    i = 1 if inline is not None else None  # If inline is provided, show inline menu
    for menu in MENUS[target]:
        # Format the output, making it display inline if necessary
        out = "[{}]".format(menu)
        if inline is not None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end="\t" if inline is not None else "\n")
        if i is not None:
            i = 1 if i == inline else i + 1

def prompt(phrase: str) -> str:
    """Prompts the user for input.
    
    Args:
        phrase (str): The message to display to the user.
    
    Returns:
        str: The input provided by the user.
    """
    return input(phrase)

def main():
    """The main entry point for the program."""
    library = DataStorage.load_library()  # Load the music library
    playlists = {}  # Initialize an empty dictionary to store playlists
    queue = Queue()  # Create an empty queue to manage tracks

    while True:
        showMenu("main")  # Display the main menu
        choice = int(prompt("Select an option: "))  # Get the user's choice
        
        if choice == 1:  # Manage Library
            manage_library(library)
        elif choice == 2:  # Manage Playlists
            manage_playlists(library, playlists)
        elif choice == 3:  # Manage Queue
            manage_queue(queue, library, playlists)
        elif choice == 4:  # Exit the program
            DataStorage.save_library(library)  # Save the library before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def manage_library(library):
    """Manage the music library (add, view, search tracks)."""
    while True:
        showMenu("library")  # Display the library menu
        choice = int(prompt("Select an option: "))  # Get the user's choice
        
        if choice == 1:  # Add Track to library
            title = prompt("Enter track title: ")  # Example: "Let It Be"
            artist = prompt("Enter artist: ")  # Example: "The Beatles"
            album = prompt("Enter album: ")  # Example: "Let It Be"
            duration = prompt("Enter duration (mm:ss): ")  # Example: "4:03"
            library.add_track(Track(title, artist, album, duration))  # Add track to library
            print("Track added successfully.")
        elif choice == 2:  # View Tracks in the library
            print("Viewing all tracks in the library:")
            library.display_tracks()
        elif choice == 3:  # Search for tracks in the library
            query = prompt("Search query (Enter part of the title, artist, or album): ")
            results = library.search_tracks(query)  # Search library for matching tracks
            if results:
                print(f"Found {len(results)} matching tracks:")
                for track in results:
                    print(track)
            else:
                print("No matching tracks found.")
        elif choice == 4:  # Go back to the main menu
            break
        else:
            print("Invalid option.")

def manage_playlists(library, playlists):
    """Manage playlists (create, view, add tracks, etc.)."""
    while True:
        showMenu("playlist")  # Display the playlist menu
        choice = int(prompt("Select an option: "))  # Get the user's choice
        
        if choice == 1:  # Create a new playlist
            name = prompt("Enter playlist name: ")  # Example: "My Favorite Tracks"
            playlists[name] = Playlist(name)  # Create new playlist and add to playlists dictionary
            print(f"Playlist '{name}' created.")
        elif choice == 2:  # View all playlists
            print("Playlists:")
            if playlists:
                for name in playlists:
                    print(name)
            else:
                print("No playlists available.")
        elif choice == 3:  # Add track to a playlist
            name = prompt("Enter playlist name: ")  # Example: "My Favorite Tracks"
            if name not in playlists:
                print("Playlist not found.")
                continue
            query = prompt("Enter track title to search for: ")  # Example: "Let It Be"
            track_results = library.search_tracks(query)
            if track_results:
                track = track_results[0]  # Get the first track that matches the search query
                playlists[name].add_track(track)  # Add track to the specified playlist
                print(f"Track '{track.title}' added to playlist '{name}'.")
            else:
                print(f"No track found with the title '{query}'.")
        elif choice == 4:  # View a specific playlist
            name = prompt("Enter playlist name: ")
            if name in playlists:
                playlists[name].display_playlist()  # Display the playlist's details
            else:
                print(f"Playlist '{name}' not found.")
        elif choice == 5:  # Go back to the main menu
            break
        else:
            print("Invalid option.")

def manage_queue(queue, library, playlists):
    """Manage the queue (add tracks, skip, shuffle, etc.)."""
    while True:
        showMenu("queue")  # Display the queue menu
        choice = int(prompt("Select an option: "))  # Get the user's choice
        
        if choice == 1:  # Add track to the queue
            print("Choose source:")
            print("[1] From Library")
            print("[2] From Playlist")
            sub_choice = int(prompt("Select source (1 or 2): "))  # Choose where to add the track from
            
            if sub_choice == 1:  # Add from library
                library.display_tracks()
                index = int(prompt("Select track index to add to the queue: ")) - 1  # Select a track from library
                queue.add_to_queue([library.tracks[index]])  # Add track to queue
                print("Track added to queue.")
            elif sub_choice == 2:  # Add from playlist
                playlist_name = prompt("Enter playlist name: ")
                if playlist_name in playlists:
                    queue.add_to_queue(playlists[playlist_name].tracks)  # Add all tracks from the playlist to the queue
                    print("Playlist tracks added to queue.")
                else:
                    print(f"Playlist '{playlist_name}' not found.")
            else:
                print("Invalid option.")
        elif choice == 2:  # Next track
            queue.next_track()
        elif choice == 3:  # Previous track
            queue.previous_track()
        elif choice == 4:  # Display the queue
            queue.display_queue()
        elif choice == 5:  # Go back to the main menu
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()  # Start the program
