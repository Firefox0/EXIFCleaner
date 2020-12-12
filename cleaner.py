from PIL import Image
import os


def remove_metadata(path: str) -> None:
    """ Remove metadata of a single image. """
    with Image.open(path) as image:
        cleansed_image = Image.new(image.mode, image.size)
        data = [x for x in image.getdata()]
    cleansed_image.putdata(data)
    os.remove(path)
    cleansed_image.save(path)


def remove_metadata_multiple(file_paths: list) -> None:
    """ Remove metadata of multiple images. """
    if not file_paths:
        return
    for path in file_paths:
        remove_metadata(path)
