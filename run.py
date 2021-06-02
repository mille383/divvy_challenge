from app import app, db
from app.models import Ride

@app.shell_context_processor
def make_shell_context():
    # ALWAYS HAVE TO RETURN A PYTHON DICTIONARY FROM CONTEXT
    return {
        'db': db,
        'Ride': Ride
    }

# app = create_app()