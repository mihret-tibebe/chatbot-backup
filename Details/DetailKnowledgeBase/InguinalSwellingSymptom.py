from experta import *
from DetailFacts import DetailInguinalSwellingFact
from DetailFacts import DetailResultFact


class InguinalSwellingSymptom(KnowledgeEngine):
    # 1 VL
	@Rule(
            DetailInguinalSwellingFact(
                swelling_presence="y",
                inguinal_area="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 2

	@Rule(
            DetailInguinalSwellingFact(
                swelling_presence="y",
                inguinal_area="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 3

	@Rule(
            DetailInguinalSwellingFact(
                swelling_presence="n",
                inguinal_area="n"
            )
        )
	def very_likely_4(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
