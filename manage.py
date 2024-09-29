#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # Check if DJANGO_SETTINGS_MODULE is set correctly
    if os.environ.get('DJANGO_SETTINGS_MODULE') != 'bona_blog.settings':
        print("Warning: DJANGO_SETTINGS_MODULE is not set to 'bona_blog.settings'")
        print(f"Current value: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
        print("Setting DJANGO_SETTINGS_MODULE to 'bona_blog.settings'")
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bona_blog.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    print(f"Using settings module: {os.environ['DJANGO_SETTINGS_MODULE']}")
    execute_from_command_line(sys.argv)
