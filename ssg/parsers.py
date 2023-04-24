from typing import List
from pathlib import Path

class Parser:
    
    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        else:
            return False
    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError('Not done yet!')

    def read(self, path):
        with open(path) as file:
            


