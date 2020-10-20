from collections import defaultdict


def create_voter_dict(voter_objects_query):
    voter_dict = defaultdict(list)

    for voter in voter_objects_query:
        voter_entry = {
            "ballot_id": voter.ballot_id,
            "first_name": voter.first_name,
            "middle_name": voter.middle_name,
            "last_name": voter.last_name,
            "county": voter.county,
            "ballot_status": voter.ballot_status,
            "status_reason": voter.status_reason,
            "challenged_or_provisional": voter.challenged_or_provisional
        }

        voter_dict[voter.voter_id].append(voter_entry)

    return voter_dict
