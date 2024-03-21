from details_infrence_engine import run_expert_system


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
    # genital sore symptoms
    sore_presence="y",
    gential_area="y",

    # inguinal swelling symptoms
    swelling_presence="y",
    inguinal_area="y",

    # scrotal pain
   	scrotal_area="y",
    less_than_6_weeks="y",
   	onset_s_sudden_g_gradual="n",

    # urethral discharge symptom
   	# unusual vaginal discharge symptoms
   	color_change="n",
   	bad_smell="n",

    # Warts in genital area- raised mass with rough surface symptom
   	type_itchy="y",
    genital_area_perianal_area_over_oral_mucosa_in_the_mouth="y"
)

for key, result in results.items():
	if result != "Unknown":
		if hasattr(result, 'other'):
			print(f'{key}: Result: {result.result}' " and ", result.other)
		else:
			print(f'{key}: Result: {result.result}')
	else:
		print(f'{key}: Result: {result}')
