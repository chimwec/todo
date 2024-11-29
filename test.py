import unittest
from unittest.mock import mock_open, patch
from todo import add_task



class TestAddTask(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_add_task_writes_to_file(self, mock_file):
        #Test adding a simple task
        add_task("my_task")
        
        # Assert the file was opened in append mode
        mock_file.assert_called_once_with("tasks.txt", "a")

        # Assert the task was written with a newline
        mock_file().write.assert_called_once_with("my_task\n")


    # i have to fix this 
    @patch("builtins.open", "mock_file")
    def test_list_task_display_to_file(self, mock_file):
        mock_open(read_data="tasks.txt")
        mock_file().assert_called_once_with("tasks.txt", "r")
        


if __name__ == "__main__":
    unittest.main()