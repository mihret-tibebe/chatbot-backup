from experta import *
from DetailFacts import DetailScrotalPainFact
from DetailFacts import DetailResultFact


class ScrotalPainSymptom(KnowledgeEngine):
    # 1 L
	@Rule(
            DetailScrotalPainFact(
                scrotal_area="y",
                less_than_6_weeks="y",
				onset_s_sudden_g_gradual="s"
            )
        )
	def very_likely_1(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 2

	@Rule(
            DetailScrotalPainFact(
                scrotal_area="y",
                less_than_6_weeks="y",
				onset_s_sudden_g_gradual="g"
            )
        )
	def very_likely_2(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 3

	@Rule(
            DetailScrotalPainFact(
                scrotal_area="y",
                less_than_6_weeks="n",
				onset_s_sudden_g_gradual="s"
            )
        )
	def very_likely_3(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 4

	@Rule(
            DetailScrotalPainFact(
                scrotal_area="y",
                less_than_6_weeks="n",
				onset_s_sudden_g_gradual="g"
            )
        )
	def very_likely_4(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)


	#5

	@Rule(
            DetailScrotalPainFact(
                scrotal_area="n",
                less_than_6_weeks="y",
				onset_s_sudden_g_gradual="s"
            )
        )
	def very_likely_1(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 6

	@Rule(
            DetailScrotalPainFact(
                scrotal_area="n",
                less_than_6_weeks="y",
				onset_s_sudden_g_gradual="g"
            )
        )
	def very_likely_2(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 7

	@Rule(
            DetailScrotalPainFact(
                scrotal_area="n",
                less_than_6_weeks="n",
				onset_s_sudden_g_gradual="s"
            )
        )
	def very_likely_3(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 8

	@Rule(
            DetailScrotalPainFact(
                scrotal_area="n",
                less_than_6_weeks="n",
				onset_s_sudden_g_gradual="g"
            )
        )
	def very_likely_4(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
