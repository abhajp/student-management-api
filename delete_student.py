from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "John", "age": 20},
    {"id": 2, "name": "Alice", "age": 21},
    {"id": 3, "name": "Bob", "age": 22}
]

@app.route('/delete-student/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students

    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({
                "message": "Student deleted successfully"
            }), 200

    return jsonify({
        "message": "Student not found"
    }), 404

if __name__ == '__main__':
    app.run(debug=True)