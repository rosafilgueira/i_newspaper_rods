import requests
import subprocess
from secrets import password
from StringIO import StringIO

class TDAIRodsManager:
    def __init__(self,
                 path="/rdZone/live/rd009s/2TB-Drive-Transfer-06-07-q2016/TDA_GDA_1785-2009"
                 ):
        self.path = path
        self.store = None

    def get_all_object_IDs_and_store(self):
        args = ["iquest","--no-page",'"%s"',
                '"SELECT DATA_PATH where COLL_NAME like '+
                "'"+self.path+"%' "+
                "and DATA_NAME like '%.xml' and DATA_RESC_HIER = 'wos;wosArchive'"+
                '"']
        results=subprocess.Popen(args, stdout=subprocess.PIPE)
        res = results.communicate()[0].split('\n')[:-1]
        self.store=map(lambda x:x[1:-1], res) # Remove initial and final quote

    def __len__(self):
        if not self.store:
            self.get_all_object_IDs_and_store()

        return len(self.store)

    def __getitem__(self, index):
        if not self.store:
            self.get_all_object_IDs_and_store()

        oid= self.store[index]
        path = 'http://arthur.rd.ucl.ac.uk/objects/'+oid
        result= requests.get('http://arthur.rd.ucl.ac.uk/objects/'+oid,
                stream=True)
        return result.iter_content(4096)
