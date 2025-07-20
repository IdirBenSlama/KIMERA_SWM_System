#!/usr/bin/env python3
"""
Canonical Console Printer for Kimera SWM
========================================

This module provides a centralized, single source of truth for all
user-facing console output across the Kimera codebase, especially for
high-level orchestration scripts, demos, and test runners.

It separates the concern of user-facing CLI presentation from system logging.
"""

import shutil

def get_terminal_width(default=80):
    """Gets the current terminal width."""
    return shutil.get_terminal_size((default, 20)).columns

def print_header(title: str, char: str = "=", width: int = None):
    """Prints a standardized header."""
    if width is None:
        width = get_terminal_width()
    print("\n" + char * width)
    print(title.center(width))
    print(char * width)

def print_subheader(title: str, char: str = "-"):
    """Prints a standardized subheader."""
    print(f"\n--- {title} ---")

def print_kv(key: str, value: str, indent: int = 2):
    """Prints a key-value pair."""
    print(f"{' ' * indent}{key}: {value}")

def print_list(items: list, indent: int = 2):
    """Prints a list of items."""
    for item in items:
        print(f"{' ' * indent}• {item}")

def print_major_section_header(title: str, char: str = "🌟"):
    """Prints a visually distinct major section header for server startup."""
    width = get_terminal_width()
    border = char * width
    print("\n" + border)
    print(char + " " * (width - 2) + char)
    print(char + title.center(width - 2) + char)
    print(char + " " * (width - 2) + char)
    print(border)

def print_info(message: str):
    """Prints an informational message."""
    print(message)

def print_success(message: str):
    """Prints a success message."""
    print(f"✅ {message}")

def print_warning(message: str):
    """Prints a warning message."""
    print(f"⚠️  {message}")
    
def print_error(message: str):
    """Prints an error message."""
    print(f"❌ {message}")

def print_line(char: str = "=", width: int = None):
    """Prints a horizontal line."""
    if width is None:
        width = get_terminal_width()
    print(char * width) 