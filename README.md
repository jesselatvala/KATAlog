 # KATAlog
HY TKT20019 project

## Functionalities

- User (karateka) can register and log in to app.
- User can add, edit and remove Katas (Karate movement sequences. Name length max 50 characters, description length max 500 characters).
- Katas consist of karate techniques and stances that can be added by the user
- User can add additional info to Kata (developer, style)
- User can view and search all Katas added to app.
- The app displays statistics of users, katas, developers and styles

## How to Use
- Clone the repository to your local machine by running:
git clone https://github.com/jesselatvala/KATAlog.git
- Navigate to the project's root directory by running:
cd KATAlog
- Create and activate a virtual environment by running first:
python3 -m venv venv
- Then: source venv/bin/activate
- Install the dependencies:
pip install flask
- Initialize the database by running:
sqlite3 database.db < schema.sql
- Start the application by running:
flask run
- Open your browser and go to http://127.0.0.1:5000/ to view the application's user interface.