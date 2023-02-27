from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

# Define the route for adding an email address to the database
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    conn = sqlite3.connect('emails.db')
    conn.execute("INSERT INTO emails (email) VALUES (?)", (email,))
    conn.commit()
    conn.close()
    return redirect('/thank-you')

# Connect to the database
conn = sqlite3.connect('emails.db')

# Create the email table if it doesn't already exist
conn.execute('''CREATE TABLE IF NOT EXISTS emails
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  email TEXT);''')

# Insert some example data into the email table
conn.execute("INSERT INTO emails (email) VALUES (?, ?)", ('john@example.com'))
conn.execute("INSERT INTO emails (email) VALUES (?, ?)", ('jane@example.com')) 
conn.execute("INSERT INTO emails (email) VALUES (?, ?)", ('greentrinket@gmail.com'))
conn.execute("INSERT INTO emails (email) VALUES (?, ?)", ('bob@example.com'))
conn.commit()

# Close the connection to the database
conn.close()