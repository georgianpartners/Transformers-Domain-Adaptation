"""Utility module for interacting with the shell."""
import shlex
from subprocess import run, Popen, PIPE


def run_shell(cmd: str) -> str:
    """Run a shell command using the subprocess module."""
    process = run(shlex.split(cmd),
               stdout=PIPE, stderr=PIPE,
               check=False, universal_newlines=True)
    if process.returncode:
        raise ValueError(process.stderr)
    return process.stdout


def is_file_in_use(filename: str) -> bool:
    """Check if a file is being used by other processes."""
    lsout = Popen(shlex.split(f'lsof {filename}'), stdout=PIPE)
    output = run(shlex.split(f'grep {filename}'), stdin=lsout.stdout)
    return not output.returncode
