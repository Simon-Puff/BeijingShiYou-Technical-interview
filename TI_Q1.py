# Read me:
# The format of input should be source + " " + target
# press ctrl + D on MacOs, press ctrl + Z on Windows in order to kill process
def combine_substrings (source, target):
    if len(target) == 0:
        #print("case 1")
        return 0
    # Corner Case
    count = 1
    index_iterator = 0
    source_copy = source
    # Copy so that it is easier to modify
    while index_iterator < len(target):
        char = target[index_iterator]
        if source.find(char) == -1:
            #print("case trival")
            return -1
            # Character not in source

        index = source_copy.find(char)
        # If not found, which means in source, there is no such character that
        # can form a sub string without affecting the original order
        if index != -1:
            source_copy = source_copy[index:]
            index_iterator += 1
        else:
            source_copy = source # reset the source_copy to restart over
            count += 1
    #print("Case 2")
    return count

try:
    while True:
        line = input()
        print(f"Read line: {line}")

        index_space = line.find(" ")
        source = line[:index_space]
        target = line[index_space + 1:]
        #print("Initially " + source + " " + target)

        print("Output: " + str(combine_substrings(source, target)))

except EOFError:
    print("\nEOF reached")

