from NodesDT import NodesDT;
from calcEntropy import calcEntropy;
from VarImpurityGain import VarImpurityGain;
from SelectAttribute import SelectAttribute;
from SelectAttributeImpurity import SelectAttributeImpurity;
from Utility import Utility;
import copy;
class makeTree():

    def makeTreeRecusive(self,node):
        
        for key in node.children:
            childNode = node.children[key];
            initEntOrVar=0.0;
            sa = None;
            if(self.heuristic ==1):
                entrObj = calcEntropy(childNode.yList);
                initEntOrVar = entrObj.getEntropy();
                sa = SelectAttribute(self.masterAttrDict,childNode.xList,childNode.yList,initEntOrVar,childNode.attrTaken);
            else:
                entrObj = VarImpurityGain(childNode.yList);
                initEntOrVar = entrObj.getVarImpurity();
                sa = SelectAttributeImpurity(self.masterAttrDict,childNode.xList,childNode.yList,initEntOrVar,childNode.attrTaken);
            childNode.entropy =initEntOrVar;
            
            if(initEntOrVar == 0.0 or (len(childNode.attrTaken)==len(self.masterAttrDict))):
                childNode.attrName = Utility.getMaxLabel(childNode.yList);
                continue;           
            childNode.attrName =sa.maxGainAttr;
            childNode.attrTaken[sa.maxGainAttr] = 'y';
            indexDict =sa.indexDict;
            
            for key1 in indexDict.keys():
                child = NodesDT();
                child.indexList = indexDict[key1];
                child.xList = Utility.getXlist(child.indexList,childNode.xList);
                child.yList = Utility.getYlist(child.indexList,childNode.yList);
                child.attrTaken = copy.copy(childNode.attrTaken);
                childNode.children[key1] =child;
                child.parent =childNode;
            self.makeTreeRecusive(childNode);
            

    def __init__(self,xMasterList,yMasterList,masterAttrDict,heuristic):
        self.xMasterList = xMasterList;
        self.yMasterList =yMasterList;
        self.heuristic = heuristic;
        self.masterAttrDict = masterAttrDict;

        self.root = NodesDT();
        indexDict ={};
        if(self.heuristic ==1):
            entrObj = calcEntropy(self.yMasterList);
            initEntropy = entrObj.getEntropy();
            sa = SelectAttribute(self.masterAttrDict,self.xMasterList,self.yMasterList,initEntropy);
            self.root.attrName = sa.maxGainAttr;
            self.root.entropy = initEntropy;
            self.root.attrTaken[self.root.attrName]='y';
            indexDict = sa.indexDict;
        else:
            impurityObj = VarImpurityGain(self.yMasterList);
            initImpurity = impurityObj.getVarImpurity();
            sa = SelectAttributeImpurity(self.masterAttrDict,self.xMasterList,self.yMasterList,initImpurity);
            self.root.attrName = sa.maxGainAttr;
            self.root.entropy = initImpurity;
            self.root.attrTaken[self.root.attrName]='y';
            indexDict = sa.indexDict;
            
        for key in indexDict.keys():
            child = NodesDT();
            child.indexList = indexDict[key];
            child.xList = Utility.getXlist(child.indexList,self.xMasterList);
            child.yList = Utility.getYlist(child.indexList,self.yMasterList);
            child.attrTaken = copy.copy(self.root.attrTaken);
            child.parent = self.root;
            self.root.children[key] =child;
        self.makeTreeRecusive(self.root);
            
