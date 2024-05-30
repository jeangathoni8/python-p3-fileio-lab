def write_file(file_name, content):
    """Write content to a file."""
    with open(f'{file_name}.txt', 'w') as f:
        f.write(content)

def append_file(file_name, content):
    """Append content to a file."""
    with open(f'{file_name}.txt', 'a') as f:
        f.write(content)

def read_file(file_name):
    """Read content from a file."""
    with open(f'{file_name}.txt', 'r') as f:
        return f.read()

