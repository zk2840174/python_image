

import chromadb
chroma_client = chromadb.Client()


print(chroma_client)


student_info = """
더러워진 하수도를 청소하기 위해서는 베이킹소다와 구연산을 이용합니다. 
"""

club_info = """
구연산은 거품이 일어납니다. 곰팡이 제거에 효과적입니다. 
"""

university_info = """
겨울철에는 벽면에 곰팡이 많이 생깁니다. 
"""

collection = chroma_client.create_collection(name="Students")

collection.add(
    documents = [student_info, club_info, university_info],
    metadatas = [{"source": "student info"},{"source": "club info"},{'source':'university info'}],
    ids = ["id1", "id2", "id3"]
)

results = collection.query(
    query_texts=["세탁"],
    n_results=2
)

print(results)