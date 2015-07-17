import natlink
from natlinkutils import *

class ThisGrammar(GrammarBase):

    gramSpec = """
        <start> exported = demo sample one;
    """
    
    def gotResults_start(self,words,fullResults):
        natlink.playString('Heard macro "sample one"{enter}')

    def initialize(self):
        self.load(self.gramSpec)
        self.activateAll()
        
thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None

