class ReadFile:
    def _getNumLines(self,filePath):
        self.num_lines =sum(1 for line in open(filePath));
    def __init__(self,filePath):
        self._getNumLines(filePath);
        self.fileObj=open(filePath);
    def getAttrDict(self):
        line1 = self.fileObj.next();
        rIndex = line1.rindex(',');
        line1 = line1[0:rIndex];
        list1 = line1.split(',');
        i=0;
        attrDict={};
        for x in list1:
            attrDict[x]=i;
            i+=1;
        self.attrDictMaster = attrDict;
        return attrDict;
    def getXValueMatrix(self):
        inputList=[];
        self.outputList=[];
        for i in range(1,self.num_lines):
            line = self.fileObj.next();
            index = line.rindex(',');
            line1 = line[0:index];
            inputList.append(line1.split(','));
            self.outputList.append(line[index+1:]);
        self.xList = inputList;
        return inputList;
    def getYValueMatrix(self):
        return self.outputList;
            
            
        
        
    
