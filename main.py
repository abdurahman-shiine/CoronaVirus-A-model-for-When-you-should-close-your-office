import pandas as pd
import streamlit as st


def results(risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week):
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


def main():
	language = st.sidebar.radio('Language', ('English', 'Somali'))

	if language == 'English':
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

				results(risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week)

			except ZeroDivisionError:
				st.error('Number of people can\'t be zero')


		# Cases method
		if method == 'Cases method (not as reliable, making wild guesses on actual current cases in your area)':
			total_cases = st.number_input('Total cases in your area as of today')
			testing_type = st.selectbox('Is testing exhaustive, or only if connected to a known case?', ['', 'Only if connected to a case', 'Exhaustive'])
			community_spread = st.selectbox('Is community spread happening?', ['', 'Yes', 'No'])

			if testing_type == 'Only if connected to a case' and community_spread == 'Yes':
				days = list(range(1, 32))
				num_cases_reported = [12, 26, 43, 64, 103, 148, 215, 310, 383, 475, 624, 807, 1019, 1256, 1373, 1508, 2019, 2480, 2998, 3625, 4384, 5300, 6409, 7749, 9369, 11329, 13698, 16562, 20025, 24213, 29277, 35399]
				cases_data = dict(zip(days, num_cases_reported))

				df = pd.read_csv('spread_share.csv', header=None).iloc[0].tolist()

				foreign_spread_share_data = []
				for i, value in enumerate(df):
					foreign_spread_share_data.append(float(value.strip('%')) / 100)

				if total_cases <= 180:
					foreign_spread_share = foreign_spread_share_data[int(total_cases) - 1]
				else:
					foreign_spread_share = 1 / 100

				num_true_cases = total_cases / foreign_spread_share

				starting_day_index = list(cases_data.keys())[list(cases_data.values()).index(min(filter(lambda x: x > num_true_cases, num_cases_reported)))]

				likely_true_cases_tmrw = cases_data[starting_day_index]
				likely_true_cases_week = cases_data[starting_day_index + 6]
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

					results(risk_probability, method, no_infection_likelihood_today, no_infection_likelihood_tmrw, no_infection_likelihood_next_week)

				except ZeroDivisionError:
					st.error('Number of people can\'t be zero')

			elif testing_type == '' or community_spread == '':
				pass

			else:
				if testing_type == 'Exhaustive':
					st.info('Testing type: only "Connected to a Case" is built right now')
				if community_spread == 'No':
					st.info('Community spread: only "Yes" is built right now')

	else:
		pass


if __name__ == "__main__":
	main()