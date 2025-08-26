@echo off
echo ========================================
echo SYMPTOSENSE - GitHub Push Script
echo ========================================
echo.

echo Step 1: Initializing Git repository...
git init

echo Step 2: Adding remote repository...
git remote add origin https://github.com/KARTHIKRAIG/SYMPTOSENSE.git

echo Step 3: Adding all files...
git add .

echo Step 4: Creating initial commit...
git commit -m "Initial commit: SYMPTOSENSE AI Medical Diagnosis System

🏥 AI-Powered Medical Diagnosis System achieving 95.12% accuracy
- Random Forest ML model with comprehensive health recommendations
- Flask web application with modern dark theme UI
- 41 disease classifications, 132 symptom parameters
- Speech recognition and symptom autocorrect features
- Complete documentation and technical analysis

📊 Key Features:
- Real-time disease prediction (<200ms response)
- PostgreSQL database integration
- Responsive Bootstrap 5.3 interface
- Email notification system
- Extensive performance validation

🔬 Technical Achievements:
- 95.12% accuracy, 95.49% precision, 95.12% recall
- 4,920 training samples with robust validation
- Professional web application architecture
- Complete deployment guides and setup instructions

📚 Documentation:
- Comprehensive README and technical analysis
- Performance metrics and validation results
- Database setup guides and migration scripts
- Interactive architecture diagrams and presentations"

echo Step 5: Setting main branch...
git branch -M main

echo Step 6: Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo Push completed successfully!
echo Repository: https://github.com/KARTHIKRAIG/SYMPTOSENSE
echo ========================================
pause
