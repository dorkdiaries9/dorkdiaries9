class Datastack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def traverse(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Traversing contents of stack:")
            for item in self.items:
                print(item)

# main
def check_balanced_brackets(eq):
    stack = Datastack()
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in eq:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return "Stack is not balanced"
            top_element = stack.pop()
            if matching_brackets[char] != top_element:
                return "Stack is not balanced"

    if stack.is_empty():
        return "Stack is balanced"
    else:
        return "Stack is not balanced"

# Main code execution
eq = input("Enter equation: ")
print(check_balanced_brackets(eq))

      
      
      
         
