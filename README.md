# NHS-Referral-Form-Automation
A project designed to use the google drive api to extract data from referral forms saved to the drive and process their data into a structured csv file. This project has the capacity to automate the nhs referral form booking in process. It has been specifically designed to process the ‘SWGLH Genomic Test Request Form’ (https://www.nbt.nhs.uk/sites/default/files/document/GMS%20Test%20Order%20Form%20v1.3.pdf) however other fillable pdf forms can also be processed. 

Key points:

Automates sample processing, reducing processing time to <10 seconds per file.
Removes transcription errors, common in the existing process.
Cloud storage provides seamless data exchange between external clinicians and internal genetic technologists.
Highly adaptable software which can be adapted to extract any additional data field or pull data from other/multiple cloud storage accounts.
This project uses a personal Google Drive account to store form data however this is not UK GDPR complaint. In order to satisfy GDPR-Compliance, the program would have to be modified to use a ‘Google Workspace Account’ configured to adhere to UK-GDPR for business use.
Laboratory implementation dependent on starlims api enabling data upload from csv.

