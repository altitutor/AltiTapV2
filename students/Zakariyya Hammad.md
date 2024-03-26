---
Current: Current
School: Adelaide High School
SACE_or_IB: SACE
Subjects:
  - SACE 12METH
  - SACE 12PHYS
Student_year_level:
  - Year 12
Student_email: zakariyya.hammad@gmail.com
Student_mobile: "+61416824600"
Parent_name: Rana Muhammad Hammad Akhter
Parent_email: ranahammad@yahoo.com
Parent_mobile: "+61455153370"
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Currently available
Student_name: Zakariyya Hammad
---
Classes:: 

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
> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]
### 1. How did you hear about us?
- He knows one of the students here (Hari) through school
### 2. **Student details** - year level, school, subjects
- Year 12
- English literature, methods, physics, biology
### 3. **Motivation** - why do you want tutoring?
- Get ahead of class; extra help
### 4.  What do you want to do after you leave school?
- Computer science 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Methods
- Physics
- English literature (drafting ocassionally)
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Bs for all subjects 
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Methods - knowledge test (haven't started)
- Biology (topic 2.2)
- Physics (topic 1 - projectile motion)
- English literature - persuasive text 

# Subsidy interview
```button
name Insert subsidy interview
type command
action QuickAdd: Insert subsidy interview questions
```

# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```
Hi Zakariyya

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

12PHYS: Mondays at 5:45pm (starting 12 February)
12METH: Saturdays at 9:30am (starting 17 February )

Before your first session, please do the following things:

Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
Download our app by searching "Altitutor" in the app store / play store
Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842).

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards
Samantha
```button
name Generate parent message
type append template
action MESSAGE - new parent message
```
