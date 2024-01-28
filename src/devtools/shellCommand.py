import subprocess


def run_shell_cmd(cmd):
    process = subprocess.Popen(
        cmd.split(),
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")
    return [stdout, stderr]