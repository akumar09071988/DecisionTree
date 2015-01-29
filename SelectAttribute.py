from calcEntropy import calcEntropy;
class SelectAttribute:

    def _calcRangeForAttr(self,xList,index):
        self.attrValueIndexDict={};
        for i in range(0,len(xList)):
            val = xList[i][index];
            if(self.attrValueIndexDict.has_key(val)==False):
                list1 =[i];
                self.attrValueIndexDict[val]=list1;
            else:
                list1 = self.attrValueIndexDict[val];
                list1.append(i);
                self.attrValueIndexDict[val] = list1;
    def __init__(self,attrDict,xList,yList,initEntropy,attrTakenDict=None):
            self.maxGain = 0.0;
            self.maxGainAttr ='';
            self.indexDict={};
            for key in attrDict:
                if(attrTakenDict != None):
                    if(attrTakenDict.has_key(key)):
                        continue;
                index = attrDict[key];
                self._calcRangeForAttr(xList,index);
                entropyList=[];
                entropy =0.0;
                for key2 in self.attrValueIndexDict:
                    entrObj = calcEntropy(yList,self.attrValueIndexDict[key2]);
                    length = len(self.attrValueIndexDict[key2]);
                    entropy =entropy+(entrObj.getEntropy()*length)/len(yList);
                gain = initEntropy - entropy;
                if(gain>self.maxGain):
                    self.maxGain = gain;
                    self.maxGainAttr = key;
                    self.indexDict = self.attrValueIndexDict;
                    
    
                    
                
                    
                                    
                
