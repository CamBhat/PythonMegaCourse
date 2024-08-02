contents = ["Contents 1",
            "Contents 2",
            "Contents 3"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"App1-ToDo/files/{filename}", "w")
    file.write(content)