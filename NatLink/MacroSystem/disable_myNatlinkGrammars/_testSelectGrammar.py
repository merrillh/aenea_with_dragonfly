import sys
#from natlink import DictGramBase
import natlinkutils
from natlinkutils import SelectGramBase

#---------------------------------------------------------------------------
# Here we test recognition of selection grammars using SelectGramBase

def testSelectGram(self):
    self.log("testSelectGram")

    # Create a selection grammar.  This grammar simply gets the results of
    # the recognition and saves it in member variables.  It also contains
    # code to check for the results of the recognition.
    class TestSelectGram(SelectGramBase):

        def __init__(self):
            SelectGramBase.__init__(self, selectWords="select", throughWord='through')

        def gotBegin(self,moduleInfo):
            if self.sawBegin:
                self.error = 'Selection grammar called gotBegin twice'
            self.sawBegin = 1
            if moduleInfo != natlink.getCurrentModule():
                self.error = 'Invalid value for moduleInfo in SelectGramBase.gotBegin'

        def gotResultsObject(self,recogType,resObj):
            if self.recogType:
                self.error = 'Selection grammar called gotResultsObject twice'
            self.recogType = recogType

        def gotResults(self,words,start,end):
            if self.words:
                self.error = 'Selection grammar called gotResults twice'
            self.words = words
            self.start = start
            self.end = end

print >> sys.stderr, "loaded testSelectGrammar"
