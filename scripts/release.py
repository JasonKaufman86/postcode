import subprocess
import sys


class Version:
    """A class to represent a version with major, minor, and patch components."""

    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        """Return the version as a string in the format 'major.minor.patch'."""
        return f"{self.major}.{self.minor}.{self.patch}"

    @staticmethod
    def from_string(version: str):
        """Create a Version instance from a version string."""
        parts = version.split(".")
        if len(parts) != 3:
            raise ValueError("Version must be in the format 'major.minor.patch'")

        if not all(part.isdigit() for part in parts):
            raise ValueError("All parts of the version must be integers")

        major, minor, patch = map(int, parts)
        if not all(0 <= part <= 99 for part in (major, minor, patch)):
            raise ValueError("Version parts must be between 0 and 99 inclusive")

        return Version(major, minor, patch)


def main():
    """Create a new release by tagging the current commit in the Git repository."""
    try:
        version = Version.from_string(
            input("Enter release version (e.g. 1.2.3): ").strip()
        )
    except ValueError as e:
        print(f"Invalid version: {e}")
        sys.exit(1)

    if input(f"Create release tag 'v{version}'? (y/n): ").strip().lower() != "y":
        print("Release cancelled.")
        sys.exit(0)

    tag = f"v{version}"

    print(f"Creating release for version {tag}...")
    try:
        subprocess.run(["git", "tag", tag], check=True)
        subprocess.run(["git", "push", "origin", tag], check=True)
        print(f"Release {tag} created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating release: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
