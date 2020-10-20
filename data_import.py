import sqlite3

import pandas as pd
import requests
import zipfile
import os


URL = 'https://elections.sos.ga.gov/Elections/downLoadVPHFile.do?https://elections.sos.ga.gov/Elections/downLoadVPHFile.do?nbElecYear=2020&cdElecCat=&idElection=35209&cdFileType=AB&cdStaticFile='


def download_data():
    if os.path.exists('Georgia_Voter_Data_Download.zip'):
        os.remove('Georgia_Voter_Data_Download.zip')

    if os.path.exists('voter_data/ga/STATEWIDE.csv'):
        os.remove('voter_data/ga/STATEWIDE.csv')

    try:
        response = requests.post(URL, stream=True)
        with open('voter_data/ga/Georgia_Voter_Data_Download.zip', 'wb') as fd:
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)

        return True

    except:
        return False


def extract_data():
    try:
        with zipfile.ZipFile('voter_data/ga/Georgia_Voter_Data_Download.zip') as zf:
            zf.extractall(path="voter_data/ga", members=['STATEWIDE.csv'])

            return True

    except:
        return False


def load_db():
    table_names = {
        "County": "county",
        "Voter Registration #": "voter_id",
        "Last Name": "last_name",
        "First Name": "first_name",
        "Middle Name": "middle_name",
        "Suffix": "suffix",
        "Street #": "street_no",
        "Street Name": "street_name",
        "Apt/Unit": "apt_or_unit",
        "City": "city",
        "State": "state",
        "Zip Code": "zip_code",
        "Mailing Street #": "mailing_street_no",
        "Mailing Street Name": "mailing_street_name",
        "Mailing Apt/Unit": "mailing_apt_or_unit",
        "Mailing City": "mailing_city",
        "Mailing State": "mailing_state",
        "Mailing Zip Code": "mailing_zip_code",
        "Application Status": "application_status",
        "Ballot Status": "ballot_status",
        "Status Reason": "status_reason",
        "Application Date": "application_date",
        "Ballot Issued Date": "ballot_issued_date",
        "Ballot Return Date": "ballot_return_date",
        "Ballot Style": "ballot_style",
        "Ballot Assisted": "ballot_assisted",
        "Challenged/Provisional": "challenged_or_provisional",
        "ID Required": "id_required",
        "Municipal Precinct": "municipal_precinct",
        "County Precinct": "county_precinct",
        "CNG": "cng",
        "SEN": "sen",
        "HOUSE	": "house",
        "JUD": "jud",
        "Combo #": "combo_no",
        "Vote Center ID": "vote_center_id",
        "Ballot ID": "ballot_id",
        "Post #": "post_no",
        "Party": "party",
    }

    conn = sqlite3.connect("app.db")

    conn.execute("DELETE FROM 'voter'")

    for chunk in pd.read_csv('voter_data/ga/STATEWIDE.csv', encoding='latin1', low_memory=False, chunksize=10000):
        chunk.rename(columns=table_names, inplace=True)
        chunk.astype(str)
        chunk.to_sql("voter", con=conn, if_exists='append', index=False)

    conn.close()
    return True


def clean_up():
    if os.path.exists('voter_data/ga/Georgia_Voter_Data_Download.zip'):
        os.remove('voter_data/ga/Georgia_Voter_Data_Download.zip')

    if os.path.exists('voter_data/ga/STATEWIDE.csv'):
        os.remove('voter_data/ga/STATEWIDE.csv')


def main():
    data_status = download_data()
    if data_status:
        try:
            extract_status = extract_data()
            if extract_status:
                load_status = load_db()

        except:
            pass

    clean_up()


if __name__ == '__main__':
    main()
