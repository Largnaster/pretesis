
import json
from searchtweets import ResultStream
from searchtweets import gen_rule_payload
from searchtweets import load_credentials

premium_search_args = load_credentials("credentials.yaml", yaml_key="search_tweets", env_overwrite=False)

query = "@V2019N (#COVID19 OR patients OR pandemic OR hospitalization OR virus OR corona OR (tested positive) OR infected OR vaccine)"
rule = gen_rule_payload(query, results_per_call=100, from_date="2020-01-01", to_date="2020-03-31")

rs = ResultStream(rule_payload=rule, max_results=3000, **premium_search_args)
print(rs)

with open('tweetsData.jsonl', 'a', encoding='utf-8') as f:
    for tweet in rs.stream():
        json.dump(tweet, f)
        f.write('\n')
print('done')