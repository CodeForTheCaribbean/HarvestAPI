agriapi
=======

Agricultural API

Built with Django based on http://django-rest-framework.org/

The code is accessible on the web: http://agriapi.herokuapp.com/ 

TODO:
* review resources, eg. add 'verified date' field, remove 'farmer_idx' field, etc.
* document process of getting database copied over to API
* create resources for prices, livestock
* finalize the fields that will be exposed and access levels/privacy/permissions
* work on defining international data standards for crops

#API Documentation: 
-Rationale(Why): 
Increasingly stakeholders are requesting more agricultural information from the Ministry of Agriculture and Fisheries and the Rural Agricultural Development Authority.

##-Objectives(What): 
Facilitate secure access to the ABIS and JAMIS data by both internal and external stakeholders. 
Provide opportunities to software developers to create more agricultural related applications.
To support and facilitate the fight against praedial larceny by using Information and Communication Technologies(ICT). 

##-Audience(Who): 
Software developers
Agricultural stakeholders
Government stakeholders
Security forces/interests
Business interests
-Where
Managed cloud based solution
-When
December 2013
##-How
API accessible online
Secure levels of access to the data using user roles and API keys
Procedure (requesting access, etc) 
System administration
Terms of Use
Managing timely updates of the data(automated/batch)
Technical explanation of how (document this with Lisa)

##API Resources:
Below are the various types of data/resources that the API will provide.
Farmers - Listing of farmers in ABIS
Receipts - Listing of receipt books sold to farmers
Farms - Listing of farms/properties, one farmer can have more than one farm
Livestock - Listing of livestock records entered by extension officers
Crops - Listing of crop records collected by RADA extension officers
Prices - Listing of crop price data collected by the Ministry of Agriculture and Fisheries



##Endpoint/Resources - Field Definitions

###Farmers
| Field Name                        | Data Type | Security Level | Nomenclature    | Field range |
|-----------------------------------|-----------|----------------|-----------------|-------------|
| IDX_StakeHolder: int              | INT       |                | farmer_idx      |             |
| StakeHolder_Num: nvarchar(10)     | VARCHAR   |                | farmer_id       |             |
| First_Name: nvarchar(30)          | VARCHAR   |                | first_name      |             |
| Last_Name: nvarchar(30)           | VARCHAR   |                | last_name       |             |
| Alias: nvarchar(30)               | VARCHAR   |                | alias           |             |
| Res_Street_Address: nvarchar(100) | VARCHAR   |                | res_address     |             |
| Res_Parish:  nvarchar(20)         | VARCHAR   |                | res_parish      |             |
| Res_Tele_Num: nvarchar(50)        | VARCHAR   |                | tel_number      |             |
| Cell_Num: nvarchar(20)            | VARCHAR   |                | cell_number     |             |
| Verified_Status: int yes/no       | BOOLEAN   |                | verified_status |             |
| date_of_birth                     | DATE      |                | dob             |             |
| Main_Agri_Activity_Code: int      | VARCHAR   |                | agri_activity   |             |


###Receipts
| Field name      | Date Type | Security Level | Nomenclature         | Field range |
|-----------------|-----------|----------------|----------------------|-------------|
| IDX_StakeHolder | INT       |                | farmer_idx           |             |
| Receipt_No      | INT       |                | receipt_no           |             |
| range1          | INT       |                | rec_range1           |             |
| range2          | INT       |                | rec_range2           |             |
| investigationyn | INT       |                | investigation_status |             |
| remarks         | VARCHAR   |                | remarks              |             |
