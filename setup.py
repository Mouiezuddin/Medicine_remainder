import os
import sys
import subprocess
import venv
from pathlib import Path

def run_command(command, description):
    print(f"\n[+] {description}...")
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during {description}: {e}")
        return False
    return True

def setup():
    project_root = Path(__file__).parent
    venv_dir = project_root / ".venv"
    
    # 1. Create Virtual Environment
    if not venv_dir.exists():
        print(f"[+] Creating virtual environment in {venv_dir}...")
        venv.create(venv_dir, with_pip=True)
    else:
        print("[*] Virtual environment already exists.")

    # Determine paths based on OS
    if sys.platform == "win32":
        python_exe = venv_dir / "Scripts" / "python.exe"
        pip_exe = venv_dir / "Scripts" / "pip.exe"
    else:
        python_exe = venv_dir / "bin" / "python"
        pip_exe = venv_dir / "bin" / "pip"

    # 2. Upgrade pip
    if not run_command(f"{python_exe} -m pip install --upgrade pip", "Upgrading pip"):
        return

    # 3. Install requirements
    requirements_file = project_root / "requirements.txt"
    if requirements_file.exists():
        if not run_command(f"{pip_exe} install -r {requirements_file}", "Installing dependencies"):
            return
    else:
        print("[!] requirements.txt not found. Skipping installation.")

    # 4. Run Migrations (includes automatic sample data seeding)
    if not run_command(f"{python_exe} manage.py migrate", "Running database migrations and seeding sample data"):
        return

    # 5. Create additional demo user if needed
    print("\n[+] Setting up demo environment...")
    run_command(f"{python_exe} manage.py create_sample_medicines --username demo --password demo123", "Creating additional demo data")

    # 6. Success Message
    print("\n" + "="*60)
    print("      🎉 MEDREMINDER SETUP COMPLETE! 🎉")
    print("="*60)
    print("\n📋 Your medicine reminder app is ready!")
    print("\n🔑 Demo Login Credentials:")
    print("   Username: demo")
    print("   Password: demo123")
    print("\n🚀 To start your application:")
    if sys.platform == "win32":
        print("   1. Activate venv: .\\.venv\\Scripts\\activate")
    else:
        print("   1. Activate venv: source .venv/bin/activate")
    print("   2. Run server:    python manage.py runserver")
    print("   3. Open browser:  http://127.0.0.1:8000/")
    print("\n💊 Sample Data Included:")
    print("   • 15 common medicines with realistic dosages")
    print("   • Tablet quantities for inventory tracking")
    print("   • Ready-to-use demo account")
    print("\nHappy Coding! 🚀\n")

if __name__ == "__main__":
    setup()
