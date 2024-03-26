---
Current: Current
School: St Peters
SACE_or_IB: SACE
Subjects:
  - PreSACE Maths
Student_year_level:
  - Year 8
Student_email: oliviayychen@gmail.com
Student_mobile: "+61401768916"
Parent_name: Olivia Chen
Parent_email: oliviayychen@gmail.com
Parent_mobile: "+61401768916"
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Student_name: Ashton Tee
---

Classes:: [[1.2 Classes/8MATH C1.md|8MATH C1]]
```button
name Insert student details
type command
action Templater: Insert Templates/Student details template.md
```

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


## Trial session questions to ask
### 1. How did you hear about us?
- Just googling and stumbled upon our website 
### 2. **Student details** - year level, school, subjects
- Year level: 8
- Subjects: English, Maths, Science
- 
### 3. **Motivation** - why do you want tutoring?
- Better grades
### 4.  What do you want to do after you leave school?
- Not sure yet (still young)
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- English, Maths and Science
### 6. **Grades** - what grades are you currently on for each of these subjects?
- A/A+ for English
- B for Maths
- C for Science
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```


# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```

[Click to message student](sms:+61401768916)

Hi Ashton, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- PreMATH: 4:15 Wednesday, starting on Wednesday, 31 January

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,
Altitutor Admin



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

[Click to message parent](sms:+61401768916)

Hi Olivia, 

This message is just to confirm that Ashton and Marissa have registered to be a student with us at Altitutor. We have organised the following session times for them:

Ashton:
- PreMATH: 4:15 Wednesday, starting on Wednesday, 31 January

Marissa:
- 12BIO: 4:15pm Thursday, starting on Thursday, 1 February
- 11CHEM: 5:45pm Thursday, starting on Thursday, 1 February
- 11PHYS: 1:15pm Saturday, starting on Saturday, 3 February


Before undefined’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin

![[Year 8 Year-to-a-page Mathematics Program 2024.docx]]