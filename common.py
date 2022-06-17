import os
from pathlib import Path

CWD = Path(os.path.abspath(__file__)).parent

if __name__ == "__main__":
    print(CWD)