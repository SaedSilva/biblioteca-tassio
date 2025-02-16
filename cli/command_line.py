from cli.auth import Auth


class CommandLine:
    def start(self):
        login = Auth()
        login.login()
