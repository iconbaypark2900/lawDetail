from pymongo import MongoClient
from pymongo import WriteConcern
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import ReadPreference

# Establish a connection to the MongoDB instance.
client = MongoClient('mongodb://localhost:27017/')
# Select the database within MongoDB where operations will be performed.
db = client.legallogix_db

# Insert a document into the 'documents' collection. This document includes nested structures and arrays.
db.documents.insert_one({
    "title": "Case File: 001",
    "defendant": "Ann Walker",
    "charges": [
        {"description": "Aggravated Fleeing", "date": "2024-01-01", "outcome": "Pending"},
        {"description": "Larceny Theft", "date": "2024-01-02", "outcome": "Convicted"}
    ],
    "filed_on": "2024-01-01",
    "status": "Open",
    "annotations": [
        {"author": "John Doe", "text": "Important case for precedent.", "date": "2024-02-01"}
    ]
})

# Query the 'documents' collection to find all documents where "Ann Walker" is listed as the defendant.
cases = db.documents.find({"defendant": "Ann Walker"})

# Query the 'documents' collection to find all documents that contain charges with an "outcome" of "Convicted".
convicted_charges = db.documents.find({"charges.outcome": "Convicted"})

# Initiating a session for a transaction to ensure atomic operations.
with client.start_session() as session:
    # Start the transaction with specific read and write concerns and read preference.
    session.start_transaction(
        read_concern=ReadConcern("local"),  # Specifies the read concern level for the transaction.
        write_concern=WriteConcern("majority"),  # Specifies the write concern level to ensure writes are acknowledged by a majority.
        read_preference=ReadPreference.PRIMARY  # Specifies that reads during the transaction should be from the primary replica set member.
    )

    try:
        # Within the transaction, update the status of a specific document and insert a log entry into the 'audit_log' collection.
        db.documents.update_one({"title": "Case File: 001"}, {"$set": {"status": "Closed"}}, session=session)
        db.audit_log.insert_one({"message": "Closed Case File: 001", "date": "2024-03-01"}, session=session)
        
        # If the above operations are successful, commit the transaction.
        session.commit_transaction()
    except Exception as e:
        # If there's an error during the transaction, output the error message and abort the transaction.
        print(f"Transaction aborted due to an error: {e}")
        session.abort_transaction()
