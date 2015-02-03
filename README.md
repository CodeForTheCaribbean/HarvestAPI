[![Stories in Ready](https://badge.waffle.io/CodeForTheCaribbean/HarvestAPI.png?label=ready&title=Ready)](https://waffle.io/CodeForTheCaribbean/HarvestAPI)
HarvestAPI
=======

![cftc](http://slashroots.org/img/cftc.png)
![srdc](http://slashroots.org/img/srdc.png)

Agricultural API - currently provides Jamaica agriculture data, eg. prices, crops, farms.

Built with Django and REST framework http://django-rest-framework.org/

A demonstartion of the API is accessible on the web: http://harvestdata.herokuapp.com/

TODO:

* review resources, eg. add 'verified date' field, remove 'farmer_idx' field, etc.
* document process of getting database copied over to API
* create resources for prices, livestock
* finalize the fields that will be exposed and access levels/privacy/permissions
* work on defining international data standards for crops


##Installation
This Django project is heavily reliant on Environmental Variables.  To see the various Environment Variables please check out ```config/local_setting_template.ini```.  On your target platform please have ready the following:

*	Postgres Database
*	SendGrid Account
*	A target machine (UNIX preferred)

On your target machine setup the environmental variables with the appropriate values (based on your credentials for DB, SendGrid and target machine).

Pull the repository and first do an install using pip:

```pip install -r requirements.txt```

Then run ```python ./manage.py syncdb```. This will setup the database tables for the application.

And presto!  You should be able to start the application using ```python ./manage.py runserver```.



##API Documentation: 
- Temporary API Documentation page is here: http://harvestapi.developdigitally.com

-Rationale(Why): 
Increasingly stakeholders are requesting more agricultural information from the Ministry of Agriculture and Fisheries and the Rural Agricultural Development Authority.

###-Objectives(What): 
Facilitate secure access to the ABIS and JAMIS data by both internal and external stakeholders. 
Provide opportunities to software developers to create more agricultural related applications.
To support and facilitate the fight against praedial larceny by using Information and Communication Technologies(ICT). 

###-Audience(Who): 
Software developers
Agricultural stakeholders
Government stakeholders
Security forces/interests
Business interests
-Where
Managed cloud based solution

###-How
API accessible online
Secure levels of access to the data using user roles and API keys
Procedure (requesting access, etc) 
System administration
Terms of Use
Managing timely updates of the data(automated/batch)
Technical explanation of how (document this with RADA tech team)

###API Resources:
Below are the various types of data/resources that the API currently provides.
Farmers - Listing of farmers in ABIS
Receipts - Listing of receipt books sold to farmers
Farms - Listing of farms/properties, one farmer can have more than one farm
Livestock - Listing of livestock records entered by extension officers
Crops - Listing of crop records collected by RADA extension officers
Prices - Listing of crop price data collected by the Ministry of Agriculture and Fisheries



###Endpoint/Resources - Field Definitions

####Farmers
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


