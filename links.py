listOfAlgorithms = [
    'Data Structures',
    'Geometry',
    'Graph',
    'Math',
    'Sorting',
    'Strings'
]

idForAlgorithms = {
    'Graph': 0,
    'Strings': 1,
    'Data Structures': 2,
    'Math': 3,
    'Sorting': 4,
    'Geometry': 5,
}


search_text = 'Search \U0001f50e'
algorithms_text = 'Algorithms \U0001f4d5'
donation_text = 'Donation \U0001f4b3'

rqToText = {
    '/search': search_text,
    '/algorithms': algorithms_text,
    '/donation': donation_text
}


search_message_text = 'Please write down the tag to find algorithm:'

help_text = """
    I can help you to find algorithms by links
    
You can control me sending these commands:
    
/algorithms - see the full list of algorithms
/search - search the algorithm by some tag
/donation - donate to support the project
"""

welcome_text = """
   \U000026a1  *Welcome to CP Algorithms Finder bot*  \U000026a1
   
This bot helps you to find the algorithm fast.
 
It is useful to find algorithm fast in the contest, or to improve yourself in training.
Write /help to see the useful commands
"""

