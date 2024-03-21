from DetailKnowledgeBase.GenitalSoreSymptom import *
from DetailKnowledgeBase.InguinalSwellingSymptom import *
from DetailKnowledgeBase.ScrotalPainSymptom import *
from DetailKnowledgeBase.UnusualVaginalDischargeSymptom import *
from DetailKnowledgeBase.UrethralDischargeSymptom import *
from DetailKnowledgeBase.WartsGenitalAreaRaisedMassWithRoughSurfaceSymptom import *

def run_expert_system(**kwargs):
	# genital sore symptoms
	sore_presence = kwargs.get('sore_presence', "")
	gential_area = kwargs.get('gential_area', "")

# inguinal swelling symptoms
	swelling_presence = kwargs.get('swelling_presence', "")
	inguinal_area = kwargs.get('inguinal_area', "")

# scrotal pain
	scrotal_area = kwargs.get('scrotal_area', "")
	less_than_6_weeks = kwargs.get('less_than_6_weeks', "")
	onset_s_sudden_g_gradual = kwargs.get('onset_s_sudden_g_gradual', "")

# unusual vaginal discharge symptoms
	color_change = kwargs.get('color_change', "")
	bad_smell = kwargs.get('bad_smell', "")

# urethral discharge symptom
	color_change = kwargs.get('color_change', "")
	bad_smell = kwargs.get('bad_smell', "")

# Warts in genital area- raised mass with rough surface symptom
	type_itchy = kwargs.get('type_itchy', "")
	genital_area_perianal_area_over_oral_mucosa_in_the_mouth = kwargs.get('genital_area_perianal_area_over_oral_mucosa_in_the_mouth', "")


	gs_engine = GenitalSoreSymptom()
	gs_engine.reset()
	is_engine = InguinalSwellingSymptom()
	is_engine.reset()
	sp_engine = ScrotalPainSymptom()
	sp_engine.reset
	uvd_engine = UnusualVaginalDischargeSymptom()
	uvd_engine.reset()
	ud_engine = UrethralDischargeSymptom()
	ud_engine.reset()
	gew_engine = WartsGenitalAreaRaisedMassWithRoughSurfaceSymptom()
	gew_engine.reset()


	# print("***", **kwargs)

	gs_engine.declare(DetailGenitalSoreFact(
            sore_presence=sore_presence,
            gential_area=gential_area
        ))

	is_engine.declare(DetailInguinalSwellingFact(
		swelling_presence=swelling_presence,
        inguinal_area=inguinal_area
	))

	sp_engine.declare(DetailScrotalPainFact(
            scrotal_area=scrotal_area,
			less_than_6_weeks=less_than_6_weeks,
			onset_s_sudden_g_gradual=onset_s_sudden_g_gradual
        ))

	uvd_engine.declare(DetailUnusualVaginalDischargeFact(
		color_change=color_change,
		bad_smell=bad_smell
	))

	ud_engine.declare(DetailUrethralDischargeFact(
		color_change=color_change,
		bad_smell=bad_smell
	))

	gew_engine.declare(DetailWartsGenitalAreaRaisedMassWithRoughSurfaceFact(
		type_itchy=type_itchy,
        genital_area_perianal_area_over_oral_mucosa_in_the_mouth=genital_area_perianal_area_over_oral_mucosa_in_the_mouth
	))


	gs_engine.run()
	is_engine.run()
	sp_engine.run()
	uvd_engine.run()
	ud_engine.run()
	gew_engine.run()

	results = {}

# 1 gs
	for fact in gs_engine.facts.values():
		# print(fact)
		if isinstance(fact, DetailResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[gs_engine.__class__.__name__] = result_fact
	else:
		results[gs_engine.__class__.__name__] = "Unknown"

# 2 UD
	for fact in sp_engine.facts.values():
		if isinstance(fact, DetailResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[sp_engine.__class__.__name__] = result_fact
	else:
		results[sp_engine.__class__.__name__] = "Unknown"

# 3 GU
	for fact in ud_engine.facts.values():
		if isinstance(fact, DetailResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[ud_engine.__class__.__name__] = result_fact
	else:
		results[ud_engine.__class__.__name__] = "Unknown"

# 4 is
	for fact in is_engine.facts.values():
		if isinstance(fact, DetailResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[is_engine.__class__.__name__] = result_fact
	else:
		results[is_engine.__class__.__name__] = "Unknown"

# 5
	for fact in uvd_engine.facts.values():
		if isinstance(fact, DetailResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[uvd_engine.__class__.__name__] = result_fact
	else:
		results[uvd_engine.__class__.__name__] = "Unknown"

# 6
	for fact in gew_engine.facts.values():
		if isinstance(fact, DetailResultFact):
			result_fact = fact
		else:
			result_fact = None
	if result_fact is not None:
		results[gew_engine.__class__.__name__] = result_fact
	else:
		results[gew_engine.__class__.__name__] = "Unknown"


	# return "Unknown"
	return results
