listOfAlgorithms = [
    'Graph \U0001f4ca',
    'Strings \U0001f4c4',
    'Data Structures \U0001f4d2',
    'Math \U0000270f',
    'Sorting',
    'Geometry \U0001f4d0',
    'Other \U0000269c',
    'Combinatorics \U0001f52d',
]

try_again_text = """
        Please try to write algorithm name correctly. 
You can use /help command to see the list of commands
                                               """
go_back_text = 'Go to the main menu \U00002b05'
idForAlgorithms = {}
for i in range(len(listOfAlgorithms)):
    idForAlgorithms[listOfAlgorithms[i]] = i

search_text = 'Search \U0001f50e'
algorithms_text = 'Algorithms \U0001f4d5'
donation_text = 'Donation \U0001f4b3'
credentials_title = 'Credentials \U0001f4c3'

rqToText = {
    '/search': search_text,
    '/algorithms': algorithms_text,
    '/donation': donation_text
}


search_message_text = 'Please write down the tag to find algorithm:'

credentials_text = """
    The project has been created by Khibadullin Orazbek
    
The algorithm sources are taken from:

1. https://github.com/askdfjlas/cp-algorithms    
2. https://github.com/Skeef79/CP-Algo/ 
3. https://github.com/AllAlgorithms/ 
4. https://github.com/sbmaruf/Algorithms-Code-Library/
5. https://github.com/ADJA/algos/
"""

help_text = """
    I can help you to find algorithms by links
    
You can control me sending these commands:
    
/algorithms - see the full list of algorithms
/search - search the algorithm by some tag
"""
# /donation - donate to support the project
# Add then
welcome_text = """
   \U000026a1  *Welcome to CP Algorithms Finder bot*  \U000026a1
   
This bot helps you to find the algorithm fast.
 
It is useful to find algorithm fast in the contest, or to improve yourself in training.
Write /help to see the useful commands
"""

donation_answer = """
  \U0001f495  If you think this project is really helpful you can donate by this link \U0001f495
Link: https://yoomoney.ru/to/4100117611389694   
Thank you!
"""

