from calEfficiency import calEfficiency;
import copy;
class PruneTree:
    def _getXList(self,indexList,masterXList):
        xList =[];
        for i in range(0,len(indexList)):
            xList.append(masterXList[indexList[i]]);
        return xList;
    def _getYList(self,indexList,masterYList):
        yList =[];
        for i in range(0,len(indexList)):
            yList.append(masterYList[indexList[i]]);
        return yList;
    def getLeafError(self,node):
        leafWrong =0;
        for key in node.children:
            childNode = node.children[key];
            if(childNode.attrName.find("1") != -1 or childNode.attrName.find("0") != -1):
               leafWrong = leafWrong + childNode.wrong;
               return leafWrong;
            else:
                leafWrong = self.getLeafError(childNode);
        return leafWrong;
    def makeAnother(self,node,root):
        for key in root.children:
            childNode = root.children[key];
            if(childNode.attrName == node.attrName):
                if(childNode.indexList == node.indexList):
                    childNode.attrName = childNode.key;
                    return;
                
            makeAnother(node,childNode);
        return root;

            
            
    

    def pruneRecursively(self,node,root,xMasterList,yMasterList):
        childWrong =0;
        children = node.children;
        for key in children:
            childNode = children[key];
            if(childNode.wrong ==0):
                xList = self._getXList(childNode.indexList,xMasterList);
                yList = self._getYList(childNode.indexList,yMasterList);
                self.pruneRecursively(childNode,root,xList,yList);
            if(childNode.wrong !=0):
                childWrong = childWrong +childNode.wrong;
        if(node != root):
            effObj1 = calEfficiency();
            currentWrong =effObj1.registerClassification(yMasterList,node.key);
            node.wrong = currentWrong;
            if(currentWrong<=childWrong):
                leafWrong = self.getLeafError(node);
                wrong = self.effObj.wrong-leafWrong;                
                if(node.key == ''): return ;                
                effObj1.wrong = currentWrong+wrong;
                effPercent = effObj1.calculateEfficiency(self.masterYList);
                if(self.accuracy<effPercent):
                    self.eficTreeRoot = self.makeAnother(node,copy.copy(root));
                    self.accuracy =effPercent;
                print effPercent;
                print effObj1.wrong
                label = node.key;
                print label;
                print '\n';
        

    def __init__(self,rootNode,accuracy,effObj,masterYList,masterXList,attrDict):
        self.rootNode = rootNode;
        self.accuracy = accuracy;
        self.effObj = effObj;
        self.masterYList = masterYList;
        self.masterXList = masterXList;
        self.attrDict =attrDict;
        self.lengthExample = len(masterYList);
        self.eficTreeRoot = None;
        print '\n';
        print self.effObj.wrong;
        self.pruneRecursively(rootNode,rootNode,masterXList,masterYList);
