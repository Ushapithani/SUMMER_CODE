'''Build a Mini Spotify Queue using a Linked List

Spotify allows users to add songs to the Play Queue.
Songs are played in the same order in which they were added.

Implement the following operations using a Queue (Linked List):

Add Song

Play Next Song

Now Playing

Last Added Song

Display Queue

exit 

sample output 
................ mini spotify ..............

'''





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):     
        self.front = None
        self.rear = None
        
    def add_song(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def play_next_song(self):# delete at head 
        if self.front is None:
            print("No songs in the queue.")
            return
        print(f"Playing next song: {self.front.data}")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def now_playing(self):
        if self.front is None:
            print("No songs are currently playing.")
            return
        print(f"Now playing: {self.front.data}")
    
    def last_added_song(self):
        if self.rear is None:
            print("No songs have been added yet.")
            return
        print(f"Last added song: {self.rear.data}")
    def display_queue(self):
        if self.front is None:
            print("Queue is empty.")
            return
        current = self.front
        print("Current Queue:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def exit(self):
        print("Exiting the Mini Spotify Queue.")
        exit()
a=Queue()
while True:
    print("\n................ mini spotify ..............")
    print("1. Add Song")
    print("2. Play Next Song")
    print("3. Now Playing")
    print("4. Last Added Song")
    print("5. Display Queue")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        song = input("Enter the song name to add: ")
        a.add_song(song)
        print(f"Added '{song}' to the queue.")
    elif choice == '2':
        a.play_next_song()
    elif choice == '3':
        a.now_playing()
    elif choice == '4':
        a.last_added_song()
    elif choice == '5':
        a.display_queue()
    elif choice == '6':
        a.exit()
    else:
        print("Invalid choice. Please try again.")



