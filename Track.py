class Track:
    def __init__(self, title, artist, album, duration):
        """
        Initializes a new Track object.

        :param title: The title of the track
        :param artist: The artist of the track
        :param album: The album of the track
        :param duration: The duration of the track in "mm:ss" format
        """
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = self._parse_duration(duration)

    def __str__(self):
        """
        Returns a string representation of the Track object.
        """
        return f"{self.title} - {self.artist} ({self.album}) [{self.get_duration()}]"

    def _parse_duration(self, duration):
        try:
            minutes, seconds = map(int, duration.split(":"))
            return minutes * 60 + seconds  # Convert to seconds
        except (ValueError, AttributeError):
            raise ValueError(f"Invalid duration format for track: '{duration}'. Expected 'mm:ss'.")

    def matches(self, query):
        """
        Checks if the track matches a search query.

        :param query: Query string
        :return: True if the query matches the title, artist, or album
        """
        query_lower = query.lower()
        return (
            query_lower in self.title.lower()
            or query_lower in self.artist.lower()
            or query_lower in self.album.lower()
        )
    
    def get_duration(self):
        """Returns the track duration in 'mm:ss' format."""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes:02}:{seconds:02}"
