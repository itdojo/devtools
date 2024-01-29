"""
This module provides functionality to execute shell 
commands from within Python.

It uses the subprocess module to safely execute shell 
commands and capture their output.

Function:
    run_shell_cmd(cmd):
        Executes a given shell command and returns 
        its standard output and standard error.

        This function takes a shell command as a string, 
        splits it into a list of arguments,
        and then executes it using subprocess.Popen. The 
        standard output (stdout) and standard
        error (stderr) of the command are captured and 
        returned.

        The function prints the stdout and stderr to the 
        console, which can be useful for debugging or 
        logging purposes.

Parameters:
    cmd (str): The shell command to be executed.

Returns:
    list: A list containing two elements - the standard 
    output and standard error of the executed command.

        The first element of the list is the standard 
        output (stdout) of the command.
        The second element is the standard error (stderr).

Example:
    >>> run_shell_cmd("echo Hello World")
    stdout: b'Hello World\n'
    stderr: b''
    [b'Hello World\n', b'']

Note:
    - The command is executed in a separate process, and 
    this function waits for it to complete.
    - This function should be used with caution, especially 
    when executing commands from untrusted sources, as it can 
    pose security risks.
"""

import subprocess

def run_shell_cmd(cmd):
    """
    Executes a given shell command and captures its standard 
    output and error.

    Parameters:
    cmd (str): The shell command to be executed.

    Returns:
    list: A list containing the standard output and standard 
    error from the executed command.
    """
    process = subprocess.Popen(
        cmd.split(),
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # print(f"stdout: {stdout}")
    # print(f"stderr: {stderr}")
    return [stdout.decode(), stderr.decode()]
