import unittest

class TestCosmicHeatImport(unittest.TestCase):

    def test_import_main(self):
        import CosmicHeat.main

    def test_import_menu(self):
        import CosmicHeat.menu

    def test_import_functions(self):
        import CosmicHeat.functions


if __name__ == "__main__":
    unittest.main()

