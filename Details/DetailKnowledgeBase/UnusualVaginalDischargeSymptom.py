from experta import *
from DetailFacts import DetailUnusualVaginalDischargeFact
from DetailFacts import DetailResultFact


class UnusualVaginalDischargeSymptom(KnowledgeEngine):
    # 1 VL
	@Rule(
            DetailUnusualVaginalDischargeFact(
                color_change="y",
                bad_smell="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 2

	@Rule(
            DetailUnusualVaginalDischargeFact(
                color_change="y",
                bad_smell="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 3

	@Rule(
            DetailUnusualVaginalDischargeFact(
                color_change="n",
                bad_smell="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 4

	@Rule(
            DetailUnusualVaginalDischargeFact(
                color_change="n",
                bad_smell="n"
            )
        )
	def very_likely_4(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
