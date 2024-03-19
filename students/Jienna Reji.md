---
Student_name: Jienna Reji
Current: Current
School: Adelaide high school
Student_year_level: Year 12
Student_email: jienna.reji@gmail.com
Student_mobile: 61404671106
Parent_name: Reji Joseph
Parent_email: rejij23@gmail.com
Parent_mobile: 61411096330
Monday: Currently available
Tuesday: Currently available
Wednesday: I can make myself available
Thursday: Currently available
Friday: I can make myself available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
SACE_or_IB: SACE
Subjects:
  - SACE 12CHEM
  - SACE 12CHEM
---
Classes:: [[12METH B1|12METH B1]], [[12CHEM B1|12CHEM B1]]

> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Jienna Reji")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Jienna Reji")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Jienna Reji")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Jienna Reji")
> ```


## Trial session questions to ask
### 1. How did you hear about us?
- Brother used to go here (back when Altitutor was at uni hub)
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: 12METH 12CHEM
- French, English General 
### 3. **Motivation** - why do you want tutoring?
- Get knowledge up, get general help
### 4.  What do you want to do after you leave school?
- Health-related 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 12METH, 12CHEM 
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Chemistry - A
- Methods - A 
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Not sure yet 
- Chemistry - Topic 1 - Monitoring the Environment 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview questions
type command
action QuickAdd: Insert subsidy interview questions
```




# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```

[Click to message student](sms:61404671106)

Hi Jienna Reji

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 12CHEM: 4:15 Monday, starting on Monday, 5 February

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 4 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards

Altitutor Admin



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

[Click to message parent](sms:61411096330)

Hi Reji Joseph

This message is just to confirm that your child Jienna Reji has registered to be a student with us at Altitutor. We have organised the following session times for them:

- 12CHEM: 4:15 Monday, starting on Monday, 5 February

Before Jienna Reji’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Jienna Reji to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 4 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards 
Altitutor Admin