class Nodes:
             

             def __init__(self) : 
                                                self.attrName = '';
                                                self.children = {};
                                                self.entropy=0.0;
                                                self.attrTaken={};
                                                self.indexList =[];
                                                self.wrong=0;
                                                self.key='';
                                                
                                                

             def displayAttrName(self):
             	                       print self.value;
             def setAttribute(self,attribute):
                 self.attrName = attribute;
             def setEntropy(self,entropy):
                 self.entropy =entropy;
             def setAttributeTaken(self,attributeTaken):
                 self.attrTaken = attributeTaken
                                    
