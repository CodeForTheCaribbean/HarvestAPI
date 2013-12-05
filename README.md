agriapi
=======

Agricultural API

Built with Django based on http://django-rest-framework.org/

The code is accessible on the web: http://infinite-hamlet-2044.herokuapp.com/ 

TODO:
*need to get data into the heroku database - currently empty
*review farmers resource, eg. add verified dat field
*document process of getting database copied over to API
*create resources for farms(will need to add GPS points), crops, prices(need to look at JAMIS database), receipts, livestock
*finalize the fields that will be exposed
*work on defining international data standards for crops
*define methods for writing back to a database before refreshing DB dump

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
