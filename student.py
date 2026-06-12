from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "James",
        "age": 20,
        "college": "ABC College",
        "branch": "Computer Science"
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 21,
        "college": "XYZ College",
        "branch": "Information Technology"
    },
    {
        "id": 3,
        "name": "Akhil",
        "age": 19,
        "college": "Government College",
        "branch": "Mechanical Engineering"
    },
    {
        "id": 4,
        "name": "Anjali",
        "age": 20,
        "college": "National College",
        "branch": "Electronics"
    },
    {
        "id": 5,
        "name": "Neha",
        "age": 22,
        "college": "Engineering College",
        "branch": "Civil Engineering"
    }
]

@app.route('/students')
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)