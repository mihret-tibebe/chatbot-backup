from experta import *
from DetailFacts import DetailUrethralDischargeFact
from DetailFacts import DetailResultFact


class UrethralDischargeSymptom(KnowledgeEngine):
    # 1 VL
	@Rule(
            DetailUrethralDischargeFact(
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
            DetailUrethralDischargeFact(
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
            DetailUrethralDischargeFact(
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
            DetailUrethralDischargeFact(
                color_change="n",
                bad_smell="n"
            )
        )
	def very_likely_4(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
