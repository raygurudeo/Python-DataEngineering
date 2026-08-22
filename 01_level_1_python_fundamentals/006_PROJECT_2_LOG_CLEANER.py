# Take a structured log line like
log="INFO 2026-08-21 System started successfully"

# and parse it into (Expected Output)
# Level → INFO
# Date → 2026-08-21
# Message → System started OK

# Clean and format
splitted_log = log.split(" ", 2)  # split into 3 parts: level, date, message
level = splitted_log[0].strip().upper() # Ensure upper case
date = splitted_log[1].strip()
message = splitted_log[2].strip().replace("successfully","OK")  # example cleaning

# Output
print(f"Level -> {level}")
print(f"Date -> {date}")
print(f"Message -> ", message)