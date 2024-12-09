# AIsuite - Setup and Testing

## Prerequisites

Before you begin, make sure you have the following installed:

- **Git**: To clone the repository.
- **Python**: Version 3.7 or higher (you can download it from [here](https://www.python.org/)).
- **Pip**: To install Python dependencies.

You will also need an API key from Groq to authenticate with their services.

## Steps to Set Up AIsuite

### 1. Clone the Repository

Start by cloning the repository from GitHub to your local machine.

```bash
git clone https://github.com/BenCodeurr/aisuite-test
cd aisuite-test
```

### 2. Create a Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment to isolate dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

### 3. Install Dependencies

Once inside the project directory and virtual environment, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 4. Get Your Groq API Key
You need to create an account on the [Groq website](https://groq.com/) to get your API key. After logging in, follow these steps:
- Go to your Groq dashboard.
- Generate a new API key under the API section.
- Copy the key for later use.

### 5. Set Up the Environment Variables
Create a .env file in the root directory of the project if it doesn't already exist. Add the following line to the .env file, replacing your-api-key with your actual Groq API key.

```bash
GROQ_API_KEY=your-api-key
```

Make sure you have the python-dotenv package installed (it should be in requirements.txt). This will load the environment variables when you run your app.

### 6. Run the Script
Once the environment is set up and the dependencies are installed, you can run the project locally.

```bash
python3 test.py
```

### Follow me
- [LinkedIn](https://www.linkedin.com/in/benmukanirwa/)
- [X](https://x.com/benmukanirwa)
- [Read my stories](https://medium.com/@benmukanirwa)


