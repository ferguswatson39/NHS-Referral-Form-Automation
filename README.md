# NHS-Referral-Form-Automation
A project designed to use an API to connect to a cloud storage platform (Google Drive) and extract the relevant referral form data from specified folders saved on the Drive. It then saves the referral forms locally on the computer, before reprocessing the data to a structured csv file. It has been specifically designed to process the ‘SWGLH Genomic Test Request Form’ (https://www.nbt.nhs.uk/sites/default/files/document/GMS%20Test%20Order%20Form%20v1.3.pdf) however other fillable pdf forms can also be processed. 

Key points:

- Automates sample processing, reducing processing time to <10 seconds per file.
- Removes transcription errors, common in the existing process.
- Cloud storage provides seamless data exchange between external clinicians and internal genetic technologists.
- Highly adaptable software which can be adapted to extract any additional data field or pull data from other/multiple cloud storage accounts.
- This project uses a personal Google Drive account to store form data however this is not UK GDPR complaint. In order to satisfy GDPR-Compliance, the program would have to be modified to use a ‘Google Workspace Account’ configured to adhere to UK-GDPR for business use.
- Laboratory implementation dependent on starlims api enabling data upload from csv.

