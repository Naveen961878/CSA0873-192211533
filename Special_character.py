import re
def findspecialcharacters(text):
    special_characters = re.findall(r'[^\w\s]', text)
    return special_characters
text = "Welcome to &^23(&@SSE"
special_chars = findspecialcharacters(text)
print("Special characters found:", special_chars)
