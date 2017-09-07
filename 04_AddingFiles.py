import os.path
import subprocess
import shlex
class AddingFiles:
    @property
    def Files(self): return self.__get_adding_files()

    def __get_adding_files(self):
        stdout, stderr, returncode = self.__run_shell("git add -n .")
        for line in self.__get_line(stdout, is_delete_blank_line=True):
            line = self.__git_command_format(line)
            yield line
    
    # "add 'path'" -> "path"
    def __git_command_format(self, line):
        if line.startswith("add '"): line = line[5:]
        if line.endswith("'"): line = line[:-1]
        return line
    
    def __get_line(self, std, is_delete_blank_line=False):
        stdout_str = std.decode('utf-8')
        for line in stdout_str.split('\n'):
            if is_delete_blank_line and 0 == len(line.strip()): continue
            yield line
    
    def __run_shell(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return stdout, stderr, p.returncode


if __name__ == '__main__':
    f = AddingFiles()
    for f in f.Files: print(f)
