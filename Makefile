.PHONY: run install lint clean

# Set the FLASK_APP environment variable
export FLASK_APP=run.py
export FLASK_ENV=development

# Run the Flask development server
run:
	@echo "Starting Flask development server..."
	@flask run

# Install dependencies from requirements.txt
install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

# Clean up pyc files and __pycache__ directories
clean:
	@echo "Cleaning up..."
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

data_prep:
	@echo "Preparing data..."
	@cd app && python pdf2png.py