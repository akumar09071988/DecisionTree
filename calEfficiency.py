class calEfficiency:
    def __init__(self):
        self.wrong=0;
    def registerClassification(self,yList,label):
        currentWrong=0;
        if(label.find('1') != -1):
            for i in range(0,len(yList)):
                #print str(label)+'in label 1'+str(yList[i]);
                if(yList[i].find('0')!=-1):self.wrong+=1; currentWrong+=1;
        elif(label.find('0')!=-1):
            for i in range(0,len(yList)):
                #print str(label)+'in label 0'+str(yList[i]);
                if(yList[i].find('1')!=-1):self.wrong+=1;currentWrong+=1;
        return currentWrong;
    def calculateEfficiency(self,masterYList):
        totalExamples = len(masterYList);
        if(totalExamples == 0):return 0;
        error = float(self.wrong)/float(totalExamples);
        correctPercentage = (1-error)*100.00;
        return correctPercentage;
