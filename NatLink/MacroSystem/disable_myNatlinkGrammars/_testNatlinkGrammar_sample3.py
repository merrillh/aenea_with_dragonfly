import natlink
from natlinkutils import *

class ThisGrammar(GrammarBase):

	gramSpec = """
		<mainRule> exported = okay <ruleOne>;
		<ruleOne> = demo <ruleTwo> now please;
		<ruleTwo> = sample three;
	"""

	def gotResults_mainRule(self,words,fullResults):
		natlink.playString('Saw <mainRule> = %s{enter}' % repr(words))

	def gotResults_ruleOne(self,words,fullResults):
		natlink.playString('Saw <ruleOne> = %s{enter}' % repr(words))
		
	def gotResults_ruleTwo(self,words,fullResults):
		natlink.playString('Saw <ruleTwo> = %s{enter}' % repr(words))
					
	def initialize(self):
		self.load(self.gramSpec)
		self.activateAll()
        
thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None

