import os


def add_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            if extension not in extensions.keys():
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_level:
            add_extensions(file, first_level=True)


directory = input("Enter the directory: ")
extensions = {}
add_extensions(directory)

for extension, filenames in sorted(extensions.items(), key=lambda x: x[0]):
    print(extension)
    for filename in sorted(filenames):
        print(f"- - - {filename}")
