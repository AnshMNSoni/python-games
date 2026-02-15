"""
Tests for the game launcher.
Tests folder existence, error handling, and module imports.
"""
import unittest
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT_DIR)


class TestLauncherFolders(unittest.TestCase):
    """Test cases for game folder validation."""

    def test_all_game_folders_exist(self):
        """Verify all games in the launcher map to real directories."""
        from banner import games
        for game_name, folder in games.items():
            game_path = os.path.join(ROOT_DIR, folder)
            self.assertTrue(
                os.path.isdir(game_path),
                f"Game folder '{folder}' does not exist"
            )


class TestRunGame(unittest.TestCase):
    """Test cases for run_game function."""

    def test_run_game_handles_invalid_folder(self):
        """Verify run_game doesn't crash on invalid folder."""
        from banner import run_game
        # Should print error, not raise exception
        run_game("nonexistent_game_folder")  # No handling needed here just shouldn't crash


class TestBannerModule(unittest.TestCase):
    """Test cases for banner module imports."""

    def test_banner_module_imports(self):
        """Ensure the module loads without errors."""
        import banner
        self.assertTrue(hasattr(banner, 'main'))
        self.assertTrue(hasattr(banner, 'run_game'))
        self.assertTrue(hasattr(banner, 'games'))

    def test_games_dict_not_empty(self):
        """Verify games dictionary is populated."""
        from banner import games
        self.assertGreater(len(games), 0, "Games dictionary should not be empty")


if __name__ == "__main__":
    unittest.main()
