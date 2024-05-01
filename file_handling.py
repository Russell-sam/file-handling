def handle_file_operations():
  try:
    # Create a new file named "my_file.txt"
    with open("my_file.txt", "w") as my_file:
      my_file.write("This is the first line of text.\n")
      my_file.write("Here's another line with a number: 42.\n")
      my_file.write("And a final line for good measure.\n")

    # Read the contents of "my_file.txt"
    with open("my_file.txt", "r") as my_file:
      contents = my_file.read()
      print("Contents of the file:\n", contents)

    # Append additional lines to "my_file.txt"
    with open("my_file.txt", "a") as my_file:
      my_file.write("\nAppended line 1.\n")
      my_file.write("Appended line 2 with another number: 100.\n")
      my_file.write("Appended line 3, the end.\n")

    print("\nSuccessfully created, read from, and appended to the file.")

  except FileNotFoundError:
    print("Error: File not found.")
  except PermissionError:
    print("Error: Insufficient permissions to access the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    print("\nFile operations completed.")

if __name__ == "__main__":
  handle_file_operations()
