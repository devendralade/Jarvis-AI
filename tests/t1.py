command = "what is the weather in New York"
keyword = "what is the weather in"

parts = command.split(keyword, 1)

print(parts)
print(parts[1].strip())