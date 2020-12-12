import exifread
import os


def get_exif(path: str) -> dir:
    """ Get exif data of image at path. """
    try:
        f = open(path, "rb")
    except Exception as e:
        print(e)
        return {}
    exif = exifread.process_file(f)
    f.close()
    return exif


def get_exifs(file_paths: list) -> dict:
    """ Get exif data of all images at directory. """
    d = {}
    if not file_paths:
        return d
    for path in file_paths:
        exif = get_exif(path)
        file_name = os.path.basename(path)
        d[file_name] = exif
    return d


def print_exif(d: dict) -> None:
    """ Print dictionary containing exif data. """
    if not d:
        print("No exif data found.")
        return
    for key in d:
        print(f"{key}: {d[key]}")


def print_exifs(d: dict) -> None:
    """ Print dictionary containing exif data of multiple files. """
    if not d:
        print("No exif data found.")
        return
    for key in d:
        print(f"EXIF data of file: {key}")
        print_exif(d[key])
        print("")
