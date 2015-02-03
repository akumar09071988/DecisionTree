class VarImpurityGain:

    def _calcFractions(self,yList):
        self.yDict={};
        for i in range(0,len(yList)):
            if(self.yDict.has_key(yList[i])):
                self.yDict[yList[i]]=self.yDict[yList[i]]+1;
            else:self.yDict[yList[i]] =1;
        self.fractionList =[];
        for key in self.yDict.keys():
            self.fractionList.append(float(self.yDict[key])/len(yList));
    def _varImpurity(self):
        self.impurity = 1.0;
        for i in range(0,len(self.fractionList)):
            fraction = self.fractionList[i];
            self.impurity = self.impurity *fraction;
        
    
    def __init__(self,yValueList,exampleIndexList=None):
        if(exampleIndexList==None or len(exampleIndexList)==0):
            self._calcFractions(yValueList);
        else:
            yList =[];
            for i in range(0,len(exampleIndexList)):
                yList.append(yValueList[exampleIndexList[i]]);
            self._calcFractions(yList);
        self._varImpurity();
    def getVarImpurity(self):
        return self.impurity;
            
        
        
        
