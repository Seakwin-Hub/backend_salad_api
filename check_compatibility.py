#!/usr/bin/env python3
"""
Check if all required packages are compatible with Python 3.11.8
"""
import sys
import pkg_resources

# Required packages
required_packages = [
    'Flask==2.3.3',
    'Flask-RESTful==0.3.10',
    'Flask-SQLAlchemy==3.0.5',
    'mysqlclient==2.2.0',
    'psycopg2-binary==2.9.7',
    'python-dotenv==1.0.0',
    'gunicorn==21.2.0',
    'Werkzeug==2.3.7',
]

def check_compatibility():
    print(f"Python version: {sys.version}")
    print("Checking package compatibility...")
    
    for package in required_packages:
        try:
            pkg_name, pkg_version = package.split('==')
            dist = pkg_resources.get_distribution(pkg_name)
            if dist.version == pkg_version:
                print(f"✓ {pkg_name} {pkg_version} is compatible")
            else:
                print(f"⚠ {pkg_name} installed: {dist.version}, expected: {pkg_version}")
        except pkg_resources.DistributionNotFound:
            print(f"✗ {pkg_name} {pkg_version} is not installed")
        except Exception as e:
            print(f"✗ Error checking {package}: {e}")

if __name__ == "__main__":
    check_compatibility()