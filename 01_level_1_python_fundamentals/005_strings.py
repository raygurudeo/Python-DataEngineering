# <<<<<<<<<<<<<<<<<<<<<<<<<<<< Strings in Python >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# <<<<<<<<< Indexing >>>>>>>>

# Access individual characters using their position (starting at 0)
text="Employee"
print(text[0])  #E
print(text[3])  #l
print(text[-1]) #e (Last character)

# <<<<<<<<<<<<<<<<<< Slicing >>>>>>>>>>>>>>>>>>>>>>>>>>>
# Extract a portion of the string.
text="Employee"
print(text[0:3])   # From index 0 to 2 (excluding 3)
print(text[2:])    # From index 2 to end (including 2)
print(text[:5])    # From start to index 4 (excluding 5)

# <<<<<<<<<<<<<<<<<<<<<<<< split() >>>>>>>>>>>>>>>>>>>>>>>
# Break a string into a list using a delimiter.
log = "INFO 2026-08-21 System started"
parts = log.split(" ")
print(parts)  # ['INFO', '2026-08-21', 'System', 'started']

# <<<<<<<<<<<<<<<<<< join() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Combine list elements into a string.
words = ["System", "started", "Successfully"]
sentence = " ".join(words)
print(sentence)  # System started Successfully

# <<<<<<<<<<<<<<< replace() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Replace part of a string.
message = "Error: Disk full"
cleaned = message.replace("Disk", "Memory")
print(cleaned)  # Error: Memory full

# <<<<<<<<<<<<<<<<<<< strip() >>>>>>>>>>>>>>>>>>>>>>>>>>>
# Remove leading/trailing spaces (or specific characters).
data = "   Log entry   "
print(data.strip())  # Log entry
data = "eeLog entryee"
print(data.strip("e"))  # Log entry
data = "$$$$$Log entry$$$$$"
print(data.strip("$"))  #Log entry
text = "@#$!Hello World!$#@"
print(text.strip("@#$!")) # Hello World
text = " #$ Hello World #$ "
print(text.strip(" #$")) # Hello World

# <<<<<<<<<<<<<<<<<<<<< lower() / upper() >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Change case.
msg = "Warning"
print(msg.lower())
print(msg.upper())

# <<<<<<<<<<<<<<<< f-strings >>>>>>>>>>>>>>>>>>>>>
# Format strings with variables (Python 3.6+).
level = "INFO"
date = "2026-08-21"
message = "System started"
print(f"{level} {date} - {message}") # INFO 2026-08-21 - System started