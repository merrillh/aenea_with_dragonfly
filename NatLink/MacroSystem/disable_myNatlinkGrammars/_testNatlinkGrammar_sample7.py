import natlink
from natlinkutils import *
import sys

class ThisGrammar(GrammarBase):

    gramSpec = """
        <firstRule> exported = sample seven [ help ];
        <secondRule> exported = sample four
            ( red | blue | green | purple | black | white | yellow |
              orange | magenta | cyan | gray );
    """
    def gotResultsInit(self,words,fullResults):
        natlink.playString('# INIT "%s" {enter}'%words)
    def gotResults_firstRule(self,words,fullResults):
        natlink.playString('# Say "demo sample two {ctrl+i}color{ctrl+i}"{enter}')

    def gotResults_secondRule(self,words,fullResults):
        natlink.playString('# The color is "%s" {enter}'%words[len(words)-1])
    def gotResults(self,words,fullResults):
        natlink.playString('# FINAL "%s" {enter}'%words)
        #self.gotBegin("test")

    def initialize(self):
        self.load(self.gramSpec)
        self.activateAll()
    def gotBegin(self, moduleInfo):
        print >> sys.stderr, 'spam'
        #print('spam', file=sys.stderr)
        print "---------------------------------------------------------Hi there"
        print ("moduleInfo=%s" % repr(moduleInfo))

        print 'attempt to match the window title'
        winHandle=matchWindow(moduleInfo,'powershell', 'PowerShell')
        if winHandle:
            print ("window=%s" % winHandle)
            self.activateAll(window=winHandle)
        else:
            print "no match"
        result = os.path.splitext(os.path.split(moduleInfo[0])[1])[0]
        print result
        print "moduleInfo[i]= ", moduleInfo[1]
        print moduleInfo[1].find('PowerShell')
        #os.path.splitext(os.path.split(name)[1])[0]
        #getBaseName(moduleInfo[0]).lower()


thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None

