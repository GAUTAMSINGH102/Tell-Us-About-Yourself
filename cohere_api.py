import cohere
import textwrap
import config

co = cohere.Client(config.API_KEY)

    # --
    # Person name: Gautam
    # Place of education: Nirma University
    # Education degree: Bachelor's of Technology
    # Place of work: AbsolutelyAI
    # Position:  Machine Learning Engineer
    # Responsibilities: Kotlin, Android, Machine Learning, Python(Programming Language), Data Structure and Algorithm, Java, C(Programming Language), JavaScript, Node.js.
    # Achievements: I have win a first prize in hackathon and also build the best healthcare project in Hackathon.
    # Personal biography paragraph: I'm Gautam a Computer Science Engineer from Nirma University, Ahmedabad. I have over 3 years of experience in the field of Computer Science. I am an AI enthusiast and I love to explore the AI and ML. I love to solve problems and always have a curious and logical mindset. I am a self-taught engineer and I have a zeal to learn new things. I have done my internship in AbsolutelyAI. I have worked on various projects of Artificial Intelligence, Machine Learning, NLP, Computer Vision and Natural Language Processing. I have worked with different technologies like Kotlin, Android, Machine Learning, Python(Programming Language), Data Structure and Algorithm, Java, C(Programming Language), JavaScript, Node.js. I have done my projects in the field of Machine Learning and also done my research paper in the field of Machine Learning. I am an avid learner and I believe in sharing my knowledge. I am a good listener and love to help people.
    

data = textwrap.dedent(""" Person name: Maksim
    Place of education: Belarussian Technical University
    Education degree: Bachelor's degree in Economics
    Place of work: Fetti
    Position: Product director
    Responsibilities: Creating product requirements documents, guiding other product leaders, and leading all product initiatives.
    Achievements: Attracted 1,000 users to the new mobile app, expanding the geographical area of interaction.
    Personal biography paragraph: I'm Maksim a Belarussian-born entrepreneur and technology executive who has co-founded and led several successful startups. I have a Bachelor's degree in Economics from Belarusian Technical University and extensive experience in building teams, organizing processes, and project management, including cross-team collaboration. I am passionate about using technology to solve problems and improve people's lives. My latest venture is Fetti, a mobile app for tourists and nomads. I consider myself a gifted leader and problem-solver who has a proven track record of success.
    
    --
    Person name: Jiya
    Place of education: Indian Institute of Information Technology Bhopal
    Education degree: Bachelor of Technology - BTech
    Place of work: Google Developer Student Clubs,
    Position:  Assistant Web Developer
    Responsibilities: Python (Programming Language),React.js,Front-End Development,GitHub,Material-UI,Bootstrap,SASS,JavaScript,C++,Content Development,Cascading Style Sheets (CSS),HTML,C (Programming Language)
    Achievements: null
    Personal biography paragraph:""")


def cohere_generate(data):
    response = co.generate(prompt=data,
                           model='large',
                           max_tokens=150,
                           temperature=0.7,
                           k=0,
                           p=0.7,
                           frequency_penalty=0.1,
                           presence_penalty=0.0,
                           stop_sequences=None,
                        #    stop_sequences=["--"],
                        #    return_likelihoods='NONE',
                        #    truncate=None,
                        #    logit_bias={}
                           )

    # for gen in response.generations:
    #     print('Prediction:\n\ttext = {}\n'.format(gen.text))
        
    referral = response.generations[0].text
    referral = referral.replace("\n\n--", "").replace("\n--", "").strip()
    return referral

# res = cohere_generate(data)
# print(res)
