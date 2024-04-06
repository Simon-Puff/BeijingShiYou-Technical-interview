# Read me:
# press ctrl + D on MacOs, press ctrl + Z on Windows in order to kill process
def check_brackets(strings):
    stack = []
    output = [" "] * len(strings) # initialize a output list to hold all characters of output
    output_str = ""

    for i, char in enumerate(strings):
        if char == '(':
            stack.append(i)  # push the index of '(' onto stack
        elif char == ')':
            if stack:
                stack.pop()  # pop one off the stack
            else:
                output[i] = '?'  
                # if nothing on stack, we mark the corresponding char on the
                # list "output" as "?"
    
    # Exit the for loop, wrap up every unmatched '()'
    for i in stack:
        output[i] = 'x'  # mark 'x' correspondingly
    # concatenate the result and return 
    for char in output:
        output_str += char
    return output_str
    

try:
    while True:
        line = input()
        print(check_brackets(line))

except EOFError:
    print("\nEOF reached")