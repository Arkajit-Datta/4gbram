import os

THIS_FILE = os.path.dirname(os.path.abspath(__file__))
PROJ_FILE = os.path.abspath(os.path.join(THIS_FILE, "../"))

class GetComment:
    def __init__(self) -> None:
        pass
    def checkdb_commentry(self):
        return  1,PROJ_FILE + '/audio/commentry.mp3'