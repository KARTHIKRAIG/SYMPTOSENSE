# SYMPTOSENSE Database Setup Guide

## Database Information
**Database Name**: PostgreSQL
**Official Download Link**: https://www.postgresql.org/download/

## Step 1: Install PostgreSQL

1. Visit the official PostgreSQL download page: https://www.postgresql.org/download/
2. Select "Windows" as your operating system
3. Click "Download the installer" 
4. Download the latest stable version (recommended: PostgreSQL 16.x)
5. Run the installer as Administrator
6. During installation:
   - Set a password for the 'postgres' user (remember this!)
   - Default port: 5432 (keep default)
   - Default locale: [Default locale] (keep default)
   - Install pgAdmin 4 (recommended for database management)

## Step 2: Create SYMPTOSENSE Database

### Option A: Using pgAdmin (GUI)
1. Open pgAdmin 4
2. Connect to PostgreSQL server (localhost)
3. Right-click "Databases" → "Create" → "Database"
4. Database name: `symptosense_db`
5. Click "Save"

### Option B: Using Command Line
1. Open Command Prompt as Administrator
2. Navigate to PostgreSQL bin directory (usually: `C:\Program Files\PostgreSQL\16\bin\`)
3. Run: `psql -U postgres`
4. Enter your postgres password
5. Create database: `CREATE DATABASE symptosense_db;`
6. Exit: `\q`

## Step 3: Setup Database Schema

1. Open pgAdmin 4 or psql command line
2. Connect to `symptosense_db` database
3. Run the SQL script from `database_setup.sql` file

### Using pgAdmin:
1. Right-click on `symptosense_db` → "Query Tool"
2. Copy and paste the content from `database_setup.sql`
3. Click "Execute" (F5)

### Using Command Line:
```bash
psql -U postgres -d symptosense_db -f database_setup.sql
```

## Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Step 5: Configure Database Connection

1. Open `migrate_to_database.py`
2. Update the `DB_CONFIG` section:
   ```python
   DB_CONFIG = {
       'host': 'localhost',
       'database': 'symptosense_db',
       'user': 'postgres',
       'password': 'YOUR_POSTGRES_PASSWORD_HERE'  # Replace with your password
   }
   ```

3. Open `main_with_database.py`
4. Update the same `DB_CONFIG` section with your password

## Step 6: Migrate CSV Data to Database

```bash
cd "Medication Recommendation System"
python migrate_to_database.py
```

## Step 7: Run SYMPTOSENSE with Database

```bash
python main_with_database.py
```

## Database Tables Created

1. **diseases** - Disease names and descriptions
2. **symptoms** - Symptom names and keys for ML model
3. **precautions** - Disease-specific precautions
4. **medications** - Recommended medications per disease
5. **diets** - Diet recommendations per disease
6. **workouts** - Exercise recommendations per disease
7. **contact_messages** - User contact form submissions
8. **app_settings** - Application configuration (including SYMPTOSENSE branding)

## Benefits of Database Integration

1. **Permanent Storage** - All SYMPTOSENSE branding stored in database
2. **Contact Form Storage** - User messages saved for follow-up
3. **Easy Updates** - Modify app name, developer details via database
4. **Scalability** - Better performance with large datasets
5. **Data Integrity** - ACID compliance ensures data consistency
6. **Backup & Recovery** - Professional database backup capabilities

## Troubleshooting

### Common Issues:
1. **Connection Error**: Check if PostgreSQL service is running
2. **Authentication Failed**: Verify postgres user password
3. **Database Not Found**: Ensure `symptosense_db` database exists
4. **Permission Denied**: Run Command Prompt as Administrator

### Check PostgreSQL Service:
- Windows: Services → PostgreSQL (should be "Running")
- Or run: `net start postgresql-x64-16` (replace 16 with your version)

## Security Notes

1. Change default postgres password after installation
2. Update email passwords in the code before production
3. Use environment variables for sensitive data in production
4. Enable SSL for database connections in production

## Next Steps After Setup

1. Test the application: `http://localhost:5000`
2. Verify database integration by submitting contact forms
3. Check pgAdmin to see stored contact messages
4. Update app settings in database as needed
