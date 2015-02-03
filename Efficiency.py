from NodesDT import NodesDT;
class Efficiency():

    def calculateWrong(self,node):
        label = node.attrName;
        yList = node.yList;
        for i in range(0,len(yList)):
            if(yList[i].find(label)==-1):self.wrong+=1;
    def calculateEfficiency(self):
        wrongFraction = float(self.wrong)/float(self.totalExamples);
        self.accuracy =(1-wrongFraction)*100.00; 
            
    def traverseToLeaf(self,node):
        for key in node.children:
            child = node.children[key];
            if(child.attrName.find('0')!=-1 or child.attrName.find('1')!=-1):
                self.calculateWrong(child);
                continue;
            else:
                self.traverseToLeaf(child);

    def __init__(self,root,totalExamples):
        self.root =root;
        self.wrong =0;
        self.totalExamples = totalExamples;
        self.traverseToLeaf(self.root);
        self.calculateEfficiency();
