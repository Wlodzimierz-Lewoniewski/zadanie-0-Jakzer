import regex as re
import pandas as pd

docs=[]
queries = []
n_doc=input("liczba dokumentow")
for i in range(int(n_doc)):
    docs.append(input("doc"))
n_query=input("liczba query")
for i in range(int(n_query)):
    queries.append(input("query"))
records =[]
def preprocess_doc(text):
    text = "".join(re.findall(r"[\w\s]",text))
    text = re.sub(r"\s",' ',text).strip()
    text = re.sub(r"\s+",' ',text).lower().split()
    return text
docs = [preprocess_doc(doc) for doc in docs]
for query in queries:
    records = []
    for doc in docs:
        records.append(
            {
                'doc':" ".join(doc),
                'count':doc.count(query)
            }
        )
    df =pd.DataFrame(records)
    df = df[df['count'] != 0].reset_index()
    df = df.sort_values(by=['count', 'index'], ascending=[False, True])
    print(list(df['index'].to_list()))
