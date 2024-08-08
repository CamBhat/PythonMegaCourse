import zipfile
import pathlib

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, mode="r") as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive(archivepath="files/compressed.zip", dest_dir="files")