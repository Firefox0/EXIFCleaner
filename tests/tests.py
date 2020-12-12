import sys
# include parent directory
sys.path.append("../")
import unittest
import viewer
import cleaner
import fs
import shutil
import os


class TestClean(unittest.TestCase):

    def copy_files(self, directory_source, directory_target):
        if not os.path.isdir(directory_target):
            os.mkdir(directory_target)
        file_paths = fs.get_images(directory_source)
        for path in file_paths:
            shutil.copy(path, directory_target)

    def view(self, file_paths):
        tags = viewer.get_exifs(file_paths)
        viewer.print_exifs(tags)

    def test_clean(self):
        directory_source = "images\\jpg"
        directory_target = "images\\backup"
        self.copy_files(directory_source, directory_target)
        file_paths = fs.get_images(directory_target)
        self.view(file_paths)
        cleaner.remove_metadata_multiple(file_paths)
        self.view(file_paths)


if __name__ == "__main__":
    unittest.main()
