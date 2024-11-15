class Track:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = self.convert_duration(duration)
    
    def convert_duration(self, duration):
        """Convert duration from string mm:ss to seconds for numeric operations."""
        minutes, seconds = map(int, duration.split(':'))
        return minutes * 60 + seconds
    
    def get_duration_str(self):
        """Convert duration in seconds back to string mm:ss."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes:02}:{seconds:02}"
    
    def __str__(self):
        return f"{self.title} – {self.artist} ({self.get_duration_str()})"

class MusicLibrary:
    def __init__(self):
        self.tracks = []
    
    def add_track(self, track):
        self.tracks.append(track)
        self.tracks = sorted(self.tracks, key=lambda x: (x.title, x.artist, x.album, x.duration))
    
    def display_tracks(self):
        for i, track in enumerate(self.tracks):
            print(f"[{i + 1}] {track}")
    
    def search_track(self, title):
        return [track for track in self.tracks if track.title.lower() == title.lower()]
