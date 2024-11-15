class Queue:
    def __init__(self):
        self.queue = []
        self.current_index = 0
        self.repeat = False
        self.shuffled = False
    
    def add_to_queue(self, tracks):
        self.queue.extend(tracks)
    
    def shuffle(self):
        from random import shuffle
        if not self.shuffled:
            shuffle(self.queue)
            self.shuffled = True
    
    def unshuffle(self, original_order):
        self.queue = original_order
        self.shuffled = False
    
    def toggle_repeat(self):
        self.repeat = not self.repeat
    
    def next_track(self):
        if self.current_index + 1 < len(self.queue):
            self.current_index += 1
        elif self.repeat:
            self.current_index = 0
        else:
            print("No more tracks in the queue.")
    
    def previous_track(self):
        if self.current_index > 0:
            self.current_index -= 1
        elif self.repeat:
            self.current_index = len(self.queue) - 1
    
    def display_queue(self):
        print("Current Queue:")
        for i, track in enumerate(self.queue[:10], 1):
            print(f"[{i}] {track}")
        print(f"Current Track: {self.queue[self.current_index]}")
