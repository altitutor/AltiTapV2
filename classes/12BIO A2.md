---
Day: 1.Monday
Subject: SACE 12BIO
Time: 4:15
---
Tutor:: [[Matthew Qin|Matthew Qin]]

> [!Example] Students
> ```dataview
> LIST
> WHERE contains(file.outlinks, this.file.link)
> ```

> [!warning]- Add or remove students
> Only use these buttons when making a new class, or for scheduling at the start of the year. To change a student's class log a PERMANENT CLASS CHANGE
> ```button
> name Add a student to this class
> type command
> action Templater: Insert Templates/Templater scripts - other/Add_Student_to_Class.md
> ```
> ```button
> name Remove a student from this class
> type command
> action Templater: Insert Templates/Templater scripts - other/Remove_student_from_class.md
> ```