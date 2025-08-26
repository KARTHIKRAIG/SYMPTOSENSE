# SYMPTOSENSE - AI-Powered Medical Diagnosis System

## 🏥 Project Overview

SYMPTOSENSE is an intelligent medical diagnosis system that uses machine learning to predict diseases based on user-reported symptoms. The system provides comprehensive health recommendations including medications, dietary suggestions, workout plans, and precautionary measures.

## 🎯 Key Features

- **AI-Powered Diagnosis**: Uses Random Forest machine learning model for disease prediction
- **Speech Recognition**: Voice input for symptom reporting
- **Comprehensive Recommendations**: Provides medications, diets, workouts, and precautions
- **Web Interface**: Modern, responsive Flask web application
- **Database Integration**: PostgreSQL support for data persistence
- **Email Notifications**: Automated email responses for contact inquiries
- **Multi-Disease Support**: Covers 41 different diseases with 132 symptom parameters

## 📊 Model Performance

Based on the analysis from `Medication.ipynb`, our Random Forest model achieves:

- **Accuracy**: 95.12%
- **Precision**: 95.49% (weighted)
- **Recall**: 95.12% (weighted)
- **F1 Score**: 94.08% (weighted)

### Dataset Statistics
- **Training Data**: 4,920 samples
- **Features**: 132 symptom parameters
- **Diseases**: 41 unique conditions
- **Train/Test Split**: 70/30 (3,444 training, 1,476 testing samples)

## 🏗️ System Architecture

### Core Components

1. **Machine Learning Model**
   - Algorithm: Random Forest Classifier
   - Features: 132 binary symptom indicators
   - Output: Disease classification (41 classes)
   - Model File: `models/model.pkl`

2. **Web Application**
   - Framework: Flask
   - Frontend: Bootstrap 5.3.1 with custom dark theme
   - Speech Recognition: Web Speech API integration

3. **Database System**
   - Primary: PostgreSQL (recommended)
   - Fallback: CSV-based data loading
   - Migration scripts included

### Data Sources

| Dataset | Description | Records |
|---------|-------------|---------|
| `Training.csv` | Main training dataset with symptoms and diagnoses | 4,920 |
| `description.csv` | Disease descriptions and explanations | 41 |
| `medications.csv` | Recommended medications per disease | Variable |
| `diets.csv` | Dietary recommendations per disease | Variable |
| `workout_df.csv` | Exercise recommendations per disease | Variable |
| `precautions_df.csv` | Precautionary measures per disease | Variable |
| `symtoms_df.csv` | Symptom definitions and mappings | 132 |
| `Symptom-severity.csv` | Symptom severity classifications | Variable |

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (optional but recommended)
- Git

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd SYMPTOSENSE
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```

4. **Access the Application**
   - Open browser to `http://localhost:5000`

### Database Setup (Optional)

For enhanced functionality with data persistence:

1. **Install PostgreSQL**
   - Download from: https://www.postgresql.org/download/
   - Follow the installation guide in `DATABASE_SETUP_GUIDE.md`

2. **Create Database**
   ```sql
   CREATE DATABASE symptosense_db;
   ```

3. **Run Migration**
   ```bash
   python migrate_to_database.py
   ```

4. **Use Database Version**
   ```bash
   python main_with_database.py
   ```

## 🔧 Configuration

### Email Configuration
Update email settings in `main.py`:
```python
from_email = 'your_email@gmail.com'
from_password = 'your_app_password'
```

### Database Configuration
Update database settings in `main_with_database.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'symptosense_db',
    'user': 'postgres',
    'password': 'your_password'
}
```

## 📱 Usage

### Web Interface

1. **Symptom Input**
   - Type symptoms manually (e.g., "itching, coughing, fever")
   - Use speech recognition for voice input
   - System includes autocorrect for symptom matching

2. **Diagnosis Results**
   - View predicted disease
   - Access detailed information through modal windows:
     - Disease description
     - Recommended medications
     - Dietary suggestions
     - Exercise recommendations
     - Precautionary measures

### API Endpoints

- `GET /` - Home page
- `POST /predict` - Disease prediction
- `GET /about` - About page
- `GET /contact` - Contact page
- `POST /contact` - Submit contact form
- `GET /developer` - Developer information

## 🧠 Machine Learning Details

### Model Training Process

1. **Data Preprocessing**
   - Missing value imputation (mean for numerical, mode for categorical)
   - Label encoding for categorical variables
   - Binary symptom encoding (0/1)

2. **Model Configuration**
   - Algorithm: Random Forest
   - Estimators: 100 trees
   - Random State: 42 (for reproducibility)

3. **Evaluation Metrics**
   - Cross-validation with 70/30 split
   - Weighted averaging for multi-class metrics
   - Confusion matrix analysis

### Supported Diseases

The system can diagnose 41 different conditions including:
- Fungal infections
- Allergies
- GERD
- Diabetes
- Hypertension
- Heart conditions
- Respiratory diseases
- Gastrointestinal disorders
- Neurological conditions
- And many more...

## 🎨 User Interface

### Design Features
- **Dark Theme**: Modern dark UI with cyan accents (#00bcd4)
- **Responsive Design**: Bootstrap-based responsive layout
- **Interactive Elements**: Hover effects and smooth transitions
- **Modal System**: Organized information display
- **Speech Integration**: Voice input capability

### Navigation
- Home: Main diagnosis interface
- About: Project information
- Contact: User feedback and inquiries
- Developer: Developer information and credits

## 📁 Project Structure

```
SYMPTOSENSE/
├── main.py                    # Main Flask application
├── main_with_database.py      # Database-integrated version
├── migrate_to_database.py     # Database migration script
├── database_setup.sql         # Database schema
├── requirements.txt           # Python dependencies
├── Medication.ipynb          # Model training notebook
├── DATABASE_SETUP_GUIDE.md   # Database setup instructions
├── models/
│   └── model.pkl             # Trained ML model
├── Datasets/                 # Training and reference data
│   ├── Training.csv
│   ├── description.csv
│   ├── medications.csv
│   ├── diets.csv
│   ├── workout_df.csv
│   ├── precautions_df.csv
│   ├── symtoms_df.csv
│   └── Symptom-severity.csv
├── templates/                # HTML templates
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── developer.html
└── static/                   # Static assets
    └── logo.png
```

## 🔬 Technical Implementation

### Symptom Processing
- **Input Parsing**: Comma-separated symptom strings
- **Autocorrect**: Fuzzy matching for symptom recognition
- **Normalization**: Underscore and spacing standardization
- **Vector Encoding**: Binary feature vector creation

### Prediction Pipeline
1. User input → Symptom parsing
2. Autocorrect → Valid symptom matching
3. Feature vector → Binary encoding (132 dimensions)
4. Model prediction → Disease classification
5. Result lookup → Comprehensive recommendations

## 🛡️ Security Considerations

- Input validation and sanitization
- SQL injection prevention (when using database)
- Email configuration security
- Environment variable usage recommended for production

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Considerations
- Use environment variables for sensitive data
- Configure proper database connections
- Set up SSL/TLS for secure communications
- Implement proper logging and monitoring

## 📈 Future Enhancements

- Enhanced model accuracy with more training data
- Multi-language support
- Mobile application development
- Integration with medical databases
- Telemedicine features
- Advanced analytics and reporting

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Implement changes
4. Add tests
5. Submit pull request

## 📄 License

[Add your license information here]

## 👨‍💻 Developer Information

For technical support and inquiries, please use the contact form in the application or refer to the developer page.

---

**Note**: This system is for educational and research purposes. Always consult with qualified medical professionals for actual medical diagnosis and treatment.
