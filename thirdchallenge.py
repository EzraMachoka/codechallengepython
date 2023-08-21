def greatest_value(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    current_value = 0
    top_value = 0
    
    
    for char in s:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
        else:
            top_value = max(top_value, current_value)
            current_value = 0
    
    return max(top_value, current_value)

print(greatest_value("kingsman")) 