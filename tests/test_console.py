import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import models

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.do_quit("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.do_EOF("")
        self.assertEqual(mock_stdout.getvalue(), "\n")

    @unittest.skipIf(isinstance(models.storage, DBStorage), "Skipping test for DBStorage")
    def test_do_create(self):
        from models.base_model import BaseModel
        import json
        obj = BaseModel()
        obj.name = "TestObject"

        self.storage.new(obj)
        self.storage.save()

        with open("file.json", "r") as f:
            data = json.load(f)
            obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.assertTrue(obj_key in data)

        self.assertIn(obj.id, unittest.mock_stdout.getvalue())


    @unittest.skipIf(isinstance(models.storage, FileStorage), "Skipping test for FileStorage")
    def test_do_show(self):
        self.storage.show("BaseModel", self.obj.id)

        self.assertIn("TestObject", unittest.mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()