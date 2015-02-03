class Utility:
    @staticmethod
    def getXlist(indexList,masterList):
        xList =[];
        for i in range(0,len(indexList)):
            xList.append(masterList[indexList[i]]);
        return xList;
    @staticmethod
    def getYlist(indexList,masterYList):
        yList=[];
        for i in range(0,len(indexList)):
            yList.append(masterYList[indexList[i]]);
        return yList;
    @staticmethod
    def getMaxLabel(yList):
        oneLabel =0;
        zeroLabel =1;
        for i in range(0,len(yList)):
            if(yList[i].find('1')!=-1):oneLabel+=1;
            elif(yList[i].find('0')!=-1):zeroLabel+=1;
        if(oneLabel>zeroLabel): return '1';
        else:return '0';
    @staticmethod
    def getIndexList(val,xMasterList,index):
        indexList=[];
        for i in range(0,len(xMasterList)):
                       if(xMasterList[i][index]==val):
                           indexList.append(i);
        #print len(indexList);
        return indexList;
    @staticmethod
    def convertTreeToList(root):
        treeList=[];
        queueList =[];
        index =0;
        queueList.append(root);
        while(index<len(queueList)):
            node = queueList[index];
            treeList.append(node);
            for key in node.children:
                childNode = node.children[key];
                if(childNode.attrName.find('1')!=-1 or childNode.attrName.find('0')!=-1):
                    continue;
                else:
                    queueList.append(childNode);
            index+=1;
        return treeList;
                
            
        
