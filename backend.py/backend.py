# backend.py

from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Create the database if it doesn't exist
def init_db():
    if not os.path.exists('profiles.db'):
        conn = sqlite3.connect('profiles.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                middle_name TEXT,
                last_name TEXT,
                email TEXT UNIQUE,
                phone TEXT,
                id_number TEXT,
                county TEXT,
                sub_county TEXT,
                ward TEXT
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/profile', methods=['POST'])
def save_profile():
    data = request.form

    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')
    id_number = data.get('ID_number')
    county = data.get('county')
    sub_county = data.get('sub-county')
    ward = data.get('ward')

    try:
        conn = sqlite3.connect('profiles.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO profiles (first_name, middle_name, last_name, email, phone, id_number, county, sub_county, ward)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, middle_name, last_name, email, phone, id_number, county, sub_county, ward))
        conn.commit()
        conn.close()
        return jsonify({"message": "Profile saved successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred saving the profile."}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
