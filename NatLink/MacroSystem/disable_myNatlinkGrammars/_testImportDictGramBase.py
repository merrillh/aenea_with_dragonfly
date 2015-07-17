import sys
#from natlink import DictGramBase
import natlinkutils
from natlinkutils import DictGramBase
class MyGrammar(DictGramBase):

    def __init__(self):
        DictGramBase.__init__(self)
        self.load()
        self.state = None
        self.isActive = 0

    def gotBegin(self, moduleInfo):
        print 'Start of recognition...'
        if not self.isActive:
            self.activate(moduleInfo[2])
            self.isActive = 1

    def gotResults(self, words):
        print 'Heard: <%s>' % string.join(words)
        output, self.state = nsformat.formatWords(words, self.state)
        print 'Formatted: <%s>' % output

print >> sys.stderr, "done loading MyGrammar"

#print >> sys.stderr, dir (natlink)