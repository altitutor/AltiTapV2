---
Time: 2:45
Subject: 11BIO
Day: 6.Saturday PM
---
Tutor:: [[1.3 Tutors/Yuhan Wang.md|Yuhan Wang]]


> [!Example] Students
> ```dataview
> LIST
> WHERE contains(file.outlinks, this.file.link)
> ```
```button
name Add a student to this class
type command
action Templater: Insert Templates/Add_Student_to_Class.md
```
```button
name Remove a student from this class
type command
action Templater: Insert Templates/Remove_student_from_class.md
```
