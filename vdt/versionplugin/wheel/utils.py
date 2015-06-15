from setuptools.dist import Distribution


class WheelRunningDistribution(Distribution):
    def parse_command_line(self):
        self.commands = ['wheel']
        return 1
    #
    # def run_commands()