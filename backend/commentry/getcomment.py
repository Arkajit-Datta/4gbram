import os
import json
THIS_FILE = os.path.dirname(os.path.abspath(__file__))
PROJ_FILE = os.path.abspath(os.path.join(THIS_FILE, "../"))
db_path = PROJ_FILE + '/commentry/db.json'
class GetComment:
    def __init__(self) -> None:
        pass
    def checkdb_commentry(self):
        f = open(db_path,'r')
        l = json.load(f)
        f.close()
        if l["1"] == []:
            return 0
        else:
            path = l["1"][0]
            l["1"].remove(l["1"][0])
            f = open(db_path,'w')
            json.dump(l,f)
            f.close()
            return  1,path
f = GetComment()
print(f.checkdb_commentry())