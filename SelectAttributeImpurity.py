from VarImpurityGain import VarImpurityGain;
class SelectAttributeImpurity:

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
    def __init__(self,attrDict,xList,yList,initImpurity,attrTakenDict=None):
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
                varImpurity =0.0;
                for key2 in self.attrValueIndexDict:
                    entrObj = VarImpurityGain(yList,self.attrValueIndexDict[key2]);
                    length = len(self.attrValueIndexDict[key2]);
                    varImpurity =varImpurity+(entrObj.getVarImpurity()*length)/len(yList);
                gain = initImpurity - varImpurity;
                if(gain>self.maxGain):
                    self.maxGain = gain;
                    self.maxGainAttr = key;
                    self.indexDict = self.attrValueIndexDict;
                    
    
                    
                
                    
                                    
                
