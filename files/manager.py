import shutil
import os

class FileManager:
    @staticmethod
    def move(src, dst):
        shutil.move(src, dst)

    @staticmethod
    def copy(src, dst):
        shutil.copy(src, dst)

    @staticmethod
    def delete(path):
        if os.path.exists(path):
            os.remove(path)
