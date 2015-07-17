import natlink
from natlinkutils import *

class ThisGrammar(GrammarBase):

	gramSpec = """
		<dgnwords> imported;
		<dgndictation> imported;
		<mainRule> exported = snake <dgndictation> ;
		<dunder> exported = dunder <dgndictation> ;
	"""

	def gotResults_mainRule(self,words,fullResults):
		natlink.playString('Saw <mainRule> = %s{enter}' % repr(words))
	def gotResults_dgnwords(self,words,fullResults):
		#natlink.playString('Saw <dgnwords> = %s{enter}' % "_".join(words))
		natlink.playString('Saw <dgnwords> = %s{enter}' % repr(words))
	def gotResults_dgndictation(self,words,fullResults):
		natlink.playString('Saw <dgndictation> = %s{enter}' % "_".join(words))
	def gotResults_dgndictation(self,words,fullResults):
		natlink.playString('__%s__' % "_".join(words))
		
	def initialize(self):
		self.load(self.gramSpec)
		self.activateAll()
        
thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None

