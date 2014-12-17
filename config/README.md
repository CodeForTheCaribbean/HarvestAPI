# Local settings configuration file

This file describes the steps necessary in setting up the application on your custom infrastructure.  This has been tested on a heroku infrastructure.

## Creation
It is important to note that the application will search for a file called `local_settings.ini` in order to setup the application.  This file contains settings that should be local to your infrastructure.  The `local_settings_template.ini` file provided is to be used as a guide. 

## Modification
The first step is to copy the `local_settings_template.ini` file and rename it to `local_settings.ini`.  Modify the parameters suitable to your infrastructure.  You may use the `harvestapi/settings.py` file as a reference.  Comments are provided that describe the parameter you are modifying within the `settings.py` file.

## Author 
Matthew Budram