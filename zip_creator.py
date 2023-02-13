from zipfile import ZipFile
from pathlib import Path


def make_zip(filepaths, destination_directory):
    destination_path = Path(destination_directory, 'my_zip.zip')
    with ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = Path(filepath)
            archive.write(filepath, arcname=filepath.name)
    print(f"File {destination_path} dibuat di {destination_directory}")


if __name__ == '__main__':
    pass