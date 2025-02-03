from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory database
students: Dict[int, dict] = {}
student_id_counter = 1

class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.post("/students/")
def create_student(student: Student):
    global student_id_counter
    students[student_id_counter] = student.model_dump()
    students[student_id_counter]["id"] = student_id_counter  # Corrected line
    student_id_counter += 1
    return students[student_id_counter - 1]


@app.get("/students/{student_id}")
def read_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student.model_dump()  # Corrected line
    students[student_id]["id"] = student_id
    return students[student_id]

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student deleted successfully"}
