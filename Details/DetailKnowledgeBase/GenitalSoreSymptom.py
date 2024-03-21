from experta import *
from DetailFacts import DetailGenitalSoreFact
from DetailFacts import DetailResultFact


class GenitalSoreSymptom(KnowledgeEngine):
    # 1 VL
	@Rule(
            DetailGenitalSoreFact(
                sore_presence="y",
                gential_area="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 2

	@Rule(
            DetailGenitalSoreFact(
                sore_presence="y",
                gential_area="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 3

	@Rule(
            DetailGenitalSoreFact(
                sore_presence="n",
                gential_area="n"
            )
        )
	def very_likely_4(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
