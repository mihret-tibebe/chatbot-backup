from inference_engine import run_expert_system


def get_user_input():
    unusual_discharge = input(
        "Is there unusual vaginal discharge? (yes/no): ").lower()
    vaginal_itching = input("Is there vaginal itching? (yes/no): ").lower()
    pain_urination = input(
        "Is there pain during urination? (yes/no): ").lower()
    pain_sex = input("Is there pain during sex? (yes/no): ").lower()

    return unusual_discharge, vaginal_itching, pain_urination, pain_sex


# Get user input
# unusual_discharge, vaginal_itching, pain_urination, pain_sex = get_user_input()

# Call the expert system
# results = run_expert_system(unusual_discharge, vaginal_itching, pain_urination, pain_sex)

results = run_expert_system(
# vaginal dicharge
    unusual_discharge="y",
    vaginal_itching="y",
    pain_urination="y",
    pain_during_sex="y",

# urethral discharge
    urethral_discharge="y",
    pain_during_urination="y",
    frequent_urination="y",

# genital ulcer
	genital_sore="y",
	# ////// for female too?
    inguinal_swelling="y",
    
# lower abdomenal pain
	pain_below_umbilicus="n",
    # fever="n",
	vaginal_discharge="n",  # umbigues
	missed_menstrual_period="n",
	# pain_during_sex="y",
	vaginal_bleeding="n",

# scrotal sweling
	scrotal_pain="y",
    sudden_onset_of_pain="y",
	# pain_during_urination="y",
	swelling="y",

# inguinal bubo
	painful_inguinal_lymph_node_or_swelling_over_the_groin="n",
	pus_discharge_from_swelling="y",
	fever="n",

# genital warts
	skin_colored_raised_bumps_with_rough_surface_single_or_multiple_on_genital_area="n",

# scabies
	skin_lesions_on_between_fingerswrist_genital_area_buttock="n",
	itching_worsening_at_night="n",
	similar_complaint_in_the_family_or_vicinity="n",

# pediculosis pubis
	pubic_area_itching="n",
	itching_over_the_thighs_axilla_eyelid="n",
	lice_or_nits_on_pubic_hair="y",

# viral hepatites
	yellowing_of_the_eyes="n",
	yellowing_of_the_skin="n",
	abdominal_pain="n",
	dark_urine="n"
)

for key, result in results.items():
	if result != "Unknown":
		if hasattr(result, 'other'):
			print(f'{key}: Result: {result.result}' " and ", result.other)
		else:
			print(f'{key}: Result: {result.result}')
	else:
		print(f'{key}: Result: {result}')
