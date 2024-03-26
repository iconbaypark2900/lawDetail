import sqlite3  # Imports the sqlite3 library to interact with SQLite databases.

def setup_database():
    # Establishes a connection to the SQLite database file 'legallogix_extended.db'. Creates the file if it doesn't exist.
    conn = sqlite3.connect('legallogix_extended.db')
    cur = conn.cursor()  # Creates a cursor object to execute SQL commands.

    # Executes a script to drop existing tables if they exist. This ensures a fresh start for the database setup.
    cur.executescript('''
    DROP TABLE IF EXISTS Defendants;
    DROP TABLE IF EXISTS Charges;
    DROP TABLE IF EXISTS CaseFiles;
    ''')

    # Executes a script to create new tables with a normalized schema.
    cur.executescript('''
    CREATE TABLE Defendants (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique identifier for each defendant, automatically incremented.
        DefendantName TEXT UNIQUE NOT NULL  # Name of the defendant, must be unique and not null.
    );

    CREATE TABLE Charges (
        ChargeID INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique identifier for each charge, automatically incremented.
        Charge TEXT NOT NULL  # Text description of the charge, cannot be null.
    );

    CREATE TABLE CaseFiles (
        FileID INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique identifier for each case file, automatically incremented.
        DefendantID INTEGER,  # References the ID from the Defendants table.
        ChargeID INTEGER,  # References the ChargeID from the Charges table.
        Description TEXT NOT NULL,  # Description of the case file.
        FOREIGN KEY(DefendantID) REFERENCES Defendants(ID),  # Establishes a foreign key relationship with the Defendants table.
        FOREIGN KEY(ChargeID) REFERENCES Charges(ChargeID)  # Establishes a foreign key relationship with the Charges table.
    );
    ''')

    # Inserts sample data into the Defendants and Charges tables.
    defendants = ['Ann Walker', 'Juan Stewart', 'Carlos Sanders']
    charges = ['AGGRAVATED FLEE OR ATTEMPT TO ELUDE POLICE', 'AGG BATTERY ON A PREGNANT WOMAN', 'CONTROLLED SUBSTANCE WITHOUT PRESCRIPTION']

    for defendant in defendants:
        cur.execute('INSERT INTO Defendants (DefendantName) VALUES (?)', (defendant,))
    
    for charge in charges:
        cur.execute('INSERT INTO Charges (Charge) VALUES (?)', (charge,))

    # Inserts sample data into the CaseFiles table, linking defendants and charges through their IDs.
    cur.execute('INSERT INTO CaseFiles (DefendantID, ChargeID, Description) VALUES (1, 1, "Case Description 1")')
    cur.execute('INSERT INTO CaseFiles (DefendantID, ChargeID, Description) VALUES (2, 2, "Case Description 2")')
    cur.execute('INSERT INTO CaseFiles (DefendantID, ChargeID, Description) VALUES (3, 3, "Case Description 3")')

    conn.commit()  # Commits the transaction to save changes to the database.
    conn.close()  # Closes the connection to the database.

setup_database()  # Calls the setup_database function to execute the database setup.

