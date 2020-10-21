# fastapi_voter_project
A rest API used to make searching the Georgia 2020 Absentee/Early Voter information more easily queryable.

https://georgia-voter-fastapi.herokuapp.com/docs

This project contains a triggerable download of the U.S. GA publicly available voter information for Absentee and Early Ballot casts, imports them into a sqlite DB, and then provides a few endpoints to make the information more easily queryable.

Upon succesfully running the project, you can navigate to /docs in the browser to get precise endpoint information. Briefly, it allows the querying of voters by id or name and returns an object (or objects if there are numerous) containing information about that voter-ballot entry.

Voters can have multiple entries if they have multiple ballots (of which only 1 will be flagged with a "ballot_status": "A" showing that is was the accepted ballot. This can happen in the event that someone requests a ballot, then decides instead to vote in person or similar conidtions.


Requirements:
Python 3.7+
Docker (if you want to run a containerized backend)

Installation:
1. Clone/download this repository
2. Run pip install -r requirements.txt
3. Run setup.py

Docker Intallation:
1. Navigate to the root of this project folder
2. Run docker build -t \<name-of-your-image\> --build-arg PORT=\<number\> .
3. Run docker run -d --name \<name of your container\> -p \<local-port-number\>:\<number from above\> \<name-of-your-image-from-above\>

Finally, to access the endpoint docs navigate to localhost:port/docs
