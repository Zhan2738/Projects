1. Full_text_mining contains the links for extracting full texts. The first link is about how to extract full texts from PubMed. And the second link is about how to extract full texts from the database S2ORC. Still working on the codes to loop through their full datasets. 


2. abstract_extract_Pubmed_API file: 

>> How to run the codes? 
Running: simplely copy and paste the python code and run it. After this first trunk of the code, you'll need to type into the query keywords and then related abstracts will show up. At the end, maybe you need to change the paths for saving the files.

>> How does it work?
This script uses NCBI E-Utilities (Entrez Programming Utilities, https://www.ncbi.nlm.nih.gov/books/NBK25499/). 
Its completely URL based. You craft "search" and "fetch" commands as URLs and open them in your browser window to access the abstracts.

For example: 
Here is the URL required to execute a PubMed esearch for P2RY8: http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=P2RY8&retmax=50&usehistory=y

This was crafted by putting the following parameters together:

http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi? is the backbone of the esearch function.
db=pubmed specifies that we will be searching the pubmed database.
term=P2RY8 specifies what we will be searching pubmed for. Change this field to whatever you want to search for.
retmax=50 specifies how many abstracts I want to return using the search.
usehistory=y will provide you with a QueryKey and WebEnv id that will let you fetch abstracts from this search.
The “&” signs are just used to separate the different conditions. Make sure to include it starting from after the db=pubmed argument.

The next step is to execute an efetch command by constructing a new URL. Using the WebEnv and QueryKey information given in the above esearch result: 

https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&query_key=1&WebEnv=NCID_1_5757184_130.14.18.48_9001_1579844644_2015135327_0MetA0_S_MegaStore&retstart=0&retmax=50&retmode=text&rettype=abstract

Explanation for this fetch link: 
http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi? is the backbone for a efetch command. Notice that the only difference from this and an esearch command is the part after “/eutils/”.
db=pubmed specifies the database, again.
query_key=1 specifies the number that was given in the “querykey” field in the esearch result.
webenv=NCID_1_5757184_130.14.18.48_9001_1579844644_2015135327_0MetA0_S_MegaStore specifies the ID that was given in the esearch result.
retmode=text specifies that I want the abstracts to be written out in print.
rettype=abstract specifies that I want abstracts shown, as opposed to other types of info that can be given from a PubMed search.

>> Why is this useful?
Even though this version only returns the abstracts, but it can be easily modifed and used to return other information including publication type, authors, PUID, DOI... 


3. abstracts.csv and abstracts.json are the same returned results in different formats after typing query with "LC-MS and validation". 

