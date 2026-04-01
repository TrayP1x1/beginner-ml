import sys
from pathlib import Path


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    template_dir = repo_root / "templates" / "test_ready_project"
    sys.path.insert(0, str(template_dir))

    from main import main as template_main

    template_main()


if __name__ == "__main__":
    main()
