from pathlib import Path
cwd = Path.cwd()

print(cwd.parents[0])

demo_file = Path(Path.joinpath(cwd.parents[0], 'demo.txt'))

# Get the file name
print('\nfile name: ' + demo_file.parents[0])

# Get the extension
print('\nfile suffix: ' + demo_file.suffix)

# Get the folder
print('\nfile folder: ' + demo_file.parent.name)

# Get the size
print('\nfile size: ' + str(demo_file.stat().st_size) + '\n')