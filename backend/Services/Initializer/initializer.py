"""File for initializing services."""
from .countries_initializer import initialize_countries
from Services.database import initialize_database
from dotenv import load_dotenv

load_dotenv()


def initialize_services():
    """Initialize services."""

    # Initialize database with models
    initialize_database()

    # Add all countries to database
    initialize_countries()