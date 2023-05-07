# Example manipulation with database in Python

1. The work consists of developing an application in Python that
make a connection between a Database and text files.
Obs.: All manipulation of the data in the bank must be done via
code.

2. Main points of the work:
* Create a Database with the following tables:

> Person
 
| CPF | First name | Middle name | Last name | Age | Account |
| ------------- | ------------- | ------------- | ------------- |------------- | ------------- |
| ... | ... | ... | ... | ... | ... |


> account

| Agency | Number | Balance | Manager | Age | Holder |
| ------------- | ------------- | ------------- | ------------- |------------- | ------------- |
| ... | ... | ... | ... | ... | ... |


* Populate the tables from a `.txt` file
- The name and account files will be available.
- The program will have to replace spaces with commas.
* Allow addition, removal and editing of any bank line.
* Perform database queries and save the result in
new text files.
    - Organize queries by type in different folders (eg:
consultation by name, by balance, by age, etc.).
    - If the folder does not exist, create a new one.
* Read and print the results of queries through the
created files.
