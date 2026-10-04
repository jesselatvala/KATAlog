 # KATAlog
HY TKT20019 project

## Target Functionalities

- User (karateka) can register and log in to app.
- User can add, edit and remove Katas (Karate movement sequences).
- Katas consist of karate techniques and stances that can be added by the user
- User can add additional info to Kata (rank, founder, style, links to other katas).
- User can view and search all Katas added to app.
- The app displays statistics for each karateka, as well as the katas added by the karateka.
- User can add Bunkai (practical application) to the Kata

## Working Functionalities
- User can register and log in to app.
- User can add katas with /new_kata (name length max 50 characters, describtion length max 500 characters)

## How to Use
- Clone the repository to your local machine by running:
git clone https://github.com/jesselatvala/KATAlog.git
- Navigate to the project's root directory by running:
cd KATAlog
- Create and activate a virtual environment by running:
python3 -m venv venv
source venv/bin/activate
- Install the dependencies:
pip install flask
- Initialize the database by running:
sqlite3 database.db < schema.sql
- Start the application by running:
flask run
- Open your browser and go to http://127.0.0.1:5000/ to view the application's user interface.