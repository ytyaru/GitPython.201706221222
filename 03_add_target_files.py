import os.path
import subprocess
import shlex

def run_shell(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr, p.returncode

def get_line(std, is_delete_blank_line=False):
    stdout_str = std.decode('utf-8')
    for line in stdout_str.split('\n'):
        if is_delete_blank_line and 0 == len(line.strip()): continue
        yield line

# "add 'path'" -> "path"
def git_command_format(line):
    if line.startswith("add '"): line = line[5:]
    if line.endswith("'"): line = line[:-1]
    return line

def get_adding_files():
    stdout, stderr, returncode = run_shell("git add -n .")
    for line in get_line(stdout, is_delete_blank_line=True):
        line = git_command_format(line)
        yield line

for fn in get_adding_files(): print(fn)
