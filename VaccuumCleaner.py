class CleaningAgent:
    def __init__(self):
        self.rooms = {'A': 'Dirty', 'B': 'Dirty', 'C': 'Dirty', 'D': 'Dirty'}  # Initial state
        self.current_room = 'A'  # Start in room A
        self.table = {  # Lookup table
            'A': {'Dirty': 'Clean', 'Clean': 'Move to B'},
            'B': {'Dirty': 'Clean', 'Clean': 'Move to C'},
            'C': {'Dirty': 'Clean', 'Clean': 'Move to D'},
            'D': {'Dirty': 'Clean', 'Clean': 'Move to A'}
        }

    def perceive_and_act(self):
        while True:
            status = self.rooms[self.current_room]
            action = self.table[self.current_room][status]

            if action == 'Clean':
                print(f"Cleaning {self.current_room}...")
                self.rooms[self.current_room] = 'Clean'
            else:
                print(f"Moving from {self.current_room} to {action.split()[-1]}...")
                self.current_room = action.split()[-1]  # Extract next room

            if all(state == 'Clean' for state in self.rooms.values()):
                print("All rooms are clean! Stopping...")
                break

# Run the agent
agent = CleaningAgent()
agent.perceive_and_act()
