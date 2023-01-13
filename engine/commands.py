class commands:
    def __init__(self, *args, **kwargs):
        self.commands = {
            '/pixelImage': self.pixelImage,
            '/pixelCommands': self.pixelCommands,
        }

    def pixelImage(self, *args, **kwargs):
        return 'https://media.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif'

    def pixelCommands(self):
        return 'PixelBot commands are: ' + ', '.join(self.commands.keys())