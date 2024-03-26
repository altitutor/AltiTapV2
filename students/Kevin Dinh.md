---
Subjects:
  - SACE 12BIO
SACE_or_IB: SACE
School: St Peters College
Student_name: Kevin
Current: Current
Student_email: dinhk9087@gmail.con
Student_mobile: "0404643459"
Student_year_level:
  - Year 12
---
Classes:: [[1.2 Classes/12BIO A2.md|12BIO A2]]

> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,this.file.name)
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,this.file.name)
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,this.file.name)
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,this.file.name)
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,this.file.name)
> 

# Trial session
> [!Info] Trial session guide
![[1.2.1 Trial sessions#General format]]
### 1. How did you hear about us?
- Minah Cho 
### 2. **Student details** - year level, school, subjects
- Year 12
- Industry 
- Design TL solutions
- Methods
- Bio
- Headstart
### 3. **Motivation** - why do you want tutoring?
- Year 12 - just wanna make sure to get the best grades
### 4.  What do you want to do after you leave school?
- Teaching or OT 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 12 Biology 
### 6. **Grades** - what grades are you currently on for each of these subjects?
- BIO - B+/A-
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Bio - DNA and Proteins

Other notes:
- Put Kevin and An in same class (if available together)

# Messages
```button
name Generate student message
type line (1000) template
action MESSAGE - class times student
```
```button
name Generate parent message
type line (1000) template
action MESSAGE - class times parent
```


[Click to message student](sms:0404643459)

Hi An, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 12BIO: Monday 4:15pm - 5:45pm (starting from Monday 11 March)

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,
Altitutor Admin