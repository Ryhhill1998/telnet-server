import subprocess
import os
from pathlib import Path

from classes.command_processors.abstract_command_processor import AbstractCommandProcessor


class TelnetCommandProcessor(AbstractCommandProcessor):

    def __init__(self):
        self.cwd = os.getcwd()

    def process(self, command: str) -> str:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, cwd=self.cwd)
            if result.returncode == 0:
                if command.startswith("cd "):
                    target_dir = command.split(" ")[1]
                    self.cwd = str(Path(self.cwd, target_dir))

                response = result.stdout.decode()
            else:
                response = result.stderr.decode()

            return response
        except Exception as e:
            print(f"Exception: {e}")
