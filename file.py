# Define the filename
filename = "example.txt"

# Open the file in append mode ('a'). This will create the file if it doesn't exist.
with open(filename, "a") as file:
    file.write("This is an additional line.\n")


