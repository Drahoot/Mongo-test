# Code Challenge 16
## Challenge Summary
Write a function called breadth first Arguments: tree Return: list of all values in the tree, in the order they were encountered

## Whiteboard
![Whiteboard](Code16.png)

## Big O
- O(N) time because its traversing trough each node


## Solution
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = self.rear

    def dequeue(self):
        if self.front == None:
            raise InvalidOperationError

        old_front = self.front
        self.front = old_front.next
        old_front.next = None
        return old_front.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        return not self.front


## Collaborators
- Jamal Malik
- Alec Torres
- Riki Plaza
