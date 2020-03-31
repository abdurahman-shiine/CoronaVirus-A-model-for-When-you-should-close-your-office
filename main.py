import pandas as pd
import streamlit as st


def results(language, risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week):
	if language == 'English':
		st.write('   ')
		st.title('Resutls')
		st.write('   ')

		business_type = st.selectbox('Business type', ['', 'Individual business', 'Group of businesses'])
		st.write('   ')

		if business_type == 'Group of businesses':
			num_group = st.number_input('Number of members in the group')
			st.subheader('Likelihood that at least one company is infected in the group')
			st.write('Likelihood that at least one company in the group is infected today', f'{round((1 - ((1 - round(1 - (no_infection_likelihood_today) / 100, 2)) ** num_group)) * 100, 1)}%')
			st.write('Likelihood that at least one company in the group will be infected tomorrow', f'{round((1 - ((1 - round(1 - (no_infection_likelihood_tmrw) / 100, 2)) ** num_group)) * 100, 1)}%')
			st.write('Likelihood that at least one company in the group will be infected in a week', f'{round((1 - ((1 - round(1 - (no_infection_likelihood_next_week) / 100, 2)) ** num_group)) * 100, 1)}%')

		st.subheader('Likelihood that an average company is infected')
		st.write('Probability that at least one of your employees is infected today: ', f'{round(1 - (no_infection_likelihood_today) / 100, 2) * 100}%')
		st.write('Probability that at least one of your employees is infected tomorrow: ', f'{round(1 - (no_infection_likelihood_tmrw) / 100, 2) * 100}%')
		st.write('Probability that at least one of your employees is infected in a week', f'{round(round(1 - (no_infection_likelihood_next_week) / 100, 2) * 100, 1)}%')

		if (round(1 - (no_infection_likelihood_today) / 100, 2) * 100) > risk_probability:
			st.error('Close immediately')
		elif (round(1 - (no_infection_likelihood_tmrw) / 100, 2) * 100) > risk_probability:
			st.warning('Close before tomorrow')
		elif (round(1 - (no_infection_likelihood_next_week) / 100, 2) * 100) > risk_probability:
			st.info('Close within a week')
		else:
			st.success('No need to close this coming week')

	elif language == 'Somali':
		st.write('   ')
		st.title('Natiijada')
		st.write('   ')

		business_type = st.selectbox('Nooca meherada', ['', 'Meherad gooni isku-taaga', 'Meherado isku biirey'])
		st.write('   ')

		if business_type == 'Meherado isku biirey':
			num_group = st.number_input('Tirada meheradaha isku biirey')
			st.subheader('Ixtimaalka in mid ka mid ah meheradaha ugu yaraan uu xanuunku gaadhey')
			st.write('Ixtimaalka in mid ka mid ah meheradaha ugu yaraan uu xanuunku gaadhey maanta', f'{round((1 - ((1 - round(1 - (no_infection_likelihood_today) / 100, 2)) ** num_group)) * 100, 1)}%')
			st.write('Ixtimaalka in mid ka mid ah meheradaha ugu yaraan uu xanuunku gaadhi doono barri', f'{round((1 - ((1 - round(1 - (no_infection_likelihood_tmrw) / 100, 2)) ** num_group)) * 100, 1)}%')
			st.write('Ixtimaalka in mid ka mid ah meheradaha ugu yaraan uu xanuunku gaadhi 7aad gudihii', f'{round((1 - ((1 - round(1 - (no_infection_likelihood_next_week) / 100, 2)) ** num_group)) * 100, 1)}%')

		st.subheader('Ixtimaalka in mid ka mid ah shaqalaha uu xanuunku ku dhacay')
		st.write('Ixtimaalka in mid ka mid ah shaqalaha uu xanuunku ku dhacay maanta: ', f'{round(1 - (no_infection_likelihood_today) / 100, 2) * 100}%')
		st.write('Ixtimaalka in mid ka mid ah shaqalaha uu xanuunku ku dhici doono barri: ', f'{round(1 - (no_infection_likelihood_tmrw) / 100, 2) * 100}%')
		st.write('Ixtimaalka in mid ka mid ah shaqalaha uu xanuunku ku dhici doono 7aad gudihii', f'{round(round(1 - (no_infection_likelihood_next_week) / 100, 2) * 100, 1)}%')

		if (round(1 - (no_infection_likelihood_today) / 100, 2) * 100) > risk_probability:
			st.error('Sida ugu dhakhsiyaha badan uxidh meherada [imikadan]')
		elif (round(1 - (no_infection_likelihood_tmrw) / 100, 2) * 100) > risk_probability:
			st.warning('Barri kohor xidh meherada')
		elif (round(1 - (no_infection_likelihood_next_week) / 100, 2) * 100) > risk_probability:
			st.info('7aad gudihii ku xidh meherada')
		else:
			st.success('Uma baahnid inaad xidhid meherada 7aadkan soo socda')





def main():
	st.sidebar.subheader('Language/Luuqada')
	language = st.sidebar.radio('', ('English', 'Somali'))

	if language == 'English':
		st.title('COVID-19: A model for when you should close your office')
		for i in range(3):
			st.write(" ")

		st.markdown("> ### A model to help you and your company make a decision on whether you should open your office or send everybody home amid the COVID-19 crisis.")

		for i in range(2):
			st.write(" ")

		st.write("It was first developed by [Tomas Pueyo](https://medium.com/@tomaspueyo) as a complimentary tool to his viral article on Medium [Coronavirus: Why You Must Act Now](https://medium.com/@tomaspueyo/coronavirus-act-today-or-people-will-die-f4d3d9cd99ca), an impressive article that I strongly recommend you read. This is a python adaptation of the model, developed by [Abdurahman Shiine](https://github.com/abdurahman-shiine).")
		st.write("It's based on how many COVID-19 cases are probably in your area, and the likelihood that at least one of your employees catches it.\nIt has lots of assumptions, but all the data necessary is [here](https://docs.google.com/spreadsheets/u/1/d/17YyCmjb2Z2QwMiRRwAb7W0vQoEAiL9Co0ARsl03dSlw/copy?usp=sharing), so you can play with the assumptions to adapt them to your situation.\nNote that only the necessary portions of the data were migrated to the [model_data.csv](https://github.com/abdurahman-shiine/CoronaVirus-A-model-for-When-you-should-close-your-office) file used for this model, so you might need to get some data from the original source if you need to recompute some specific parameters.")
		st.write("The way to use this dashbourd is by filling in all the empty boxes, and select one of the options in each of the dropdown menus to apply the model to your case. The model is available in both English and Somali languages.")

		st.markdown("<div align='center'><br>"
                "<img src='https://img.shields.io/badge/MADE%20WITH-PYTHON%20-red?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/SERVED%20WITH-Heroku-blue?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/DASHBOARDING%20WITH-Streamlit-green?style=for-the-badge'"
                "alt='API stability' height='25'/></div>", unsafe_allow_html=True)

		for i in range(3):
			st.write(" ")

		st.header('🌀 The model')
		num_employees = st.number_input('The number of employees you have')
		risk_probability = st.number_input("Tolerable risk % (I'm ok with this probability that one or more of my employees has the coronavirus.)")
		method = st.selectbox('Calculation method', ['', 'Deaths method (more reliable, use if there have been deaths in your area)', 'Cases method (not as reliable, making wild guesses on actual current cases in your area)'])


		# Deaths method
		if method == 'Deaths method (more reliable, use if there have been deaths in your area)':
			total_deaths = st.number_input('Total deaths as of today (Number of deaths you are seeing in the geographic area of influence of your office. Eg Sonomish / King / Grant counties)')

			st.markdown('### The following results are based on:')
			st.markdown('#### - Fatality rate = 0.87%')
			st.markdown('#### - Number of days from infection to death = 17.3 days')
			st.markdown('#### - Doubling time = 6.2 days')
			st.markdown('#             ')

			fatality_rate = 0.87 / 100
			# How many cases were there some time ago that caused these deaths?
			num_cases_caused_death = total_deaths / fatality_rate
			# How many days did it take for the cases to become deaths? Based on 4 papers
			days_from_infection = 17.3
			# How many days does it take for cases to double?
			doubling_time = 6.2
			# How many times do cases double between the time of the cases that caused deaths and the deaths
			num_times_cases_doubled = days_from_infection / doubling_time
			# Estimation of true cases today in your area
			num_true_cases = num_cases_caused_death * 2 ** num_times_cases_doubled

			# The likelihood of true and new cases in your area tomorrow and in a week
			likely_true_cases_tmrw = num_true_cases * 2 ** (1 / doubling_time)
			likely_new_cases_tmrw = likely_true_cases_tmrw - num_true_cases
			likely_true_cases_week = num_true_cases * 2 ** (7 / doubling_time)
			likely_new_cases_week = likely_true_cases_week - num_true_cases

			st.write('Number of cases that caused the death: ', round(num_cases_caused_death))
			st.write('True cases today: ', round(num_true_cases))
			st.write('Likely true cases tomorrow: ', round(likely_true_cases_tmrw))
			st.write('Likely true cases in a week: ', round(likely_true_cases_week))
			st.write('Likely new cases tomorrow: ', round(likely_new_cases_tmrw))
			st.write('Likely new cases in a week: ', round(likely_true_cases_week))


			# ******* Estimation of the likelihood of a person getting infected *******
			st.subheader('Estimation of the likelihood of a person getting infected')
			num_people = st.number_input('Number of people in the area of deaths (must be >= 10,000)', value=10000, min_value=10000)

			try:
				if num_true_cases >= num_people:
					no_infection_likelihood_today = 0.0
					no_infection_likelihood_tmrw = 0.0
					no_infection_likelihood_next_week = 0.0

				else:
					# Current infection rate
					infection_rate_today = num_true_cases / num_people
					# Expected infection rate the next day
					infection_rate_tmrw = likely_true_cases_tmrw / num_people
					# Expected infection rate a week later
					infection_rate_next_week = likely_true_cases_week / num_people

					no_infection_likelihood_today = ((1 - infection_rate_today) ** num_employees) * 100
					no_infection_likelihood_tmrw = ((1 - infection_rate_tmrw) ** num_employees) * 100
					no_infection_likelihood_next_week = ((1 - infection_rate_next_week) ** num_employees) * 100

				st.write('likelihood that none of your employees already have the coronavirus', f'{round(no_infection_likelihood_today, 1)}%')
				st.write('likelihood that none of your employees will have the coronavirus by tomorrow', f'{round(no_infection_likelihood_tmrw, 1)}%')
				st.write('likelihood that none of your employees will have the coronavirus by next week', f'{round(no_infection_likelihood_next_week, 1)}%')

				results(language, risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week)

			except ZeroDivisionError:
				st.error('Number of people can\'t be zero')


		# Cases method
		if method == 'Cases method (not as reliable, making wild guesses on actual current cases in your area)':
			total_cases = st.number_input('Total cases in your area as of today')
			testing_type = st.selectbox('Is testing exhaustive, or only if connected to a known case?', ['', 'Only if connected to a case', 'Exhaustive'])
			community_spread = st.selectbox('Is community spread happening?', ['', 'Yes', 'No'])

			if testing_type == 'Only if connected to a case' and community_spread == 'Yes':
				df = pd.read_csv('model_data.csv', header=None, thousands=',').transpose()
				new_header = df.iloc[0]
				df = df[1:]
				df.columns = new_header
				df.reset_index(inplace=True)

				foreign_spread_share_data = df['Share China'].apply(lambda x: float(x.strip('%')) / 100)

				if total_cases <= 180:
					foreign_spread_share = foreign_spread_share_data[int(total_cases) - 1]
				else:
					foreign_spread_share = 1 / 100

				num_true_cases = total_cases / foreign_spread_share
				cases_data = df['Typical contagion as a blend of other countries (US UK DE FR ES IT IR SK JP CH) (you can insert your own #s here)'][:32]
				cases_data = cases_data.str.replace(',', '').astype(float)
				starting_day_index = min(filter(lambda x: x > num_true_cases, cases_data.tolist()))

				likely_true_cases_tmrw = cases_data[cases_data[ cases_data == starting_day_index].index[0]]
				likely_true_cases_week = cases_data[cases_data[ cases_data == starting_day_index].index[0] + 6]
				likely_new_cases_tmrw = likely_true_cases_tmrw - num_true_cases
				likely_new_cases_week = likely_true_cases_week - num_true_cases

				st.write('True cases today: ', round(num_true_cases))
				st.write('Likely true cases tomorrow: ', round(likely_true_cases_tmrw))
				st.write('Likely true cases in a week: ', round(likely_true_cases_week))
				st.write('Likely new cases tomorrow: ', round(likely_new_cases_tmrw))
				st.write('Likely new cases in a week: ', round(likely_new_cases_week))


				# ******* Estimation of the likelihood of a person getting infected *******
				st.subheader('Estimation of the likelihood of a person getting infected')
				num_people = st.number_input('Number of people in the infected area (must be >= 10,000)', value=10000, min_value=10000)

				try:
					if num_true_cases >= num_people:
						no_infection_likelihood_today = 0.0
						no_infection_likelihood_tmrw = 0.0
						no_infection_likelihood_next_week = 0.0

					else:
						# Current infection rate
						infection_rate_today = num_true_cases / num_people
						# Expected infection rate the next day
						infection_rate_tmrw = likely_true_cases_tmrw / num_people
						# Expected infection rate a week later
						infection_rate_next_week = likely_true_cases_week / num_people

						no_infection_likelihood_today = ((1 - infection_rate_today) ** num_employees) * 100
						no_infection_likelihood_tmrw = ((1 - infection_rate_tmrw) ** num_employees) * 100
						no_infection_likelihood_next_week = ((1 - infection_rate_next_week) ** num_employees) * 100

					st.write('likelihood that none of your employees already have the coronavirus', f'{round(no_infection_likelihood_today, 3)}%')
					st.write('likelihood that none of your employees will have the coronavirus by tomorrow', f'{round(no_infection_likelihood_tmrw, 3)}%')
					st.write('likelihood that none of your employees will have the coronavirus by next week', f'{round(no_infection_likelihood_next_week, 3)}%')

					results(language, risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week)

				except ZeroDivisionError:
					st.error('Number of people can\'t be zero')

			elif testing_type == '' or community_spread == '':
				pass

			else:
				if testing_type == 'Exhaustive':
					st.info('Testing type: only "Connected to a Case" is built right now')
				if community_spread == 'No':
					st.info('Community spread: only "Yes" is built right now')


	elif language == 'Somali':
		st.title('COVID-19: Hab-xisaabineed aad ku ogaanayso goorta ay tahey in aad meheradaada xidho')
		for i in range(3):
			st.write(" ")

		st.markdown("> ### Model kaa caawinaya adi iyo sharikadaadaba ka go'aan qaadashada goorma ayaa ay tahey in aad xidho xafiisyada oo shaqaalaha aad fasaxdo")

		for i in range(2):
			st.write(" ")

		st.write("Waxa markii ugu horraysay curiyey model-kan [Tomas Pueyo](https://medium.com/@tomaspueyo) oo ugu talo-galay in ay isticmaalaan akhristayaashaa maqaalkiisii caanka noqdey ee uu ku shaaciyey wargayska Medium [Coronavirus: Why You Must Act Now](https://medium.com/@tomaspueyo/coronavirus-act-today-or-people-will-die-f4d3d9cd99ca), kaasi oo aad aan ugula talinayo cid kasta in ay akhirdo, (tarjumaadiisa somaliga ahna aad ka helaysiin [halkan](https://www.facebook.com/notes/abdurahman-shiine/-covid-19-maxay-waajib-kuugu-tahey-inaad-maanta-fal-qaaddo/2941779562584988/)). Kani waa model kii oo Python lagu qorey, waxana qorey [Abdurahman Shiine](https://github.com/abdurahman-shiine).")
		st.write("Waxa uu model-ku ku salaysanyahey imisa xaaladood oo COVID_19 ah ayaa ay ubadantahey in ay ka jiraan aagaaga, iyo ixtimaalka in mid shaqaalahaaga ka mid ah uu ku qaadi karo xanuunkaas. Xisaabuhu waxa ay ku salaysan yihiin xog laga helayo [halkan](https://docs.google.com/spreadsheets/u/1/d/17YyCmjb2Z2QwMiRRwAb7W0vQoEAiL9Co0ARsl03dSlw/copy?usp=sharing), inteeda badanna ay tahey qiyaasid/dhadhawayn ee ayna ahayn wax la hubo 100%, sidaa darteed haddii aad ubaahato xogta aasaasiga ah wax waa aad ka beddeli kartaa si model-ka aad ugu salaysid duruufahaaga. FG. Xogta inteeda lagama maarmaanka ah kaliya ayaa lagu xareeyey file-ka [model_data.csv](https://github.com/abdurahman-shiine/CoronaVirus-A-model-for-When-you-should-close-your-office) ee uu xogta ka akhrinayo program-kani, sidaa darteed laga yaabaa in xogta qaybo ka mid ah aad kaliya ka hesho lifaaqa hore.")
		st.write("Qaabka loo isticmaalayo program-kan waa in aad buuxiso bogosyada bannaan meelaha ka xulasho ubaahanna aad options-ka ku hor yaalla mid ka xulato, si aad model-ka ugu dabbaqdo xaaladaada. Labada luuqadood ee Somali iyo Ingiriisiba waa aad ku isticmaali kartaa program-kan.")

		st.markdown("<div align='center'><br>"
                "<img src='https://img.shields.io/badge/MADE%20WITH-PYTHON%20-red?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/SERVED%20WITH-Heroku-blue?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/DASHBOARDING%20WITH-Streamlit-green?style=for-the-badge'"
                "alt='API stability' height='25'/></div>", unsafe_allow_html=True)

		for i in range(3):
			st.write(" ")

		st.header('🌀 Model-ka')
		num_employees = st.number_input('Tirada shaqaalahaaga')
		risk_probability = st.number_input(" % khatarta aad xamili karto (Waxa aan xamili karaa ixtimaal ah in mid ama wax ka badan oo shaqaalahayga ka mid ahi ay boqolkiiba intaa xanuunku hayyo.)")
		method = st.selectbox('Habka xisaabinta', ['', 'Habka tirada dhimashooyinka (waa la isku hallayn karaa, isticmaal haddii aagaaga wax dhimasho ahi ka dhacdey)', 'Habka tirada xaaladaha (Sida habka kale la iskuguma hallayn karo)'])


		# Deaths method
		if method == 'Habka tirada dhimashooyinka (waa la isku hallayn karaa, isticmaal haddii aagaaga wax dhimasho ahi ka dhacdey)':
			total_deaths = st.number_input('Wadarta dhimashooyinka illaa maanta (Tirada xaaladaha ku dhintey COVID-19 aaga xafiisyada sharikadaadu ku yaallaan)')

			st.markdown('### Natiijooyinka soo socdaa waxa ay ku salaysanyihiin:')
			st.markdown('#### - Heer dhimasho = 0.87%')
			st.markdown('#### - Muddada udhaxaysa qaadida xanuunka iyo ku dhimashadiisa = 17.3 maaalmood')
			st.markdown('#### - Muddada ay ku libinlaabmayaan xaaladuhu = 6.2 maalmood')
			st.markdown('#             ')

			fatality_rate = 0.87 / 100
			# How many cases were there some time ago that caused these deaths?
			num_cases_caused_death = total_deaths / fatality_rate
			# How many days did it take for the cases to become deaths? Based on 4 papers
			days_from_infection = 17.3
			# How many days does it take for cases to double?
			doubling_time = 6.2
			# How many times do cases double between the time of the cases that caused deaths and the deaths
			num_times_cases_doubled = days_from_infection / doubling_time
			# Estimation of true cases today in your area
			num_true_cases = num_cases_caused_death * 2 ** num_times_cases_doubled

			# The likelihood of true and new cases in your area tomorrow and in a week
			likely_true_cases_tmrw = num_true_cases * 2 ** (1 / doubling_time)
			likely_new_cases_tmrw = likely_true_cases_tmrw - num_true_cases
			likely_true_cases_week = num_true_cases * 2 ** (7 / doubling_time)
			likely_new_cases_week = likely_true_cases_week - num_true_cases

			st.write('Tirada xaaladaha keenay dhimashada: ', round(num_cases_caused_death))
			st.write('Tirada xaaladaha dhabta ah maanta: ', round(num_true_cases))
			st.write('Tirada la filanayo in ay xaaladuhu barri gaadhaan: ', round(likely_true_cases_tmrw))
			st.write('Tirada la filanayo in ay xaaladuhu 7aad ka bacdi gaadhaan: ', round(likely_true_cases_week))
			st.write('Tirada xaaladaha la filanayo in ay barri soo kordhaan: ', round(likely_new_cases_tmrw))
			st.write('Tirada xaaladaha la filanayo in ay 7aad ka bacdi soo kordhaan: ', round(likely_true_cases_week))


			# ******* Estimation of the likelihood of a person getting infected *******
			st.subheader('Qiyaasida ixtimaalka uu hal qof ku qaadi karo xanuunka')
			num_people = st.number_input('Tirada dadka ku sugan aaga dhimashadu ka dhacdey (waa in ay >= 10,000)', value=10000, min_value=10000)

			try:
				if num_true_cases >= num_people:
					no_infection_likelihood_today = 0.0
					no_infection_likelihood_tmrw = 0.0
					no_infection_likelihood_next_week = 0.0

				else:
					# Current infection rate
					infection_rate_today = num_true_cases / num_people
					# Expected infection rate the next day
					infection_rate_tmrw = likely_true_cases_tmrw / num_people
					# Expected infection rate a week later
					infection_rate_next_week = likely_true_cases_week / num_people

					no_infection_likelihood_today = ((1 - infection_rate_today) ** num_employees) * 100
					no_infection_likelihood_tmrw = ((1 - infection_rate_tmrw) ** num_employees) * 100
					no_infection_likelihood_next_week = ((1 - infection_rate_next_week) ** num_employees) * 100

				st.write('Ixtimaalka in shaqaalahaaga midna uuna qabin COVID-19 hadda', f'{round(no_infection_likelihood_today, 1)}%')
				st.write('Ixtimaalka in shaqaalahaaga midna uuna qabin doonin COVID-19 barri', f'{round(no_infection_likelihood_tmrw, 1)}%')
				st.write('Ixtimaalka in shaqaalahaaga midna uuna qabin doonin COVID-19 7aad ka bacdi', f'{round(no_infection_likelihood_next_week, 1)}%')

				results(language, risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week)

			except ZeroDivisionError:
				st.error('Tirada dadka dagan aagu 0 ma noqon karto')


		# Cases method
		if method == 'Habka tirada xaaladaha (Sida habka kale la iskuguma hallayn karo)':
			total_cases = st.number_input('Wadarta tirada xaaladaha ka jira aagaaga maanta ahaan')
			testing_type = st.selectbox('Ma lawada baadhey dadka aaga oo dhan mise kaliya kuwa la kulmey qof buka?', ['', 'Kaliya kuwa la kulmey qof buka', 'Waa la wada baadhey'])
			community_spread = st.selectbox('Bulshadu miyey isku faafinaysaa xanuunka?', ['', 'Haa', 'Maya'])

			if testing_type == 'Kaliya kuwa la kulmey qof buka' and community_spread == 'Haa':
				df = pd.read_csv('model_data.csv', header=None, thousands=',').transpose()
				new_header = df.iloc[0]
				df = df[1:]
				df.columns = new_header
				df.reset_index(inplace=True)

				foreign_spread_share_data = df['Share China'].apply(lambda x: float(x.strip('%')) / 100)

				if total_cases <= 180:
					foreign_spread_share = foreign_spread_share_data[int(total_cases) - 1]
				else:
					foreign_spread_share = 1 / 100

				num_true_cases = total_cases / foreign_spread_share
				cases_data = df['Typical contagion as a blend of other countries (US UK DE FR ES IT IR SK JP CH) (you can insert your own #s here)'][:32]
				cases_data = cases_data.str.replace(',', '').astype(float)
				starting_day_index = min(filter(lambda x: x > num_true_cases, cases_data.tolist()))

				likely_true_cases_tmrw = cases_data[cases_data[ cases_data == starting_day_index].index[0]]
				likely_true_cases_week = cases_data[cases_data[ cases_data == starting_day_index].index[0] + 6]
				likely_new_cases_tmrw = likely_true_cases_tmrw - num_true_cases
				likely_new_cases_week = likely_true_cases_week - num_true_cases

				st.write('Tirada xaaladaha dhabta ah maanta: ', round(num_true_cases))
				st.write('Tirada la filanayo in ay xaaladuhu barri gaadhaan: ', round(likely_true_cases_tmrw))
				st.write('Tirada la filanayo in ay xaaladuhu 7aad ka bacdi gaadhaan: ', round(likely_true_cases_week))
				st.write('Tirada xaaladaha la filanayo in ay barri soo kordhaan: ', round(likely_new_cases_tmrw))
				st.write('Tirada xaaladaha la filanayo in ay 7aad ka bacdi soo kordhaan: ', round(likely_new_cases_week))


				# ******* Estimation of the likelihood of a person getting infected *******
				st.subheader('Qiyaasida ixtimaalka uu hal qof ku qaadi karo xanuunka')
				num_people = st.number_input('Tirada dadka ku sugan aaga xanuunku ku faafey (waa in ay >= 10,000)', value=10000, min_value=10000)

				try:
					if num_true_cases >= num_people:
						no_infection_likelihood_today = 0.0
						no_infection_likelihood_tmrw = 0.0
						no_infection_likelihood_next_week = 0.0

					else:
						# Current infection rate
						infection_rate_today = num_true_cases / num_people
						# Expected infection rate the next day
						infection_rate_tmrw = likely_true_cases_tmrw / num_people
						# Expected infection rate a week later
						infection_rate_next_week = likely_true_cases_week / num_people

						no_infection_likelihood_today = ((1 - infection_rate_today) ** num_employees) * 100
						no_infection_likelihood_tmrw = ((1 - infection_rate_tmrw) ** num_employees) * 100
						no_infection_likelihood_next_week = ((1 - infection_rate_next_week) ** num_employees) * 100

					st.write('Ixtimaalka in shaqaalahaaga midna uuna qabin COVID-19 hadda', f'{round(no_infection_likelihood_today, 3)}%')
					st.write('Ixtimaalka in shaqaalahaaga midna uuna qabin doonin COVID-19 barri', f'{round(no_infection_likelihood_tmrw, 3)}%')
					st.write('Ixtimaalka in shaqaalahaaga midna uuna qabin doonin COVID-19 7aad ka bacdi', f'{round(no_infection_likelihood_next_week, 3)}%')

					results(language, risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week)

				except ZeroDivisionError:
					st.error('Tirada dadka dagan aagu 0 ma noqon karto')

			elif testing_type == '' or community_spread == '':
				pass

			else:
				if testing_type == 'Waa la wada baadhey':
					st.info('Nooca baadhitaanka: kaliya hab-xisaabineedka "Kaliya kuwa la kulmey qof buka" ayaa la sameeyey hadda')
				if community_spread == 'Maya':
					st.info('Isku-faafinta bulshada: kaliya "Haa" ayaa la sameeyey hadda')

	else:
		pass



if __name__ == "__main__":
	main()