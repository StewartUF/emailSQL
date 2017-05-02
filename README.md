# emailSQL
#### SDW 5/2/17

## Overview

This project provides two scripts designed to email a table of iDMD patients and their recommended next visit dates. The table includes a few other data points, such as the patients' visit types and the name of the site thier associated with. The goal of the project is to easily send the iDMD team an easy to use list of the most recent iDMD patient statuses (no, unfortunately it is not "stati").

## Requirements

The following are necessary for the project.

* Python 3.x
Note: This project was designed to work with python 3.x, but may work with earlier versions.
* Python libraries:
    1. pymysql
    2. datetime
    3. json
    4. pdb
    5. smtplib

## Installing Dependencies

Most libraries can be installed to a specific python verision using the format of `pythonX -m pip install <pythonLibrary>` where X is the python root version; i.e., 3 for python 3.6.

## Running the Scripts

Currently, the only function is sending the email. To do this, navigate to the project directory in the terminal and enter `python3 mailing_html.py`. You may run sql_query.py, but no output is produced.

## Configuration

Configuration is currently hard coded into the scripts. The development iDMD sql database is specified in sql_query.py. The emailing service is provided by UF and the email recipient is set as swehmeyer@ufl.edu. This must be changed manually in order to check the content.

Thanks to devmattm, PBC, and PFWhite for their feedback and contributions to this project.