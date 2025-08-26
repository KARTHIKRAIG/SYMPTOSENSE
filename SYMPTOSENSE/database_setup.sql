-- SYMPTOSENSE Database Schema
-- Create database for the SYMPTOSENSE medical recommendation system

-- Create the main database (run this as postgres superuser)
-- CREATE DATABASE symptosense_db;

-- Connect to symptosense_db and run the following:

-- Table for storing disease descriptions
CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing symptoms
CREATE TABLE symptoms (
    id SERIAL PRIMARY KEY,
    symptom_name VARCHAR(255) UNIQUE NOT NULL,
    symptom_key VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing precautions
CREATE TABLE precautions (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(255) NOT NULL,
    precaution_1 VARCHAR(500),
    precaution_2 VARCHAR(500),
    precaution_3 VARCHAR(500),
    precaution_4 VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_name) REFERENCES diseases(disease_name) ON UPDATE CASCADE
);

-- Table for storing medications
CREATE TABLE medications (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(255) NOT NULL,
    medication_list TEXT NOT NULL, -- JSON array of medications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_name) REFERENCES diseases(disease_name) ON UPDATE CASCADE
);

-- Table for storing diet recommendations
CREATE TABLE diets (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(255) NOT NULL,
    diet_recommendations TEXT NOT NULL, -- JSON array of diet recommendations
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_name) REFERENCES diseases(disease_name) ON UPDATE CASCADE
);

-- Table for storing workout recommendations
CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(255) NOT NULL,
    workout_recommendations TEXT NOT NULL, -- JSON array of workout recommendations
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (disease_name) REFERENCES diseases(disease_name) ON UPDATE CASCADE
);

-- Table for storing user contact messages
CREATE TABLE contact_messages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    responded BOOLEAN DEFAULT FALSE
);

-- Table for storing application settings
CREATE TABLE app_settings (
    id SERIAL PRIMARY KEY,
    setting_key VARCHAR(255) UNIQUE NOT NULL,
    setting_value TEXT NOT NULL,
    description TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert application settings with SYMPTOSENSE branding
INSERT INTO app_settings (setting_key, setting_value, description) VALUES
('app_name', 'SYMPTOSENSE', 'Main application name'),
('app_description', 'AI-powered medical symptom analysis and recommendation system', 'Application description'),
('developer_name', 'KARTHIK RAI G', 'Developer name'),
('developer_email', 'KARTHIK9860RAI@GMAIL.COM', 'Developer email'),
('support_email', 'support@symptosense.com', 'Support contact email'),
('app_version', '1.0.0', 'Current application version');

-- Create indexes for better performance
CREATE INDEX idx_diseases_name ON diseases(disease_name);
CREATE INDEX idx_symptoms_key ON symptoms(symptom_key);
CREATE INDEX idx_precautions_disease ON precautions(disease_name);
CREATE INDEX idx_medications_disease ON medications(disease_name);
CREATE INDEX idx_diets_disease ON diets(disease_name);
CREATE INDEX idx_workouts_disease ON workouts(disease_name);
CREATE INDEX idx_contact_messages_email ON contact_messages(email);
CREATE INDEX idx_contact_messages_created ON contact_messages(created_at);
