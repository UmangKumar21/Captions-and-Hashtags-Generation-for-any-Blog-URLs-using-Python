# Captions-and-Hashtags-Generation-for-any-Blog-URLs-using-Python
To write the code to generate the Captions and Hashtags of any blog URLs to upload or share on Facebook, LinkedIn, Twitter, or any other social media platform using Python.

GOALS
    Generate the dynamically Captions and Hashtags for a blog URL.
    
METHODS
1.	First we have to fetch the Blogs URLs when it will requests to us.
2.	Now, we have to extract the all contents from the Blog URLs.
3.	Split those all extracted contents or sentences into the words.
4.	And now generate the Captions from those words.
5.	Here we will install nltk package and import them for filter the words and recognize the tokens (Noun, Verb, Obj, etc..) 
6.	After recognizing the Tokens System will be asked for blog_url and then It will generate the both captions and hashtags for the Blog URLs.


Input
    Blog_url  = “https://nec.edu.in/blog/”


Output
Captions: 
Caption 1: National Engineering College / Blog The award was given by Dr.K.K.Surappa, Vice chancellor, Anna 
Caption 2: University and was received by from left NEC NSS Programme officer Mr.J.Thamba, NEC NSS Secretary
Caption 3: Mr.S.Thanga… From Left : Mr.M.Veera Shanthi Ram receiving winning memento from Heike Mock, Director 
Caption 4: (DAAD) on 07th April 2018 at Jadavpur Univeristy, Dr.Michael Feiner (Consul General… 2017–2018 
Caption 5: Engineering Cut-off List Lakshmi Ammal Memorial 10th All India Hockey Tournament - 2018 was held 
Caption 6: during May 17 - 27, 2018 National Engineering College, Kovilpatti NCC units 2/9(TN) SIG. COY. NCC, 
Caption 7: Tirunelveli and 3(TN) GIRLS BN NCC, Tirunelveli conducted Nominal roll from 07.00 am to 08.00… NEC 
Caption 8: is preparing to provide new innovative platform, for its student community including alumni, to 
Caption 9: initiate new venture "Startup" in the campus. Ir this context,… The college offers various 
Caption 10: engineering and technology courses, many of which are accredited by the National Board of 
Caption 11: Accreditation. These courses provide a syllabus that… © National Engineering College 2023 | All 
Caption 12: rights reserved.

Hashtags:
#engineering
#national
#college
#nec
#ncc
#left
#nss
#tn
#tirunelveli
#provide
#new
#courses
#blog
#award
#given
#vice
#chancellor
#anna
#university
#received
[nltk_data] Downloading package punkt to /root/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package stopwords to /root/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
