# -*- coding: utf-8 -*
from sys import argv
from os import system
try: from email_validator import validate_email, EmailNotValidError
except: 
	system("python -m pip install email_validator")
	from email_validator import validate_email, EmailNotValidError
try: import tqdm
except:
	system("python -m pip install tqdm")
	import tqdm
from multiprocessing import Pool
LOGO='''


        *             (    (                               
      (  `            )\ ) )\ )                            
 (    )\))(     (    (()/((()/(                            
 )\  ((_)()\    )\    /(_))/(_))                           
((_) (_()((_)  ((_)  (_)) (_))                             
| __||  \/  | /__ _\ |_ _|| |                              
| _| | |\/| |// _` |\ | | | |__                            
|___||_|  |_|\\__,_|/|___||____|                           
              \(___/ (    (                          (     
               )\ )  )\ ) )\ )           *   )    )  )\ )  
 (   (   (    (()/( (()/((()/(     (   ` )  /( ( /( (()/(  
 )\  )\  )\    /(_)) /(_))/(_))    )\   ( )(_)))\()) /(_)) 
((_)((_)((_)  (_))  (_)) (_))_    ((_) (_(_())((_)\ (_))   
\ \ / //__ _\ | |   |_ _| |   \  /__ _\|_   _|/  (_)| _ \  
 \ V /// _` |\| |__  | |  | |) |// _` |\ | | | () | |   /  
  \_/ \\__,_|/|____||___| |___/ \\__,_|/ |_|  \__/  |_|_\  
       \____/                    \____/                    

                         
                   
		@KTN - 0x666
'''

def email_validator(email):
	bad = ["'",
			"/",
			"+",
			"*"]
	if [case for case in bad if case in email]: pass
	else:
		try:
			valid = validate_email(email,allow_smtputf8=False)
			open("valid_emails.txt","a").write(email+"\n")
		except EmailNotValidError as e: pass
if __name__ == '__main__':
	print(LOGO)
	print("[+] USAGE: {} EMAILS.txt (NUM OF THREAD)".format(argv[0]))
	try:
		with open(argv[1]) as f: emails = f.read().splitlines()
		pool = Pool(int(argv[2]))
		print("[!] CHECKING EMAILLIST...")
		for _ in tqdm.tqdm(pool.imap_unordered(email_validator, emails), total=len(emails)): pass
	except Exception as e: print(str(e))
