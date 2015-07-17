import natlink
from natlinkutils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <firstRule> exported = demo sample two [ help ];
        <secondRule> exported = demo sample two
            ( red | blue | green | purple | black | white | yellow |
              orange | magenta | cyan | gray );
    """
    
    def gotResults_firstRule(self,words,fullResults):
        natlink.playString('Say "demo sample two {ctrl+i}color{ctrl+i}"{enter}')

    def gotResults_secondRule(self,words,fullResults):
        natlink.playString('The color is "%s" {enter}'%words[3])
        
    def initialize(self):
        self.load(self.gramSpec)
        self.activateAll()
        
thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None

