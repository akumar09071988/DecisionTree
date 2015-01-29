from FileProcess import ReadFile;
from calcEntropy import calcEntropy;
from SelectAttribute import SelectAttribute;
from PopulateTree import PopulateTree;
from Nodes import Nodes;
from TraverseTree import TraverseTree;

fp = ReadFile('book_example.csv');

def _createLeaf(yList):
    entrObj = calcEntropy(yList);
    print entrObj.getEntropy();
    if(entrObj.getEntropy() ==0.0):
        leave = Nodes();
        return leave;
    else: return None;
def _getXList(indexList,masterList):
    xList =[];
    for i in range(0,len(indexList)):
        xList.append(masterList[indexList[i]]);
    return xList;
def _getYList(indexList,masterYList):
    yList=[];
    for i in range(0,len(indexList)):
        yList.append(masterYList[indexList[i]]);
    return yList;


def _makeTree(node):
    for key in node.children:
        childNode = node.children[key];
        print '_maketree '+ key;
        attrDict = fp.attrDictMaster;
        xMasterList =fp.xList;
        yMasterList = fp.getYValueMatrix();
        xList = _getXList(childNode.indexList,xMasterList);
        yList =_getYList(childNode.indexList,yMasterList);
        entrObj = calcEntropy(yList);
        initEntropy = entrObj.getEntropy();
        print 'entropy :'+str(initEntropy);
        if(initEntropy == 0.0):
            childNode.setAttribute(yList[0]);
            childNode.setEntropy(initEntropy);
            print 'end';
            continue;
        sa = SelectAttribute(attrDict,xList,yList,initEntropy,childNode.attrTaken);
        print sa.maxGainAttr;
        childNode.setAttribute(sa.maxGainAttr);
        childNode.setEntropy(initEntropy);
        childNode.attrTaken[sa.maxGainAttr] = 'y';
        indexDict =sa.indexDict;
        for key1 in indexDict.keys():
            child = Nodes();
            child.indexList = indexDict[key1];
            child.attrTaken = childNode.attrTaken;
            childNode.children[key1] =child;
        _makeTree(childNode);
    print 'finished';
  
def main() :
    
    attrDict = fp.getAttrDict();
    xList = fp.getXValueMatrix();
    yList = fp.getYValueMatrix();
    entrObj = calcEntropy(yList);
    initEntropy = entrObj.getEntropy();
    sa = SelectAttribute(attrDict,xList,yList,initEntropy);
    print sa.maxGainAttr;
    print sa.maxGain;
    #recObj = PopulateTree();
    #recObj.recursion(0);
    root = Nodes();
    root.attrName = sa.maxGainAttr;
    root.entropy = initEntropy;
    root.attrTaken[root.attrName]='y';
    indexDict = sa.indexDict;
    for key in indexDict.keys():
        child = Nodes();
        child.indexList = indexDict[key];
        child.attrTaken = root.attrTaken;
        root.children[key] =child;
    print root.children;
    _makeTree(root);
    travrse = TraverseTree(root);
        
    

if __name__ == '__main__':
    main()
    
        
    
    
