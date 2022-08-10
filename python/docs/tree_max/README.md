# Code Challenge 17
## Challenge Summary
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric

## Whiteboard
![Whiteboard](challenge17whiteboard.png)

## Solution
    def find_max(self):
        vals = self.post_order()
        max_value = vals[0]
        for value in vals:
            if value > max_value:
                max_value = value
        return max_value

## Collaborators
- Jamal Malik
- Alec Torres
- Riki Plaza
