import natlink
from natlinkutils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <firstRule> exported = sample four [ help ];
        <secondRule> exported = sample four
            ( red | blue | green | purple | black | white | yellow |
              orange | magenta | cyan | gray );
    """
    def gotResultsInit(self,words,fullResults):
		natlink.playString('INIT "%s" {enter}'%words)
    def gotResults_firstRule(self,words,fullResults):
        natlink.playString('Say "demo sample two {ctrl+i}color{ctrl+i}"{enter}')

    def gotResults_secondRule(self,words,fullResults):
        natlink.playString('The color is "%s" {enter}'%words[len(words)-1])
    def gotResults(self,words,fullResults):
		natlink.playString('FINAL "%s" {enter}'%words)
        
    def initialize(self):
        self.load(self.gramSpec)
        self.activateAll()
        
thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None

