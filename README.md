# 💊 MedRemind — Medicine Reminder Web App

A full-stack Django web application with a stunning 3D glassmorphism UI.

## Tech Stack
- **Backend**: Django 6.x, Python 3
- **Database**: SQLite (default)
- **Frontend**: HTML5, Custom CSS (3D effects, glassmorphism), Vanilla JS
- **Notifications**: Browser Notification API (no external services)

## Project Structure
```
medreminder/
├── accounts/          # Auth: register, login, logout
├── medicines/         # CRUD for medicines
├── reminders/         # CRUD for reminders + toggle
├── dashboard/         # Main dashboard view
├── templates/         # All HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── medicines/
│   ├── reminders/
│   └── dashboard/
├── static/
│   ├── css/styles.css   # 3D + glassmorphism + animations
│   └── js/notifications.js  # Browser notification system
└── manage.py
```

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# 1. Clone the repository
git clone <repository-url>
cd medreminder

# 2. Run automated setup (creates venv, installs deps, runs migrations, seeds data)
python setup.py

# 3. Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 4. Start server
python manage.py runserver

# 5. Open browser and login
#    http://127.0.0.1:8000/
#    Username: demo
#    Password: demo123
```

### Option 2: Manual Setup
```bash
# 1. Clone the repository
git clone <repository-url>
cd medreminder

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations (includes sample data)
python manage.py migrate

# 4. Start server
python manage.py runserver

# 5. Open browser and login
#    http://127.0.0.1:8000/
#    Username: demo
#    Password: demo123
```

## Sample Data
The project includes comprehensive medicine data that gets created automatically:

### Automatic Medicine Library (50+ Common Medicines)
- **New users**: Automatically receive 50+ common medicines when they register
- **Existing users**: Run `python manage.py add_common_medicines` to add the full library
- **Categories included**: Pain relief, antibiotics, cardiovascular, diabetes, vitamins, allergy medications, and more
- **Realistic data**: Each medicine includes proper dosage, category, and typical quantities

### Legacy Sample Data
The project also includes sample medicines data that gets created automatically when you run migrations. This includes:
- 15 common medicines with realistic dosages
- Tablet quantities ranging from 6-100 tablets
- A demo user account (username: `demo`, password: `demo123`)

### Manual Sample Data Creation
If you need to create sample data for a different user:
```bash
# Create sample data for a specific user
python manage.py create_sample_medicines --username myuser --password mypass

# Add 50 tablets to all existing medicines
python manage.py add_tablets --quantity 50

# Add common medicines to all users
python manage.py add_common_medicines

# Add common medicines to specific user only
python manage.py add_common_medicines --user username

# View medicine statistics
python manage.py medicine_stats
```

## Features
- ✅ User registration & login (Django auth)
- ✅ **NEW**: 50+ common medicines automatically added to new users
- ✅ Add/Edit/Delete medicines with tablet quantity tracking
- ✅ Set multiple time-based reminders per medicine
- ✅ **NEW**: Add medicines directly from reminder form (inline medicine creation)
- ✅ Toggle reminders active/paused
- ✅ Dashboard with live clock + active reminder cards + medicine statistics
- ✅ Browser push notifications (checks every minute)
- ✅ Tablet inventory management with visual indicators
- ✅ Sample data included for quick demo
- ✅ 3D glassmorphism UI with floating medical artifacts
- ✅ 3D tilt effect on hover (mousemove perspective)
- ✅ Floating pill, sphere, cross, ring animations
- ✅ Responsive mobile layout

## Enhanced Reminder Creation
When creating a new reminder at `/reminders/add/`, users can now:
1. **Select existing medicine** from their medicine list, OR
2. **Add new medicine inline** by checking "Add new medicine instead"
   - Enter medicine name, category, dosage, and quantity
   - Medicine is automatically created and linked to the reminder
   - Perfect for users who don't have any medicines set up yet

This streamlined workflow eliminates the need to navigate between different sections when setting up reminders.

## UI Design Notes
- **Glassmorphism**: backdrop-filter blur + rgba backgrounds
- **3D Cards**: CSS perspective + rotateX/Y on mousemove
- **Hero**: CSS-only rotating sphere (no Three.js dependency needed)
- **Artifacts**: Pure CSS pills, spheres, crosses, rings
- **Theme**: Dark space gradient + indigo/cyan accent palette

## Notification Logic
- Checks current time every 60 seconds
- Compares against all active reminder times (HH:MM)
- Shows browser notification if permission granted
- Falls back to in-app toast if permission denied
- Prevents duplicate alerts using a JavaScript Set per session
