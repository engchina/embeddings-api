import jsonlines
import requests


def read_jsonl(path):
    content = []
    with jsonlines.open(path, "r") as json_file:
        for obj in json_file.iter(type=dict, skip_invalid=True):
            content.append(obj)
    return content


def write_one_jsonl(path, content):
    with jsonlines.open(path, "a") as json_file:
        json_file.write(content)


def generate_routing(model, query_text, examples):
    classified_response = requests.post('http://127.0.0.1:7965/v1/classify',
                                        json={'classify_model': model,
                                              'query_text': query_text,
                                              'example_docs': examples}).json()
    print(f"{classified_response=}")
    return classified_response


if __name__ == "__main__":
    classify_model = "text-embedding-3-large"
    examples = [doc for doc in read_jsonl('./examples.jsonl')]
    queries = [doc for doc in read_jsonl('./queries.jsonl')]

    for query in queries:
        print(f"{query['id']=} {query['question']=}")
        query['routing'] = generate_routing(classify_model, query['question'], examples)
        print(f"{query['routing']=}")
        write_one_jsonl('./results_2.jsonl', query)
