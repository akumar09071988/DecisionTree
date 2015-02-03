from NodesDT import NodesDT;
class TraverseTree:

    def _traverse(self ,node,str1):
        for key in node.children:
            print str1+node.attrName +'= '+key;
            print '|  ';
            #str1 =str1+'   ';
            self._traverse(node.children[key],str1+'  ');
            
    def __init__(self,rootNode):
        self._traverse(rootNode,'');
        
