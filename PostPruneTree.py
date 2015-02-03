import copy;
import random;
from Utility import Utility;
from Efficiency import Efficiency;
class PostPruneTree:

                
    def prune(self,bestTree):
        for i in range(0,self.L):
            #print 'in firstTree';
            dTree = copy.deepcopy(bestTree);
            M = random.randint(1,self.K);
            for m in range(1,M):
                #print 'in second tree';
                treeList = Utility.convertTreeToList(dTree);
                length = len(treeList);
                #print str(length)+"::: ";
                if(length <=1):break;
                P = random.randint(1,length-1);
                #print str(length)+" "+str(P);
                node = treeList[P];
                if(node.parent.attrName.find('0')!=-1 or node.parent.attrName.find('1')!=-1 or node.attrName.find('0')!=-1 or node.attrName.find('1')!=-1):
                    m-=1;
                else:
                    node.attrName = Utility.getMaxLabel(node.yList);
                    #print "in removig "+node.attrName;
                    node.children.clear();
            eff = Efficiency(dTree,self.totalExamples);
            #print eff.accuracy;
            if(eff.accuracy>self.accuracy):
                self.bestDtree = copy.copy(dTree);
                self.accuracy = eff.accuracy;           


    def __init__(self,L,K,root,accuracy,totalExamples):
        self.L = L;
        self.K = K;
        self.bestDtree = root;
        self.accuracy =accuracy;
        self.totalExamples = totalExamples;
        self.prune(self.bestDtree);
        
