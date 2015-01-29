class PopulateTree:
    def _rec(self,val):
        if(val == self.limit):
            print 'g';
            return 'hahahaa';
        else:
            val=val+1l;
            print 'l';
            return self._rec(val);


    def __init__(self):
        self.limit =3;
        print self._rec(0);
    

