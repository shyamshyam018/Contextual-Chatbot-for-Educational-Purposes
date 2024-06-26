from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import logout
from .models import UserProfile 
from .models import UserHistory
import pytz
from django.shortcuts import render
from app1.models import UserHistory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    user_name = request.user.username if request.user.is_authenticated else None
    return render(request, 'home.html', {'user_name': user_name})

def HomePage1(request):
    user_name = request.user.username if request.user.is_authenticated else None
    return render(request, 'home1.html', {'user_name': user_name})




def ContactPage(request):
    return render(request, 'contact.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')



from django.contrib.auth import logout

def Logout(request):
    logout(request)
    return redirect('login')


def ChatBot(request):
    return render (request,'chatbot.html')
    

def BitChat(request):
    return render (request,'bitchat.html')


def DashBoard(request):
    return render(request, 'dashboard.html')

def ContactPage(request):
    return render(request, 'contact.html')



def ChatBot1(request):
    return render (request,'chatbot1.html')
    

def BitChat1(request):
    return render (request,'bitchat1.html')


def DashBoard1(request):
    return render(request, 'dashboard1.html')

def ContactPage1(request):
    return render(request, 'contact1.html')

def bit(request):
    return render(request, 'bit.html')

def bit1(request):
    return render(request, 'bit1.html')

def VoiceBot(request):
    return render(request, 'voicechat.html')





from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer , ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch
# import collections
# from collections.abc import Hashable
 

bot = ChatBot('BitBot', read_only=False, logic_adapters=[
    {
        'import_path':'chatterbot.logic.BestMatch',
        'default_response':'Sorry, I don\'t know what that means',
        'maximum_similarity_threshold': 0.90
    }
])


list_to_train = [

"hai",
"Hello , Im BitBot how can i help you ?",

"what can you do",
"I can help you with your educational doubts ",

"How to become a Machine Learning Engineer",
"Learn Python Programming (2-3 months) > Study Mathematics and Statistics (3-4 months) > Learn Machine Learning Basics (3-4 months) > Dive into Advanced Machine Learning (6+ months) > Build Machine Learning Projects (6+ months)",

"How to become a Cloud Architect",
"Understand Cloud Computing Concepts (2-3 months) > Learn Cloud Platforms (AWS, Azure, GCP) (3-4 months) > Study Cloud Services and Solutions (3-4 months) > Gain Architecture Design Skills (6+ months) > Design and Implement Scalable Cloud Solutions (6+ months)",

"How to become a Full Stack Developer",
"Learn HTML, CSS, and JavaScript (3-4 months) > Understand Backend Development (Node.js, Python, etc.) (3-4 months) > Study Databases and API Integration (3-4 months) > Learn Frontend Frameworks (React, Angular, etc.) (3-4 months) > Build and Deploy Full Stack Applications (6+ months)",

"How to become a Game Developer",
"Learn Programming Fundamentals (2-3 months) > Study Game Development Basics (3-4 months) > Understand Game Engines (Unity, Unreal) (3-4 months) > Learn 2D and 3D Graphics (3-4 months) > Build and Publish Games (6+ months)",

"How to become a Network Engineer",
"Understand Networking Fundamentals (2-3 months) > Study Network Protocols and Topologies (3-4 months) > Learn Network Security and Firewall (3-4 months) > Gain Hands-on Experience with Network Configuration (6+ months) > Design and Implement Secure Networks (6+ months)",

"How to become a Blockchain Developer",
"Understand Blockchain Technology (2-3 months) > Learn Cryptography and Smart Contracts (3-4 months) > Study Blockchain Platforms (Ethereum, Binance Smart Chain) (3-4 months) > Build Decentralized Applications (DApps) (6+ months) > Explore DeFi and NFT Development (6+ months)",

"How to become an AI Engineer",
"Learn Python and Data Manipulation (2-3 months) > Study Machine Learning Algorithms (3-4 months) > Understand Natural Language Processing (NLP) and Computer Vision (3-4 months) > Dive into Deep Learning and Neural Networks (6+ months) > Build AI Applications and Models (6+ months)",

"How to become a Quality Assurance (QA) Engineer",
"Learn Software Development Lifecycle (SDLC) (1-2 months) > Study Software Testing Fundamentals (2-3 months) > Learn Manual Testing and Test Case Creation (3-4 months) > Dive into Automation Testing (Selenium, etc.) (3-4 months) > Test and Validate Software Products (6+ months)",

"How to become a Software Engineer",
"Learn a Programming Language (e.g., Python, Java, C++) (1-2 months) > Learn Data Structures and Algorithms (2-3 months) > Build Projects and Gain Experience (3-6 months) > Study Advanced Topics and Frameworks (6+ months)",

"How to become a Data Scientist",
"Learn Programming (Python or R) (1-2 months) > Study Mathematics and Statistics (2-3 months) > Learn Data Manipulation and Analysis Libraries (Pandas, Numpy) (1-2 months) > Study Machine Learning and Deep Learning (3-4 months) > Work on Real-world Projects (3-6 months)",

"How to become a Mobile App Developer",
"Learn Programming (Java for Android, Swift for iOS) (2-3 months) > Learn Mobile App Development Basics (3-4 months) > Build Simple Apps (3-4 months) > Study UI/UX Design Principles (1-2 months) > Develop Advanced Apps and Publish (6+ months)",

"How to become a DevOps Engineer",
"Learn Linux and Shell Scripting (2-3 months) > Understand Version Control (Git) (1 month) > Study Continuous Integration and Deployment (CI/CD) (1-2 months) > Learn Configuration Management (e.g., Ansible) (1-2 months) > Gain Cloud Platform Knowledge (AWS, Azure, etc.) (2-3 months)",

"How to become a Cybersecurity Analyst",
"Understand Networking Basics (2-3 months) > Learn Operating System Security (2-3 months) > Study Cryptography and Web Security (2-3 months) > Learn Ethical Hacking Techniques (3-4 months) > Gain Practical Experience through Projects (3-6 months)",

"How to become a Data Engineer",
"Learn SQL and Database Management (1-2 months) > Study Big Data Technologies (Hadoop, Spark) (2-3 months) > Learn ETL (Extract, Transform, Load) Processes (2-3 months) > Work with Data Warehousing and Cloud Services (3-4 months) > Build and Optimize Data Pipelines (3-6 months)",

"How to become a UI/UX Designer",
"Study Design Principles and Fundamentals (2-3 months) > Learn Graphic Design and Tools (Adobe XD, Sketch) (2-3 months) > Study User-Centered Design and Usability (2-3 months) > Work on Mock Projects and Prototypes (3-6 months) > Create an Impressive Portfolio (6+ months)",

"What does BIT stand for?",
"BIT stands for Bannari Amman Institute of Technology.",

"Tell me about Bannari Amman Institute of Technology.",
"Bannari Amman Institute of Technology (BIT) is a prominent educational institution known for its quality education and infrastructure.",

"What kind of institution is BIT?",
"Bannari Amman Institute of Technology (BIT) is an institute of higher education that offers various courses and programs in technical fields.",

"Can you give more details about BIT's infrastructure?",
"Bannari Amman Institute of Technology (BIT) boasts modern and well-equipped infrastructure, including state-of-the-art classrooms, labs, libraries, and sports facilities.",

"Where is BIT located?",
"Bannari Amman Institute of Technology (BIT) is located in Sathyamangalam, Erode.",

"What are the key features of BIT's education environment?",
"Bannari Amman Institute of Technology (BIT) provides a conducive learning environment through experienced faculty, interactive sessions, and opportunities for hands-on learning.",

"What programs does BIT offer?",
"Bannari Amman Institute of Technology (BIT) offers a wide range of academic programs in engineering, technology, and other related fields.",

"How is BIT's reputation in terms of education quality?",
"Bannari Amman Institute of Technology (BIT) has built a strong reputation for delivering quality education and producing skilled graduates in various disciplines.",

"Can you share any notable achievements of BIT?",
"Bannari Amman Institute of Technology (BIT) has achieved recognition for its contributions to technical education and has received accolades for student achievements in competitions and projects."

"How does BIT contribute to the education sector?",
"Bannari Amman Institute of Technology (BIT) plays a significant role in shaping the future by providing quality education, fostering innovation, and producing skilled professionals.",

"What is the infrastructure like at Bannari Amman Institute of Technology?",
"Bannari Amman Institute of Technology boasts modern facilities and spacious classrooms as part of its infrastructure.",

"What is available in terms of learning resources at BIT Erode's infrastructure?",
"BIT Erode's infrastructure includes a learning center with a sizable collection of books, periodicals, and other study materials.",

"What facilities can be found in the labs at Bannari Amman Institute of Technology?",
"The Bannari Amman Institute of Technology houses a variety of labs as part of its infrastructure.",

"Does Bannari Amman Institute of Technology offer accommodation options?",
"Yes, hostel accommodations are available at the Bannari Amman Institute of Technology for both male and female students.",

"What additional facilities are accessible to the students and faculty of BIT Erode?",
"Bannari Amman Institute of Technology provides access to sports, gym, medical, transportation, and Wi-Fi facilities to its students and faculty.",

"Is Bannari Amman Institute of Technology (BIT) currently accepting admissions for 2023?",
"Yes, BIT is currently accepting admissions for various programs for the year 2023.",

"Have the placements for 2023 been announced by Bannari Amman Institute of Technology?",
"Yes, Bannari Amman Institute of Technology has released its placements report for 2023.",

"How many companies have visited the Bannari Amman Institute of Technology campus for placements in 2023?",
"According to the placements report, more than 200 companies have visited the campus for placements in 2023.",

"What was the highest package offered during the 2023 placements at BIT?",
"The highest package offered during the 2023 placements at Bannari Amman Institute of Technology was INR 44 LPA.",

"Which company made the highest placement offer in 2023 at BIT?",
"Virtusa made the highest placement offer of INR 44 LPA during the 2023 placements at Bannari Amman Institute of Technology.",

"How extensive is the library collection at Bannari Amman Institute of Technology?",
"Bannari Amman Institute of Technology Library boasts an impressive collection of 83,000 volumes, ensuring a wealth of academic resources.",

"What variety of resources are available in the library?",
"The library features 400 National and International Journals, 6,500 CD-ROMs, and a Digital Library housing 6,000 e-journals.",

"Are there any video courses available at the library?",
"Yes, the library offers 274 NPTEL and 166 NITTTR video courses, providing multimedia learning options.",

"What affiliations or memberships does the library hold?",
"Bannari Amman Institute of Technology is an Institutional member of the British Council Library in Chennai, DELNET in New Delhi, and the INDEST Consortium in New Delhi.",

"How many beds are available in the Boys Hostel at Bannari Amman Institute of Technology?",
"The Boys Hostel at Bannari Amman Institute of Technology offers accommodation for 2,500 students in both single occupancy and shared rooms.",

"What types of accommodations are available in the Boys Hostel?",
"The Boys Hostel provides both single occupancy and shared rooms for students at Bannari Amman Institute of Technology.",

"How many beds are available in the Girls Hostel at Bannari Amman Institute of Technology?",
"The Girls Hostel at Bannari Amman Institute of Technology offers accommodation for 2,200 students in both single occupancy and shared rooms.",

"What types of accommodations are available in the Girls Hostel?",
"The Girls Hostel provides both single occupancy and shared rooms for students at Bannari Amman Institute of Technology.",

"What are the available labs and facilities at Bannari Amman Institute of Technology?",
"Bannari Amman Institute of Technology offers a range of well-equipped labs including Civil Engineering Lab, Chemistry Lab, Computer Lab, Electrical Lab, Electronics Lab, Language Lab, Mechanical Lab, Physics Lab, Liquid Crystal Research Lab, and more.",

"What specific labs are available for engineering disciplines?",
"Engineering students at Bannari Amman Institute of Technology have access to specialized labs such as Aerodynamics Lab, Modelling and Simulation Lab, Propulsion Lab, Machine Drawing Lab, Biochemistry Lab, and more.",

"Are there labs dedicated to specific subjects like communication and electronics?",
"Yes, there are labs like Digital Communication Lab, Micro Controller Lab, Computer Networks Lab, Dc Machines and Transformers Lab, Ac Machines Lab, and Power Electronics Lab.",

"Are there labs focused on mechanical and thermal engineering?",
"Bannari Amman Institute of Technology provides facilities such as Sensors and Transducers Lab, Thermal Engineering Lab, Concrete Technology Lab, Fluid Mechanics Lab, and Metallurgy Lab.",

"What sports facilities are available at Bannari Amman Institute of Technology?",
"Bannari Amman Institute of Technology offers a range of sports facilities, including a Basketball Court, Cricket Ground, Football Ground, Tennis Court, Volleyball Court, Pool Table, 400 M Athletics Track With Kerb, and Handball Court.",

"Are outdoor sports options available on campus?",
"Yes, outdoor sports enthusiasts can enjoy facilities such as Cricket Ground, Football Ground, Tennis Court, Volleyball Court, and Handball Court at Bannari Amman Institute of Technology.",

"Tell me a joke.",
"Why don't scientists trust atoms? Because they make up everything!",

"What's your favorite color?",
"I'm a chatbot, so I don't have preferences, but I can help you with many things!",

"How's the weather today?",
"I'm sorry, I don't have real-time data. You might want to check a weather app for that!",

"What's your name?",
"I'm a chatbot created by TEAM-UCHIHA. You can call me BITBOT.",

"What should I do if I'm feeling stressed?",
"When feeling stressed, try taking deep breaths and practicing mindfulness to calm your mind.",

"How do you say 'hello' in Spanish?",
"'Hello' in Spanish is 'Hola.',"

"What's the meaning of life?",
"The meaning of life is a philosophical question that has many interpretations.",

"What do you think about artificial intelligence?",
"I don't have personal beliefs or feelings, but I can provide information on different perspectives.",

"Where were you born?",
"I'm an AI language model created by TEAM-UCHIHA. I don't have a physical birthplace or age.",

"Hello! How are you today?",
"Hello! I'm here and ready to assist you.",

"Hey there, what's new?",
"Hey! Not much on my end, but I'm here to help with whatever you need.",

"Hi, can you tell me a joke?",
"Hi! Of course, here's a joke for you: Why don't scientists trust atoms? Because they make up everything!",

"Good morning! What's the weather like today?",
"Good morning! I'm sorry, but I can't provide real-time weather updates. Is there anything else you'd like to know?",

"Hi, recommend a movie to watch, please.",
"Hello! Certainly, I recommend checking out 'Inception.' It's a mind-bending thriller that's sure to captivate you.",

"Hey, how do I tie a tie?",
"Hey there! To tie a tie, start with the wide end around your neck, cross the narrow end over it, wrap the wide end around the narrow end, then tuck it up and through the loop around your neck.",

"Hi, what's your opinion on AI in healthcare?",
"Hi! I don't have personal opinions, but I can provide information on the various ways AI is being used in healthcare.",

"Hey, where were you created?",
"Hello! I'm an AI language model created by TEAM-UCHIHA. I don't have a physical origin or location.",

"Hi, tell me an interesting fact!",
"Hello! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",

"Hi, tell me a joke about computers.",
"Hello! Sure thing. Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",

"Hey, tell me a fun science fact!",
"Hello! Here's a fun fact: Honeybees can recognize human faces and remember them for a long time.",

"Hey, what's your favorite book?",
"Hello! I don't have personal preferences, but I can recommend some popular books if you'd like.",

"Hi, what's the speed of light?",
"Hello! The speed of light in a vacuum is approximately 299,792,458 meters per second.",

"Give me a funny one-liner.",
"I used to play piano by ear, but now I use my hands.",

"Tell me something to make me laugh.",
"I told my wife she was drawing her eyebrows too high. She seemed surprised.",

"Can you make me smile with a joke?",
"Parallel lines have so much in common. It's a shame they'll never meet.",

"Share a joke to brighten my day.",
"Why did the bicycle fall over? Because it was two-tired!",

"I need a good laugh. What's a joke?",
"Why don't some couples go to the gym? Because some relationships don't work out!",

"Do you know a joke that will crack me up?",
"Why did the math book look sad? Because it had too many problems.",

"In the mood for a joke. Hit me!",
"I used to play piano by ear, but now I use my hands.",

"Feeling down. Joke time?",
"Why don't skeletons fight each other? They don't have the guts.",

"Joke, please!",
"Parallel lines have so much in common. It's a shame they'll never meet.",

"I'm feeling overwhelmed with work. Any advice?",
"Try breaking your tasks into smaller, manageable chunks and prioritize them. Don't forget to take short breaks to recharge.",

"What should I do to improve my focus and productivity?",
"Consider using the Pomodoro Technique: work for 25 minutes, then take a 5-minute break. Repeat this cycle and take a longer break after 4 cycles.",

"I'm having trouble making a decision. Any guidance?",
"List the pros and cons of each option. Consider your long-term goals and how each choice aligns with them. Trust your instincts.",

"How can I reduce stress in my daily life?",
"Practice deep breathing, meditation, or mindfulness. Engage in regular physical activity and find activities you enjoy to relax.",

"Any advice for maintaining a healthy work-life balance?",
"Set clear boundaries between work and personal time. Make time for hobbies, socializing, and self-care to recharge.",

"What's the best way to start learning a new skill?",
"Break the skill into smaller subskills and focus on one at a time. Consistent practice and patience are key to gradual improvement.",

"I want to be more organized. How do I start?",
"Start by decluttering your space. Use tools like to-do lists, calendars, and apps to help you plan and keep track of tasks.",

"How can I boost my self-confidence?",
"Celebrate your achievements, no matter how small. Focus on your strengths and positive qualities. Surround yourself with supportive people.",

"I need motivation to exercise regularly. Any tips?",
"Set specific goals, like aiming for a certain number of workouts per week. Find activities you enjoy, and consider exercising with a friend for accountability.",

"I'm struggling with time management. Any suggestions?",
"Use time-blocking to allocate specific periods for tasks. Prioritize your most important tasks first and minimize distractions during work periods.",

"Tell me an interesting fact.",
"Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",

"Give me a random piece of information.",
"Octopuses have three hearts: two pump blood to the gills, and one pumps it to the rest of the body.",

"Share a fun fact with me.",
"Cows have best friends and can become stressed when they're separated.",

"Tell me something I probably don't know.",
"Bananas are berries, but strawberries are not.",

"Do you have any surprising facts?",
"The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",

"Can you impress me with a fact?",
"There are more possible iterations of a game of chess than there are atoms in the known universe.",

"Tell me a mind-blowing fact.",
"A day on Venus is longer than its year. Venus takes about 243 Earth days to rotate,"

"What is Python?",
"Python is a versatile, high-level programming language known for its readability and simplicity. It's widely used for web development, data analysis, automation, and more.",

"What is Java?",
"Java is a popular, object-oriented programming language known for its platform independence. It's used for building a wide range of applications, including web and mobile apps.",

"What is JavaScript?",
"JavaScript is a dynamic scripting language commonly used for adding interactivity to websites. It's executed in web browsers, allowing for client-side interactions.",

"What is C++?",
"C++ is a powerful programming language with features of both C and object-oriented programming. It's used for systems programming, game development, and more.",

"What is Ruby on Rails?",
"Ruby on Rails is a web application framework written in Ruby. It follows the Model-View-Controller (MVC) pattern and simplifies building robust web applications.",

"What is PHP?",
"PHP is a server-side scripting language commonly used for web development. It's embedded in HTML and enables dynamic content generation.",

"What is React?",
"React is a JavaScript library for building user interfaces. It focuses on creating reusable UI components and is often used in front-end development.",

"What is Angular?",
"Angular is a front-end framework for building dynamic web applications. It provides tools for building single-page applications and offers a structured approach to development.",

"What is Node.js?",
"Node.js is a JavaScript runtime that allows developers to run JavaScript on the server side. It's commonly used for building scalable and real-time applications.",

"What is Django?",
"Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the Model-View-Controller (MVC) architectural pattern.",

"What is Swift?",
"Swift is a programming language developed by Apple for building iOS, macOS, watchOS, and tvOS applications. It's designed for performance and safety.",

"What is Kotlin?",
"Kotlin is a modern programming language that runs on the Java Virtual Machine (JVM). It's known for concise syntax and is often used for Android app development.",

"What is Go (Golang)?",
"Go, also known as Golang, is a statically typed language designed for simplicity and efficiency. It's used for systems programming and web development.",

"What is Vue.js?",
"Vue.js is a progressive JavaScript framework for building user interfaces. It's lightweight and easy to integrate into existing projects.",

"What is Flask?",
"Flask is a micro web framework for Python. It's designed to be simple and lightweight, making it a good choice for small to medium web applications.",

"What is Laravel?",
"Laravel is a PHP web framework known for its elegant syntax and features like routing, authentication, and database management.",

"What is Ruby?",
"Ruby is a dynamic, object-oriented programming language known for its focus on developer happiness. It's used for web development, scripting, and more.",

"What is Rust?",
"Rust is a systems programming language focused on safety and performance. It prevents common programming errors while allowing low-level control.",

"What is .NET Core?",
".NET Core is an open-source, cross-platform framework for building modern applications. It supports multiple programming languages and is used for web, desktop, and cloud applications.",

"What is Express.js?",
"Express.js is a minimal and flexible Node.js web application framework. It simplifies building web applications and APIs using JavaScript.",

"What is SQL?",
"SQL (Structured Query Language) is a domain-specific language used for managing and manipulating relational databases. It's used to retrieve, insert, update, and delete data.",

"What is MongoDB?",
"MongoDB is a NoSQL database that stores data in JSON-like documents. It's designed for scalability and flexibility, making it suitable for modern applications.",

"What is Docker?",
"Docker is a platform for developing, shipping, and running applications in containers. Containers provide isolation and portability for software components.",

"What is Kubernetes?",
"Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.",

"What is HTML?",
"HTML (Hypertext Markup Language) is the standard markup language for creating web pages. It defines the structure and content of a webpage using tags.",

"What is CSS?",
"CSS (Cascading Style Sheets) is used to style and format the appearance of HTML elements on a webpage. It defines layout, colors, fonts, and more.",

"What is Git?",
"Git is a distributed version control system used for tracking changes in code. It allows multiple developers to collaborate on projects efficiently.",

"What is Jenkins?",
"Jenkins is an open-source automation server used for building, testing, and deploying software. It supports continuous integration and continuous delivery (CI/CD).",

"What is REST API?",
"REST (Representational State Transfer) API is an architectural style used for designing networked applications. It enables communication between different software systems over the internet.",

"What is Cybersecurity?",
"Cybersecurity involves protecting computer systems, networks, and data from cyber threats. It includes measures to prevent, detect, and respond to security breaches.",

"What is Agile Development?",
"Agile is a software development methodology that emphasizes iterative and incremental development. It focuses on flexibility, collaboration, and customer feedback.",

"What is Virtual Reality (VR)?",
"VR is a technology that immerses users in a simulated environment. It typically involves the use of headsets to create an interactive 3D experience.",

"What is Machine Learning?",
"Machine learning is a subset of artificial intelligence (AI) that enables computers to learn from data and make predictions or decisions without being explicitly programmed.",

"What is Internet of Things (IoT)?",
"IoT refers to a network of interconnected devices (things) that can communicate and exchange data over the internet. It enables automation and data analysis.",

"What is DevOps?",
"DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to automate and streamline the software delivery process.",

"What is Quantum Computing?",
"Quantum computing uses quantum bits (qubits) to perform complex calculations. It has the potential to solve problems that are currently infeasible for classical computers.",

"What is Responsive Web Design?",
"Responsive web design is an approach to designing websites that adapt and look good on various screen sizes and devices, from desktops to smartphones.",

"What is Serverless Computing?",
"Serverless computing allows developers to build and run applications without managing traditional server infrastructure. It's based on functions that run in response to events.",

"What is Blockchain?",
"Blockchain is a decentralized and distributed digital ledger used to record transactions across multiple computers. It's most commonly associated with cryptocurrencies.",

"What is UI/UX Design?",
"UI (User Interface) design focuses on how a user interacts with a product's visual elements, while UX (User Experience) design considers the overall experience and usability.",

"What is Big Data?",
"Big Data refers to large and complex data sets that are difficult to process using traditional methods. It often involves analysis to extract insights and patterns.",

"What is Cloud Computing?",
"Cloud computing involves delivering computing services over the internet, such as storage, processing power, and applications, eliminating the need for on-premises infrastructure.",

"What is Natural Language Processing (NLP)?",
"NLP is a branch of artificial intelligence that focuses on enabling computers to understand, interpret, and generate human language.",

"What is Augmented Reality (AR)?",
"AR is a technology that overlays digital information or virtual elements onto the real world, enhancing the user's perception and interaction with their environment.",

"What is Continuous Integration and Continuous Delivery (CI/CD)?",
"CI/CD is a set of practices that automate the process of building, testing, and deploying software. It ensures frequent and reliable updates to applications.",

"What is Cryptocurrency?",
"Cryptocurrency is a digital or virtual currency that uses cryptography for secure transactions. Bitcoin and Ethereum are well-known examples.",

"What is Flutter?",
"Flutter is an open-source UI software development kit by Google for building natively compiled applications for mobile, web, and desktop from a single codebase.",

"What is CSS Grid?",
"CSS Grid is a layout system in CSS that allows you to create complex grid-based layouts with ease, helping design responsive web pages.",

"What is GraphQL?",
"GraphQL is a query language for APIs that provides a more efficient, flexible, and precise way to request and manipulate data compared to traditional REST APIs.",

"What is Version Control?",
"Version control is a system that manages changes to source code over time. It enables collaboration, tracking of modifications, and reverting to previous versions.",

"What is Microservices Architecture?",
"Microservices architecture is an approach to software development where applications are built as a collection of small, independently deployable services that communicate through APIs.",

"What is Encryption?",
"Encryption is the process of converting data into a code to prevent unauthorized access. It's used to secure sensitive information during transmission and storage.",

"What is a Compiler?",
"A compiler is a software that translates high-level programming code into machine-readable code. It's an essential tool for creating executable programs.",

"What is a Framework?",
"A framework is a pre-built set of tools, libraries, and conventions that provide structure and functionality to facilitate the development of software applications.",

"What is Metadata?",
"Metadata is data that provides information about other data. It describes properties, attributes, and characteristics of files, documents, or resources.",

"What is API Documentation?",
"API documentation provides information about how to use and interact with an API, including details about endpoints, parameters, and response formats.",

"What is Dependency Injection?",
"Dependency injection is a design pattern used in software development to achieve loose coupling between components by providing dependencies from external sources.",

"What is Continuous Testing?",
"Continuous testing is the practice of automatically testing code changes throughout the software development lifecycle to identify defects early and ensure quality.",

"What is the Internet of Things (IoT)?",
"The Internet of Things (IoT) refers to the network of interconnected physical devices embedded with sensors and software that can communicate and exchange data.",

"What is Cloud Native?",
"Cloud native refers to designing and building applications that leverage the capabilities of cloud computing environments, including scalability and resilience.",

"What is Progressive Web App (PWA)?",
"A Progressive Web App (PWA) is a web application that uses modern web technologies to provide a native app-like experience, including offline capabilities and push notifications.",

"What is Cross-Platform Development?",
"Cross-platform development involves creating software that can run on multiple operating systems or platforms, often using frameworks like React Native or Xamarin.",

"What is Encryption Key?",
"An encryption key is a piece of information used in cryptographic algorithms to encode and decode data. It's a crucial component of secure communication.",

"What is Scrum?",
"Scrum is an agile framework used in software development to manage complex projects. It involves iterative development cycles called sprints and emphasizes collaboration.",

"What is Cloud Storage?",
"Cloud storage is a service that allows you to store and access data over the internet. It provides scalability, accessibility, and backup solutions.",

"What is Virtualization?",
"Virtualization is the process of creating virtual versions of computing resources, such as servers, storage, and networks, to improve efficiency and resource utilization."    
]

# chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
# chatterbotCorpusTrainer.train('chatterbot.corpus.english')
  
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def getResponse(request):
    msg = request.GET.get('msg')
    chatResponse = str(bot.get_response(msg)) 
    return HttpResponse(chatResponse)  