import subprocess

class MySubProcessException(subprocess.CalledProcessError):
    def __str__(self) -> str:
        print('Exception')
        return "Command not found"