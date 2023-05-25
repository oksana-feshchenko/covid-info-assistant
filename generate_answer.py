from connect_db import connect_to_db


def return_answer(question):
    model = connect_to_db()
    return model({"query": question}, return_only_outputs=True)["result"]
