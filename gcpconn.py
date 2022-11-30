from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'/app/utility-braid-367219-790a133797fb.json')

project_id = 'utility-braid-367219'
client = bigquery.Client(credentials= credentials,project=project_id)


def topFour():
    query_job = client.query("""
    SELECT ct.cases_positive_increase/nullif(ct.cases_positive_total, 0)*100 AS newpositive,
    ct.deaths_increase/nullif(ct.deaths_total, 0)*100 AS newdeath,
    ct.hospitalizations_increase/nullif(ct.hospitilzations_current, 0)*100 AS newhospitalization ,
    ct.date FROM `bigquery-public-data.covid19_covidtracking.summary` ct
    order by date asc
    limit 4""")

    results = query_job.result()
    # count = 1
    # for row in results:
    #     if row[0] and row[1] and row[2] is not None:
    #         print(row[0:4])
    #         count += 1
    #         if count == 30:
    #             break
    return results.to_dataframe()
