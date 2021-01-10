def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open (filename, "w") as script:
    import os
    filesize = os.path.getsize(filename)
    script.write(comments)
  return filesize

print(create_python_script("program.py"))
