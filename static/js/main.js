document.addEventListener("DOMContentLoaded", function() {
    let semesterCount = 1;
    document.getElementById('add_semester').addEventListener('click', function() {
        semesterCount++;
        let semesterDiv = document.createElement('div');
        semesterDiv.className = "semester";
        semesterDiv.id = `semester${semesterCount}`;
        semesterDiv.innerHTML = `
            <h2>Semester ${semesterCount}</h2>
            <div class="mb-3">
                <label for="subject${semesterCount}" class="form-label">Subject Name</label>
                <input type="text" class="form-control" id="subject${semesterCount}" name="subject_name_${semesterCount}" required>
            </div>
            <div class="mb-3">
                <label for="marks_obtained${semesterCount}" class="form-label">Marks Obtained</label>
                <input type="number" class="form-control" id="marks_obtained${semesterCount}" name="marks_obtained_${semesterCount}" required>
            </div>
            <div class="mb-3">
                <label for="max_marks${semesterCount}" class="form-label">Maximum Marks</label>
                <input type="number" class="form-control" id="max_marks${semesterCount}" name="max_marks_${semesterCount}" required>
            </div>
        `;
        document.getElementById('semesters').appendChild(semesterDiv);
    });
});
