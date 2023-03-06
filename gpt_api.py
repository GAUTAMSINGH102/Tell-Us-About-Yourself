# import openai

# openai.api_key =""

# def gpt_generate(data):
#     response = openai.Completion.create(
#            model="text-davinci-002",
#             max_tokens = 250,
#             top_p = 1.00,
#             frequency_penalty = 0,
#             presence_penalty = 0,
#             prompt=data,
#             temperature=0.7,
#         )
#     return response.choices[0].text

# data = {'first_name': 'Gautam', 'lastName': 'Singh', 'position': 'Machine Learning Engineer', 'study': {'timePeriod': {'endDate': {'year': 2025}, 'startDate': {'year': 2020}}, 'degreeName': 'Integrated B.Tech CSE MBA ', 'schoolName': 'NIRMA UNIVERSITY', 'fieldOfStudy': 'Computer Science and Engineering'}, 'degree': [{'authority': 'SuperDataScience', 'name': 'Complete Python A-Z', 'timePeriod': {'startDate': {'month': 4, 'year': 2022}}}, {'authority': 'Coursera', 'name': 'Getting Started with AWS Machine Learning', 'timePeriod': {'startDate': {'month': 4, 'year': 2022}}}, {'authority': 'Coursera', 'name': ' Java for Android', 'timePeriod': {'startDate': {'month': 8, 'year': 2021}}}, {'authority': 'LinkedIn', 'name': 'Deep Learning: Face Recognition', 'timePeriod': {'startDate': {'month': 3, 'year': 2022}}}, {'authority': 'Udemy', 'name': 'Learn Machine Learning & AI', 'timePeriod': {'startDate': {'month': 4, 'year': 2022}}}, {'authority': 'Cloud Academy, Inc.', 'name': 'Machine Learning on Google Cloud Platform'}], 'company': {'locationName': 'Remote', 'companyName': 'AbsolutelyAI', 'timePeriod': {'endDate': {'month': 8, 'year': 2022}, 'startDate': {'month': 6, 'year': 2022}}}, 'responsibilities': ['Kotlin', 'Android', 'Machine Learning', 'Python (Programming Language)', 'Data Structure and Algorithm', 'Java', 'C (Programming Language)', 'JavaScript', 'Node.js'], 'achievements': None}
# returning = gpt_generate(data)
# print(returning)
