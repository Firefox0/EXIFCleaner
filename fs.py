import os

image_file_extensions = {"png", "jpg", "jpeg"}


def get_images(directory: str) -> list:
    """ Get paths to all images at directory. """
    l = []
    if not os.path.isdir(directory):
        return l
    directory_files = os.listdir(directory)
    for f in directory_files:
        for extension in image_file_extensions:
            if extension in f:
                full_path = os.path.join(directory, f)
                l.append(full_path)
    return l
