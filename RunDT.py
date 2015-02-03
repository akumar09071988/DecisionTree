from FileProcess import ReadFile;
from calcEntropy import calcEntropy;
from VarImpurityGain import VarImpurityGain;
from SelectAttribute import SelectAttribute;
from SelectAttributeImpurity import SelectAttributeImpurity;
from PopulateTree import PopulateTree;
from Nodes import Nodes;
from TraverseTree import TraverseTree;
from calEfficiency import calEfficiency;
from PruneTree import PruneTree;
from makeTree import makeTree;
from NodesDT import NodesDT;
from Efficiency import Efficiency;
from Predict import Predict;
from PostPruneTree import PostPruneTree;

fp = ReadFile('training_set.csv');
fp1 = ReadFile('validation_set.csv');
calEffObj = calEfficiency();
calEffObj1 = calEfficiency();

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
def _makeTree1(node,xMasterList,yMasterList):
    for key in node.children:
        childNode = node.children[key];
        attrDict = fp.attrDictMaster;
        xList = _getXList(childNode.indexList,xMasterList);
        yList =_getYList(childNode.indexList,yMasterList);
        entrObj = VarImpurityGain(yList);
        initEntropy = entrObj.getVarImpurity();
        if(initEntropy == 0.0):
            childNode.setAttribute(yList[0]);
            childNode.setEntropy(initEntropy);
            calEffObj.registerClassification(yList,childNode.attrName);
            continue;
        sa = SelectAttributeImpurity(attrDict,xList,yList,initEntropy,childNode.attrTaken);
        childNode.setAttribute(sa.maxGainAttr);
        childNode.setEntropy(initEntropy);
        childNode.attrTaken[sa.maxGainAttr] = 'y';
        indexDict =sa.indexDict;
        for key1 in indexDict.keys():
            child = Nodes();
            child.indexList = indexDict[key1];
            child.attrTaken = childNode.attrTaken;
            child.key = key1;
            childNode.children[key1] =child;
        _makeTree1(childNode,xList,yList);


def _makeTree(node,xMasterList,yMasterList):
    for key in node.children:
        childNode = node.children[key];
        #print '_maketree '+ key;
        attrDict = fp.attrDictMaster;
        #xMasterList =fp.xList;
        #yMasterList = fp.getYValueMatrix();
        xList = _getXList(childNode.indexList,xMasterList);
        yList =_getYList(childNode.indexList,yMasterList);
        entrObj = calcEntropy(yList);
        initEntropy = entrObj.getEntropy();
        #print 'entropy :'+str(initEntropy);
        if(initEntropy == 0.0):
            childNode.setAttribute(yList[0]);
            #print childNode.attrName;
            #print yList;
            childNode.setEntropy(initEntropy);
            calEffObj.registerClassification(yList,childNode.attrName);
            #print 'end';
            continue;
        sa = SelectAttribute(attrDict,xList,yList,initEntropy,childNode.attrTaken);
        #print sa.maxGainAttr;
        childNode.setAttribute(sa.maxGainAttr);
        childNode.setEntropy(initEntropy);
        childNode.attrTaken[sa.maxGainAttr] = 'y';
        indexDict =sa.indexDict;
        for key1 in indexDict.keys():
            child = Nodes();
            child.indexList = indexDict[key1];
            child.attrTaken = childNode.attrTaken;
            child.key = key1;
            childNode.children[key1] =child;
        _makeTree(childNode,xList,yList);
    #print 'finished';

def _getIndexList(val,xMasterList,index):
    indexList=[];
    for i in range(0,len(xMasterList)):
                   if(xMasterList[i][index]==val):
                       indexList.append(i);
    print len(indexList);
    return indexList;

def predict(node,xMasterList,yMasterList):
    attrDict = fp1.attrDictMaster;
    #xMasterList =fp1.xList;
    #yMasterList =fp1.getYValueMatrix();
    
    if(node.attrName.find('1') != -1):
        node.wrong = calEffObj1.registerClassification(yMasterList,node.attrName);
        return;
    if(node.attrName.find('0')!= -1):
        node.wrong = calEffObj1.registerClassification(yMasterList,node.attrName);
        return;
    if(attrDict.has_key(node.attrName)):
           index =attrDict[node.attrName];
           for key in node.children:           
            node.children[key].indexList = _getIndexList(key,xMasterList,index);
            xList = _getXList(node.children[key].indexList,xMasterList);
            yList =_getYList(node.children[key].indexList,yMasterList);
            predict(node.children[key],xList,yList);
            
    
  
def main1() :
    
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
    _makeTree(root,xList,yList);
    travrse = TraverseTree(root);
    print calEffObj.calculateEfficiency(yList);
    fp1.getAttrDict();
    xMaster =fp1.getXValueMatrix();
    yMaster =fp1.getYValueMatrix();
    root.indexList=None;
    predict(root,xMaster,yMaster);
    accuracy =calEffObj1.calculateEfficiency(fp1.getYValueMatrix());
    print len(fp1.getYValueMatrix());
    print calEffObj1.wrong
    print calEffObj1.calculateEfficiency(fp1.getYValueMatrix());
    prune = PruneTree(root,accuracy,calEffObj1,yMaster,xMaster,fp1.attrDictMaster);
    #travrse = TraverseTree(root);

    root1 = Nodes();
    impurityObj = VarImpurityGain(yList);
    initImpurity = impurityObj.getVarImpurity();
    sa1 = SelectAttributeImpurity(attrDict,xList,yList,initImpurity);
    root1.attrName = sa1.maxGainAttr;
    root1.entropy = initImpurity;
    root1.attrTaken[root1.attrName]='y';
    indexDict1 = sa1.indexDict;
    for key in indexDict.keys():
        child = Nodes();
        child.indexList = indexDict[key];
        child.attrTaken = root1.attrTaken;
        root1.children[key] = child;
    _makeTree1(root1,xList,yList);
    TraverseTree(root1);
def main():
    attrDict = fp.getAttrDict();
    xList = fp.getXValueMatrix();
    yList = fp.getYValueMatrix();
    treeObj = makeTree(xList,yList,attrDict,2);
    print treeObj.root.attrName;
    TraverseTree(treeObj.root);
    eff1 =Efficiency(treeObj.root,len(yList));
    print eff1.accuracy;
    attrDict1 = fp1.getAttrDict();
    xList1 = fp1.getXValueMatrix();
    yList1 = fp1.getYValueMatrix();
    pre = Predict(treeObj.root,xList1,yList1,attrDict1);
    eff2 = Efficiency(pre.root,len(yList1));
    print eff2.accuracy;
    eff3 = Efficiency(treeObj.root,len(yList1));
    print eff3.accuracy;
    print "after traversing";
    postPruneObj = PostPruneTree(20,30,pre.root,eff3.accuracy,len(yList1));
    print postPruneObj.accuracy;
    #TraverseTree(postPruneObj.bestDtree);
    #TraverseTree(pre.root);
if __name__ == '__main__':
    main()
    
        
    
    
