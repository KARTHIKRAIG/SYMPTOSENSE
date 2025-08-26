"""
SYMPTOSENSE Database Migration Script
Migrates CSV data to PostgreSQL database
"""

import pandas as pd
import psycopg2
import json
import os
from psycopg2.extras import RealDictCursor

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'symptosense_db',
    'user': 'postgres',
    'password': 'your_password_here'  # Replace with your PostgreSQL password
}

def connect_to_db():
    """Connect to PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def migrate_diseases():
    """Migrate disease descriptions from CSV to database"""
    print("Migrating diseases...")
    df = pd.read_csv('Datasets/description.csv')
    
    conn = connect_to_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        try:
            cursor.execute(
                "INSERT INTO diseases (disease_name, description) VALUES (%s, %s) ON CONFLICT (disease_name) DO UPDATE SET description = EXCLUDED.description",
                (row['Disease'], row['Description'])
            )
        except Exception as e:
            print(f"Error inserting disease {row['Disease']}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Diseases migration completed!")
    return True

def migrate_precautions():
    """Migrate precautions from CSV to database"""
    print("Migrating precautions...")
    df = pd.read_csv('Datasets/precautions_df.csv')
    
    conn = connect_to_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        try:
            cursor.execute(
                """INSERT INTO precautions (disease_name, precaution_1, precaution_2, precaution_3, precaution_4) 
                   VALUES (%s, %s, %s, %s, %s)
                   ON CONFLICT DO NOTHING""",
                (row['Disease'], row['Precaution_1'], row['Precaution_2'], 
                 row['Precaution_3'], row['Precaution_4'])
            )
        except Exception as e:
            print(f"Error inserting precautions for {row['Disease']}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Precautions migration completed!")
    return True

def migrate_medications():
    """Migrate medications from CSV to database"""
    print("Migrating medications...")
    df = pd.read_csv('Datasets/medications.csv')
    
    conn = connect_to_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        try:
            # Convert medication string to proper JSON format
            medication_list = row['Medication']
            cursor.execute(
                """INSERT INTO medications (disease_name, medication_list) 
                   VALUES (%s, %s)
                   ON CONFLICT DO NOTHING""",
                (row['Disease'], medication_list)
            )
        except Exception as e:
            print(f"Error inserting medications for {row['Disease']}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Medications migration completed!")
    return True

def migrate_diets():
    """Migrate diet recommendations from CSV to database"""
    print("Migrating diets...")
    df = pd.read_csv('Datasets/diets.csv')
    
    conn = connect_to_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        try:
            cursor.execute(
                """INSERT INTO diets (disease_name, diet_recommendations) 
                   VALUES (%s, %s)
                   ON CONFLICT DO NOTHING""",
                (row['Disease'], row['Diet'])
            )
        except Exception as e:
            print(f"Error inserting diets for {row['Disease']}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Diets migration completed!")
    return True

def migrate_workouts():
    """Migrate workout recommendations from CSV to database"""
    print("Migrating workouts...")
    df = pd.read_csv('Datasets/workout_df.csv')
    
    conn = connect_to_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        try:
            cursor.execute(
                """INSERT INTO workouts (disease_name, workout_recommendations) 
                   VALUES (%s, %s)
                   ON CONFLICT DO NOTHING""",
                (row['disease'], row['workout'])
            )
        except Exception as e:
            print(f"Error inserting workouts for {row['disease']}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Workouts migration completed!")
    return True

def migrate_symptoms():
    """Migrate symptoms dictionary to database"""
    print("Migrating symptoms...")
    
    # Import symptoms_dict from main.py
    import sys
    sys.path.append('.')
    from main import symptoms_dict
    
    conn = connect_to_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    for symptom_key, symptom_id in symptoms_dict.items():
        try:
            # Convert symptom_key to readable name
            symptom_name = symptom_key.replace('_', ' ').title()
            cursor.execute(
                """INSERT INTO symptoms (symptom_name, symptom_key) 
                   VALUES (%s, %s)
                   ON CONFLICT (symptom_key) DO NOTHING""",
                (symptom_name, symptom_key)
            )
        except Exception as e:
            print(f"Error inserting symptom {symptom_key}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Symptoms migration completed!")
    return True

def main():
    """Main migration function"""
    print("Starting SYMPTOSENSE database migration...")
    print("Make sure PostgreSQL is running and the database 'symptosense_db' exists.")
    print("Update the DB_CONFIG with your PostgreSQL password before running.")
    
    # Check if all CSV files exist
    required_files = [
        'Datasets/description.csv',
        'Datasets/precautions_df.csv',
        'Datasets/medications.csv',
        'Datasets/diets.csv',
        'Datasets/workout_df.csv'
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"Error: Required file {file} not found!")
            return False
    
    # Run migrations
    migrations = [
        migrate_diseases,
        migrate_symptoms,
        migrate_precautions,
        migrate_medications,
        migrate_diets,
        migrate_workouts
    ]
    
    for migration in migrations:
        if not migration():
            print("Migration failed!")
            return False
    
    print("\n✅ All migrations completed successfully!")
    print("SYMPTOSENSE database is ready to use!")
    return True

if __name__ == "__main__":
    main()
