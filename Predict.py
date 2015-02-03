from Utility import Utility;
from NodesDT import NodesDT;
class Predict():

    def predict(self,node,masterXList,masterYList):
        if(node.attrName.find('0')!=-1 or node.attrName.find('1')!=-1 ):return;
        if(not self.attrDictMaster.has_key(node.attrName)):return;
        index = self.attrDictMaster[node.attrName];
        for key in node.children:
            node.children[key].indexList = Utility.getIndexList(key,masterXList,index);
            node.children[key].xList= Utility.getXlist(node.children[key].indexList,masterXList);
            node.children[key].yList= Utility.getYlist(node.children[key].indexList,masterYList);
            self.predict(node.children[key],node.children[key].xList,node.children[key].yList);
            
    def __init__(self,root,masterXList,masterYList,attrDictMaster):
        self.root = root;
        self.masterXList = masterXList;
        self.masterYList = masterYList;
        self.attrDictMaster = attrDictMaster;
        self.predict(self.root,masterXList,masterYList);
        
