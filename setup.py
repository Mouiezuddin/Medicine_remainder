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

    # 4. Run Migrations
    if not run_command(f"{python_exe} manage.py migrate", "Running database migrations"):
        return

    # 5. Seed Data
    print("\n[+] Seeding database with sample medicines...")
    run_command(f"{python_exe} manage.py create_sample_medicines", "Seeding sample medicines")
    run_command(f"{python_exe} manage.py add_tablets", "Adding 3D tablet artifacts")

    # 6. Success Message
    print("\n" + "="*50)
    print("      🎉 SETUP COMPLETE SUCCESSFULLY! 🎉")
    print("="*50)
    print("\nTo start your application:")
    if sys.platform == "win32":
        print(f"  1. Activate venv: .\\.venv\\Scripts\\activate")
    else:
        print(f"  1. Activate venv: source .venv/bin/activate")
    print("  2. Run server:    python manage.py runserver")
    print("\nHappy Coding!\n")

if __name__ == "__main__":
    setup()
