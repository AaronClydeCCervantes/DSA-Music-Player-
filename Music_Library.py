class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        # Check if the track already exists in the library
        if any(existing_track.title == track.title and existing_track.artist == track.artist for existing_track in self.tracks):
            print(f"Track '{track.title}' by '{track.artist}' is already in the library.")
        else:
            self.tracks.append(track)
            self.tracks.sort(key=lambda x: x.title.lower())  # Sort by title only for simplicity

    def get_tracks(self):
        return self.tracks

    def display_tracks(self):
        for i, track in enumerate(self.tracks, 1):
            print(f"[{i}] {track}")

    def search_track(self, title):
        return [track for track in self.tracks if track.title.lower() == title.lower()]
