---
Current: Current
Student_name: Baljot
School: The Heights
SACE_or_IB: SACE
Subjects:
  - UCAT
  - UCAT
Student_year_level:
  - Year 12
Student_email: baljot1117@gmail.com
Student_mobile: "0423484131"
Parent_name: Amarjot Kaur
Parent_email: amarjot1183@gmail.com
Parent_mobile: "0415124383"
Sunday_AM: Currently available
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_PM: Definitely unavailable
---
Classes:: [[1.2 Classes/UCAT C.md|UCAT C]]

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
- Have friends from the Heights that go here 
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: UCAT
- 
### 3. **Motivation** - why do you want tutoring?
- 
### 4.  What do you want to do after you leave school?
- Medicine
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Do not know yet as there has barely been any assessments at school
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?


**Subsidy interview**
- Mum's a nurse while dad is a truck driver
- Has one other sibling
- Cannot afford to come every week if it is $60/week so suggested to half the tuition but she comes every week (this'll be in her best interest as coming fortnightly would not be effective for her)


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


[Click to message student](sms:0423484131)

Hi Baljot, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- UCAT Sunday AM 9:30, starting on Sunday, 24 March

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,
Samantha, Altitutor Admin