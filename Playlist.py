class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []
        self.total_duration = 0

    def add_track(self, track):
        # Check if the track is already in the playlist
        if track not in self.tracks:
            self.tracks.append(track)
            self.total_duration += track.duration
        else:
            print(f"Track '{track.title}' is already in the playlist.")

    def get_tracks(self):
        return self.tracks

    def display_playlist(self):
        print(f"Playlist Name: {self.name}")
        print(f"Total Duration: {self.get_duration_str()}")
        for track in self.tracks:
            print(f"- {track}")

    def get_duration_str(self):
        minutes = self.total_duration // 60
        seconds = self.total_duration % 60
        return f"{minutes} min {seconds} sec"
