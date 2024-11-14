import subprocess


class Execute:
    def run(self, cmd):
        return subprocess.check_output(cmd, shell=True)
