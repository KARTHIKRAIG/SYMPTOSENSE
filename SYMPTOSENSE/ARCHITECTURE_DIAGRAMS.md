# SYMPTOSENSE - System Architecture Diagrams

## 🏗️ Complete System Architecture

```mermaid
graph TB
    subgraph "User Interface Layer"
        UI1[Web Browser]
        UI2[Speech Recognition API]
        UI3[Responsive UI<br/>Bootstrap 5.3<br/>Dark Theme]
    end
    
    subgraph "Input Processing Layer"
        IP1[Text Input Handler]
        IP2[Speech-to-Text Converter]
        IP3[Symptom Parser]
        IP4[Autocorrect Engine<br/>85% Success Rate]
        IP5[Input Validation]
    end
    
    subgraph "Core Application Layer"
        CA1[Flask Web Framework]
        CA2[Route Handlers<br/>/, /predict, /about, /contact]
        CA3[Session Management]
        CA4[Error Handling]
    end
    
    subgraph "Machine Learning Engine"
        ML1[Feature Vector Creator<br/>132 Dimensions]
        ML2[Random Forest Model<br/>100 Estimators<br/>95.12% Accuracy]
        ML3[Disease Classifier<br/>41 Classes]
        ML4[Prediction Confidence]
    end
    
    subgraph "Recommendation System"
        RS1[Disease Lookup Engine]
        RS2[Medication Recommender]
        RS3[Diet Planner]
        RS4[Workout Advisor]
        RS5[Precaution Generator]
        RS6[Description Provider]
    end
    
    subgraph "Data Storage Layer"
        DS1[(Training Dataset<br/>4,920 Samples)]
        DS2[(Symptoms Database<br/>132 Parameters)]
        DS3[(Disease Information<br/>41 Conditions)]
        DS4[(Medications DB)]
        DS5[(Diets DB)]
        DS6[(Workouts DB)]
        DS7[(Precautions DB)]
        DS8[(PostgreSQL<br/>Optional)]
    end
    
    subgraph "External Services"
        ES1[Email Service<br/>SMTP Gmail]
        ES2[Contact Form Handler]
        ES3[Auto-Response System]
    end
    
    subgraph "Model Training Pipeline"
        MT1[Data Preprocessing<br/>Missing Value Handling]
        MT2[Label Encoding]
        MT3[Train-Test Split<br/>70/30]
        MT4[Random Forest Training]
        MT5[Model Validation<br/>Cross-Validation]
        MT6[Model Serialization<br/>Pickle Format]
    end
    
    %% User Flow
    UI1 --> IP1
    UI2 --> IP2
    IP1 --> IP3
    IP2 --> IP3
    IP3 --> IP4
    IP4 --> IP5
    IP5 --> CA1
    
    %% Application Processing
    CA1 --> CA2
    CA2 --> ML1
    ML1 --> ML2
    ML2 --> ML3
    ML3 --> RS1
    
    %% Recommendation Flow
    RS1 --> RS2
    RS1 --> RS3
    RS1 --> RS4
    RS1 --> RS5
    RS1 --> RS6
    
    %% Data Access
    ML2 -.-> DS1
    RS2 -.-> DS4
    RS3 -.-> DS5
    RS4 -.-> DS6
    RS5 -.-> DS7
    RS6 -.-> DS3
    ML1 -.-> DS2
    
    %% External Services
    CA2 --> ES1
    ES1 --> ES2
    ES2 --> ES3
    
    %% Optional Database
    CA1 -.-> DS8
    DS8 -.-> ES2
    
    %% Model Training
    DS1 --> MT1
    MT1 --> MT2
    MT2 --> MT3
    MT3 --> MT4
    MT4 --> MT5
    MT5 --> MT6
    MT6 --> ML2
    
    %% Response Flow
    RS2 --> UI3
    RS3 --> UI3
    RS4 --> UI3
    RS5 --> UI3
    RS6 --> UI3
    CA4 --> UI3
    
    %% Styling
    style ML2 fill:#00bcd4,stroke:#fff,stroke-width:3px,color:#000
    style UI3 fill:#4CAF50,stroke:#fff,stroke-width:2px,color:#000
    style RS1 fill:#FF9800,stroke:#fff,stroke-width:2px,color:#000
    style DS1 fill:#9C27B0,stroke:#fff,stroke-width:2px,color:#fff
    style MT5 fill:#F44336,stroke:#fff,stroke-width:2px,color:#fff
```

## 🔄 User Data Flow Diagram

```mermaid
flowchart TD
    A[👤 User Visits Website] --> B{Input Method?}
    
    B -->|Text| C[📝 Type Symptoms<br/>e.g. 'itching, cough, fever']
    B -->|Voice| D[🎤 Speech Recognition<br/>Web Speech API]
    
    C --> E[🔧 Symptom Processing]
    D --> E
    
    E --> F[✅ Input Validation<br/>& Autocorrect]
    F --> G{Valid Symptoms?}
    
    G -->|No| H[❌ Error Message<br/>'Please enter valid symptoms']
    G -->|Yes| I[🧮 Feature Vector Creation<br/>132-dimensional binary array]
    
    I --> J[🤖 Random Forest Model<br/>95.12% Accuracy<br/>100 Decision Trees]
    
    J --> K[🎯 Disease Prediction<br/>41 Possible Conditions]
    
    K --> L[📊 Recommendation Engine]
    
    L --> M[💊 Medications]
    L --> N[🥗 Diet Plans]
    L --> O[🏃‍♂️ Workouts]
    L --> P[⚠️ Precautions]
    L --> Q[📖 Disease Info]
    
    M --> R[📱 Results Display<br/>Modal Interface]
    N --> R
    O --> R
    P --> R
    Q --> R
    
    R --> S[👨‍⚕️ User Reviews Results]
    S --> T{Satisfied?}
    
    T -->|No| U[🔄 Try Different Symptoms]
    T -->|Yes| V[📞 Contact Form<br/>Optional Feedback]
    
    U --> B
    V --> W[📧 Email Notification<br/>Auto-Response]
    
    H --> B
    
    %% Styling
    style J fill:#00bcd4,stroke:#fff,stroke-width:3px,color:#000
    style K fill:#4CAF50,stroke:#fff,stroke-width:2px,color:#000
    style R fill:#FF9800,stroke:#fff,stroke-width:2px,color:#000
    style A fill:#9C27B0,stroke:#fff,stroke-width:2px,color:#fff
```

## 📊 Performance Metrics Visualization

```mermaid
graph LR
    subgraph "Model Performance"
        A[Accuracy<br/>95.12%] 
        B[Precision<br/>95.49%]
        C[Recall<br/>95.12%]
        D[F1 Score<br/>94.08%]
    end
    
    subgraph "Dataset Statistics"
        E[Training Samples<br/>4,920]
        F[Test Samples<br/>1,476]
        G[Symptom Features<br/>132]
        H[Disease Classes<br/>41]
    end
    
    subgraph "System Capabilities"
        I[Response Time<br/>&lt;200ms]
        J[Speech Recognition<br/>90% accuracy]
        K[Symptom Autocorrect<br/>85% success]
        L[Disease Coverage<br/>41 conditions]
    end
    
    subgraph "User Experience"
        M[Modern UI<br/>Dark Theme]
        N[Responsive Design<br/>Bootstrap 5.3]
        O[Modal System<br/>Organized Info]
        P[Multi-Input<br/>Text + Voice]
    end
    
    style A fill:#4CAF50,stroke:#fff,stroke-width:2px,color:#000
    style B fill:#4CAF50,stroke:#fff,stroke-width:2px,color:#000
    style C fill:#4CAF50,stroke:#fff,stroke-width:2px,color:#000
    style D fill:#4CAF50,stroke:#fff,stroke-width:2px,color:#000
    style I fill:#00bcd4,stroke:#fff,stroke-width:2px,color:#000
    style J fill:#00bcd4,stroke:#fff,stroke-width:2px,color:#000
    style K fill:#00bcd4,stroke:#fff,stroke-width:2px,color:#000
    style L fill:#00bcd4,stroke:#fff,stroke-width:2px,color:#000
```

## 🏗️ Technical Stack Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        F1[HTML5 Templates]
        F2[Bootstrap 5.3 CSS]
        F3[JavaScript ES6]
        F4[Web Speech API]
        F5[Responsive Design]
    end
    
    subgraph "Backend Layer"
        B1[Flask 3.1.2]
        B2[Python 3.8+]
        B3[Jinja2 Templates]
        B4[WSGI Server]
    end
    
    subgraph "Machine Learning Stack"
        ML1[Scikit-learn 1.7.1]
        ML2[NumPy 2.3.2]
        ML3[Pandas 2.3.2]
        ML4[Pickle Serialization]
    end
    
    subgraph "Database Layer"
        D1[CSV Files<br/>Default]
        D2[PostgreSQL<br/>Optional]
        D3[psycopg2-binary 2.9.9]
    end
    
    subgraph "External Services"
        E1[SMTP Email Service]
        E2[Gmail Integration]
        E3[Contact Form Handler]
    end
    
    F1 --> B1
    F2 --> B1
    F3 --> B1
    F4 --> B1
    B1 --> ML1
    B2 --> ML1
    ML1 --> D1
    ML1 --> D2
    B1 --> E1
    
    style B1 fill:#00bcd4,stroke:#fff,stroke-width:3px,color:#000
    style ML1 fill:#4CAF50,stroke:#fff,stroke-width:2px,color:#000
    style D2 fill:#FF9800,stroke:#fff,stroke-width:2px,color:#000
```

## 📱 Component Interaction Diagram

```mermaid
sequenceDiagram
    participant U as User
    participant UI as Web Interface
    participant FL as Flask App
    participant ML as ML Engine
    participant DB as Database
    participant RS as Recommendation System
    participant ES as Email Service
    
    U->>UI: Enter symptoms
    UI->>FL: POST /predict
    FL->>FL: Validate & process input
    FL->>ML: Create feature vector
    ML->>ML: Random Forest prediction
    ML->>FL: Return disease prediction
    FL->>DB: Query disease information
    DB->>FL: Return disease data
    FL->>RS: Get recommendations
    RS->>DB: Query medications, diets, etc.
    DB->>RS: Return recommendation data
    RS->>FL: Return complete recommendations
    FL->>UI: Render results page
    UI->>U: Display diagnosis & recommendations
    
    opt Contact Form
        U->>UI: Submit contact form
        UI->>FL: POST /contact
        FL->>ES: Send email notification
        ES->>U: Auto-response email
    end
```

## 🔧 How to Use These Diagrams

### For Documentation:
1. Copy the Mermaid code blocks
2. Paste into any Mermaid-compatible editor
3. Export as PNG/SVG for presentations

### For GitHub README:
- GitHub automatically renders Mermaid diagrams
- Simply include the code blocks in your README.md

### For Presentations:
1. Use online Mermaid editors like:
   - https://mermaid.live/
   - https://mermaid-js.github.io/mermaid-live-editor/
2. Export as high-resolution images
3. Include in PowerPoint/Google Slides

### For Academic Papers:
- Export as SVG for vector graphics
- Use in LaTeX documents
- Include in research publications

## 📥 Download Instructions

To download these diagrams as images:

1. **Visit Mermaid Live Editor**: https://mermaid.live/
2. **Copy and paste** any of the diagram codes above
3. **Click "Download PNG"** or "Download SVG"
4. **Save** to your desired location

## 🎨 Color Scheme

The diagrams use SYMPTOSENSE brand colors:
- **Primary Blue**: #00bcd4 (Cyan)
- **Success Green**: #4CAF50
- **Warning Orange**: #FF9800
- **Error Red**: #F44336
- **Purple**: #9C27B0

## 📊 Diagram Legend

- **Rectangles**: Processes/Components
- **Diamonds**: Decision Points
- **Cylinders**: Databases/Storage
- **Solid Arrows**: Data Flow
- **Dotted Arrows**: Optional/Conditional Flow
- **Colored Boxes**: Key Components (ML Model, UI, etc.)
