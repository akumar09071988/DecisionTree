from math import log;

class calcEntropy:
    def _calcFractions(self,yList):
        self.yDict={};
        #print 'fractions';
        for i in range(0,len(yList)):
            if(self.yDict.has_key(yList[i])):
                self.yDict[yList[i]]=self.yDict[yList[i]]+1;
            else:
                #print 'new';
                self.yDict[yList[i]] =1;
        self.fractionList =[];
        index=0;
        #print 'b4 loop';
        for key in self.yDict.keys():
            #print key;
            self.fractionList.append(float(self.yDict[key])/len(yList));
            index+=1;
    def _calcEntropy(self):
        self.entropy = 0.0;
        for i in range(0,len(self.fractionList)):
            fraction = self.fractionList[i];
            self.entropy = self.entropy +fraction*log(fraction);
        self.entropy = -1.0*self.entropy;
    
    
    def __init__(self,yValueList,exampleIndexList=None):
        if(exampleIndexList==None or len(exampleIndexList)==0):
            self._calcFractions(yValueList);
            print len(self.fractionList);
        else:
            yList =[];
            for i in range(0,len(exampleIndexList)):
                yList.append(yValueList[exampleIndexList[i]]);
            self._calcFractions(yList);
        self._calcEntropy();

    def getEntropy(self):
        return self.entropy;
                
            
            
    

            
    
