import json
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track
from Data_Storage import DataStorage
import random

# MENUS dictionary
MENUS = {
    "main": {
        1: "Play Music",
        2: "Music Library",
        3: "Playlists",
        4: "Exit"
    },
    "Play Music": {
        1: "Play",
        2: "Next",
        3: "Previous",
        4: "Toggle Repeat",
        5: "Toggle Shuffle",
        6: "Clear Queue",
        7: "Exit"
    },
    "Music Library": {
        1: "Add Track",
        2: "View Tracks",
        3: "Search Tracks",
        4: "Go Back to Main Menu"
    },
    "Playlist": {
        1: "Create Playlist",
        2: "View Playlists",
        3: "Add Track to Playlist",
        4: "Go Back to Main Menu"
    }
}

# -------------------------
# FUNCTIONALITY (Backend)
# -------------------------

def get_total_duration(queue):
    """Calculate the total duration of the tracks in the queue."""
    total_seconds = sum([track.duration for track in queue])  # sum the raw seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours} hr {minutes} min"


def manage_play_music(library):
    """Handles operations related to playing music."""
    current_track_index = 0
    repeat = False
    shuffle = False
    queue = library.get_tracks()

def manage_play_music(library):
    current_track_index = 0
    repeat = False
    shuffle = False
    queue = library.get_tracks()

    while True:
        if queue:
            print(f"Total Duration: {get_total_duration(queue)}")
            print(f"Shuffled: {'Yes' if shuffle else 'No'}")
            print(f"Repeat: {'Yes' if repeat else 'No'}")
            print(f"Currently Playing: {queue[current_track_index].title} – {queue[current_track_index].artist}")
            print("Tracks:")
            for i in range(current_track_index, len(queue)):
                print(f"({i+1}) {queue[i].title} – {queue[i].artist} ({queue[i].duration})")
        else:
            print("No tracks available.")
        
        choice = show_menu("Play Music")
        if choice == "1":
            print(f"Now Playing: {queue[current_track_index].title} – {queue[current_track_index].artist}")
            if repeat:
                print("Repeating this track.")
        elif choice == "2":
            current_track_index = (current_track_index + 1) % len(queue)
            print(f"Next Track: {queue[current_track_index].title} – {queue[current_track_index].artist}")
        elif choice == "3":
            current_track_index = (current_track_index - 1) % len(queue)
            print(f"Previous Track: {queue[current_track_index].title} – {queue[current_track_index].artist}")
        elif choice == "4":
            repeat = not repeat
            print(f"Repeat is now {'on' if repeat else 'off'}.")
        elif choice == "5":
            shuffle = not shuffle
            if shuffle:
                random.shuffle(queue)  # Shuffle the queue when enabled
                print("Shuffle is now on.")
            else:
                print("Shuffle is now off.")
        elif choice == "6":
            queue = library.get_tracks()  # Refilling the queue from the library
            print("Queue has been reset.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


        # User interaction with menu
        choice = show_menu("Play Music")

        if choice == "1":
            print(f"Now Playing: {queue[current_track_index].title} – {queue[current_track_index].artist}")
            current_track_index = -1  # Assume it's paused if the user hits play.
        elif choice == "2":
            current_track_index = (current_track_index + 1) % len(queue)
        elif choice == "3":
            current_track_index = (current_track_index - 1) % len(queue)
        elif choice == "4":
            repeat = not repeat
            print(f"Repeat is now {'on' if repeat else 'off'}.")
        elif choice == "5":
            shuffle = not shuffle
            print(f"Shuffle is now {'on' if shuffle else 'off'}.")
        elif choice == "6":
            queue.clear()
            print("Queue has been cleared.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_music_library(library):
    """Handles operations related to the music library, including CRUD for Tracks."""
    while True:
        choice = show_menu("Music Library")
        
        if choice == "1":  # Add Track
            title = input("Enter track title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            duration = input("Enter duration (mm:ss): ")

            try:
                track = Track(title, artist, album, duration)
                library.add_track(track)
                print(f"Track '{title}' added successfully!")
            except ValueError as e:
                print(f"Error adding track: {e}")

        elif choice == "2":  # View all Tracks
            if library.get_tracks():
                print("\nMusic Library:")
                library.display_tracks()
                track_index = int(input("Enter track number to modify (0 to skip): ")) - 1
                if 0 <= track_index < len(library.get_tracks()):
                    track = library.get_tracks()[track_index]
                    print(f"Selected Track: {track}")
                    action_choice = input("1. Update  2. Delete  3. Discard: ")
                    if action_choice == "1":
                        # Update Track
                        new_title = input(f"Enter new title (leave blank to keep '{track.title}'): ") or track.title
                        new_artist = input(f"Enter new artist (leave blank to keep '{track.artist}'): ") or track.artist
                        new_album = input(f"Enter new album (leave blank to keep '{track.album}'): ") or track.album
                        new_duration = input(f"Enter new duration (leave blank to keep '{track.duration}'): ") or track.duration

                        # Update track details
                        track.title = new_title
                        track.artist = new_artist
                        track.album = new_album
                        track.duration = new_duration

                        print(f"Track '{track.title}' updated successfully!")
                    elif action_choice == "2":
                        # Delete Track
                        library.get_tracks().remove(track)
                        print(f"Track '{track.title}' deleted successfully!")
                    else:
                        print("Changes discarded.")
                else:
                    print("Invalid track number.")
            else:
                print("The music library is empty.")

        elif choice == "3":  # Search Tracks
            title = input("Enter track title to search: ")
            results = library.search_track(title)
            if results:
                print("\nSearch Results:")
                for i, track in enumerate(results, 1):
                    print(f"{i}. {track}")
                track_index = int(input("Enter track number to modify (0 to skip): ")) - 1
                if 0 <= track_index < len(results):
                    track = results[track_index]
                    print(f"Selected Track: {track}")
                    action_choice = input("1. Update  2. Delete  3. Discard: ")
                    if action_choice == "1":
                        # Update Track
                        new_title = input(f"Enter new title (leave blank to keep '{track.title}'): ") or track.title
                        new_artist = input(f"Enter new artist (leave blank to keep '{track.artist}'): ") or track.artist
                        new_album = input(f"Enter new album (leave blank to keep '{track.album}'): ") or track.album
                        new_duration = input(f"Enter new duration (leave blank to keep '{track.duration}'): ") or track.duration

                        # Update track details
                        track.title = new_title
                        track.artist = new_artist
                        track.album = new_album
                        track.duration = new_duration

                        print(f"Track '{track.title}' updated successfully!")
                    elif action_choice == "2":
                        # Delete Track
                        library.get_tracks().remove(track)
                        print(f"Track '{track.title}' deleted successfully!")
                    else:
                        print("Changes discarded.")
                else:
                    print("Invalid track number.")
            else:
                print("No tracks found with that title.")

        elif choice == "4":  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")


def manage_playlists(library, playlists):
    """Handles operations related to playlists, including CRUD."""
    while True:
        choice = show_menu("Playlist")

        if choice == "1":  # Create Playlist
            name = input("Enter playlist name: ")
            if any(playlist.name == name for playlist in playlists):
                print("A playlist with that name already exists.")
            else:
                playlists.append(Playlist(name))
                print(f"Playlist '{name}' created successfully!")

        elif choice == "2":  # View all Playlists
            if playlists:
                print("\nPlaylists:")
                for i, playlist in enumerate(playlists, 1):
                    print(f"{i}. {playlist.name} ({len(playlist.tracks)} tracks)")
                playlist_index = int(input("Enter playlist number to modify (0 to skip): ")) - 1
                if 0 <= playlist_index < len(playlists):
                    playlist = playlists[playlist_index]
                    print(f"Selected Playlist: {playlist.name}")
                    action_choice = input("1. Update  2. Delete  3. Discard: ")
                    if action_choice == "1":
                        # Update Playlist
                        new_name = input(f"Enter new name (leave blank to keep '{playlist.name}'): ") or playlist.name
                        playlist.name = new_name
                        print(f"Playlist '{playlist.name}' updated successfully!")
                    elif action_choice == "2":
                        # Delete Playlist
                        playlists.remove(playlist)
                        print(f"Playlist '{playlist.name}' deleted successfully!")
                    else:
                        print("Changes discarded.")
                else:
                    print("Invalid playlist number.")
            else:
                print("No playlists available.")

        elif choice == "3":  # Add Track to Playlist
            if not library.get_tracks():
                print("No tracks in the library to add.")
                continue

            print("\nAvailable Tracks:")
            library.display_tracks()
            try:
                track_index = int(input("Enter the track number to add: ")) - 1
                track = library.get_tracks()[track_index]
            except (ValueError, IndexError):
                print("Invalid track number.")
                continue

            print("\nAvailable Playlists:")
            for i, playlist in enumerate(playlists, 1):
                print(f"{i}. {playlist.name}")
            try:
                playlist_index = int(input("Enter the playlist number: ")) - 1
                playlists[playlist_index].add_track(track)
                print(f"Track '{track.title}' added to playlist '{playlists[playlist_index].name}'.")
            except (ValueError, IndexError):
                print("Invalid playlist number.")

        elif choice == "4":  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")

# -----------------------------
# USER INTERACTION (Frontend)
# -----------------------------

def show_menu(menu_name):
    """Displays a menu and gets user choice, ensuring input is valid."""
    print(f"\n{menu_name} Menu:")
    # Display all menu options with proper numbering
    for key, value in MENUS[menu_name].items():
        print(f"{key}. {value}")
    
    # Ensure the input is a valid menu option
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in MENUS[menu_name]:
                return str(choice)  # Return the choice as a string, since inputs are compared as strings
            else:
                print("Invalid choice. Please enter a number corresponding to the menu options.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Ensure the main menu, play music, library, and playlist menus work with this validation.


def main():
    """Main function to handle the program's execution flow."""
    # Load existing data
    library, playlists = DataStorage.load()

    # Main menu loop
    while True:
        choice = show_menu("main")
        if choice == "1":
            manage_play_music(library)
        elif choice == "2":
            manage_music_library(library)
        elif choice == "3":
            manage_playlists(library, playlists)
        elif choice == "4":
            # Save data and exit
            DataStorage.save(library, playlists)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# -----------------------------
# RUN THE PROGRAM
# -----------------------------
main()
