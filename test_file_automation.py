import unittest
import os
import shutil

from main import MyHandler, FILE_PATH

class TestFileAutomation(unittest.TestCase):

    def setUp(self):
        #Set up test environment: Create a dummy download folder.
        self.test_folder = os.path.join(FILE_PATH, "Test_Downloads")
        self.test_file = os.path.join(self.test_folder, "test.mp4")
        self.destination_folder = os.path.join(FILE_PATH, "Downloaded_Videos")

        os.makedirs(self.test_folder, exist_ok=True)  # Create test download folder
        with open(self.test_file, "w") as f:  # Create a dummy file
            f.write("Test content")

    def tearDown(self):
        #Clean up after tests by removing test files and folders.
        shutil.rmtree(self.test_folder, ignore_errors=True)
        shutil.rmtree(self.destination_folder, ignore_errors=True)

    def test_file_movement(self):
        #Test if the process_file() function correctly moves a file.
        handler = MyHandler()
        handler.process_file(self.test_file, "Downloaded_Videos")

        expected_path = os.path.join(self.destination_folder, "test.mp4")
        self.assertTrue(os.path.exists(expected_path), "File was not moved correctly.")

    def test_nonexistent_file(self):
        #Ensure process_file() handles missing files gracefully.
        handler = MyHandler()
        fake_file = os.path.join(self.test_folder, "fake.mp4")

        handler.process_file(fake_file, "Downloaded_Videos")

        expected_path = os.path.join(self.destination_folder, "fake.mp4")
        self.assertFalse(os.path.exists(expected_path), "Nonexistent file should not be moved.")

if __name__ == "__main__":
    unittest.main()
