from cli.auth import Auth


class CommandLine:
    def start(self):
        auth = Auth()
        while not auth.logged:
            auth.start()

        print("Você está logado!")