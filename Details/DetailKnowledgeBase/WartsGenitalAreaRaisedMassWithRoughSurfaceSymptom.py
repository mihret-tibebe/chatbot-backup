from experta import *
from DetailFacts import DetailWartsGenitalAreaRaisedMassWithRoughSurfaceFact
from DetailFacts import DetailResultFact


class WartsGenitalAreaRaisedMassWithRoughSurfaceSymptom(KnowledgeEngine):
    # 1 VL
	@Rule(
            DetailWartsGenitalAreaRaisedMassWithRoughSurfaceFact(
                type_itchy="y",
                genital_area_perianal_area_over_oral_mucosa_in_the_mouth="y"
            )
        )
	def very_likely_1(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "L"
		self.declare(new_result_fact)
	# 2

	@Rule(
            DetailWartsGenitalAreaRaisedMassWithRoughSurfaceFact(
                type_itchy="y",
                genital_area_perianal_area_over_oral_mucosa_in_the_mouth="n"
            )
        )
	def very_likely_2(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
	# 3

	@Rule(
            DetailWartsGenitalAreaRaisedMassWithRoughSurfaceFact(
                type_itchy="n",
                genital_area_perianal_area_over_oral_mucosa_in_the_mouth="y"
            )
        )
	def very_likely_3(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "VL"
		self.declare(new_result_fact)
	# 4

	@Rule(
            DetailWartsGenitalAreaRaisedMassWithRoughSurfaceFact(
                type_itchy="n",
                genital_area_perianal_area_over_oral_mucosa_in_the_mouth="n"
            )
        )
	def very_likely_4(self):
		new_result_fact = DetailResultFact()
		new_result_fact.result = "UL"
		self.declare(new_result_fact)
