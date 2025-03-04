class SimpleReflexAgent:
    def __init__(self):
        # Initial state: All rooms are dirty
        self.rooms = {'A': 'Dirty', 'B': 'Dirty', 'C': 'Dirty', 'D': 'Dirty'}
        self.current_room = 'A'  # Start in Room A

    def perceive_and_act(self):
        while True:
            print(f"Agent is in Room {self.current_room}, Status: {self.rooms[self.current_room]}")

            # If the room is dirty, clean it
            if self.rooms[self.current_room] == 'Dirty':
                print(f"Cleaning Room {self.current_room}...")
                self.rooms[self.current_room] = 'Clean'
            else:
                # Move to the next room in order (A → B → C → D)
                next_room = chr(ord(self.current_room) + 1) if self.current_room != 'D' else 'A'
                print(f"Moving to Room {next_room}...")
                self.current_room = next_room
            
            # Stop if all rooms are clean
            if all(status == 'Clean' for status in self.rooms.values()):
                print("All rooms are clean! Agent is stopping.")
                break

# Run the agent
agent = SimpleReflexAgent()
agent.perceive_and_act()
