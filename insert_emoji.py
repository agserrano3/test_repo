import os
if not os.path.exists('codegen'):
    os.makedirs('codegen')
if not os.path.isfile('codegen/README.md'):
    with open('codegen/README.md', 'w'):
        pass
with open('codegen/README.md', 'r') as file:
    contents = file.readlines()
with open('codegen/README.md', 'w') as file:
    file.write("🌈\\n")
    for line in contents:
        file.write(line)

