---
Student_name: Skyla Hardie
Current: Current
School: Brighton Secondary
Student_year_level: Year 12
Student_email: hardie.skyla00@icloud.com
Student_mobile: 61407901247
Parent_name: Amie Dobie
Parent_email: amiedobie183@gmail.com
Parent_mobile: 61401342654
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
SACE_or_IB: SACE
Subjects:
  - SACE 12METH
  - SACE 12CHEM
---
Classes:: [[1.2 Classes/12METH B1.md|12METH B1]], [[1.2 Classes/12CHEM B1.md|12CHEM B1]]
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
- friend
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: Methods, Chem
- 
### 3. **Motivation** - why do you want tutoring?
- better grades
### 4.  What do you want to do after you leave school?
- midwifery
- atar 93
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- methods
- chem
### 6. **Grades** - what grades are you currently on for each of these subjects?
- methods A/B
- chem A/B
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- hasnt started yet

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

[Click to message student](sms:61407901247)

Hi Skyla Hardie, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 12METH: 5:45 Monday, starting on Monday, 29 January
- 12CHEM: 4:15 Monday, starting on Monday, 29 January
- 12CHEM: 4:15 Wednesday, starting on Wednesday, 31 January

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 28 January so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message student](sms:61407901247)

Hi Skyla Hardie, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- Class time, day, or subject not found
- Class time, day, or subject not found

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 21 January so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message student](sms:61407901247)

Hi Skyla Hardie, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 12CHEM: Wednesdays at 4.15pm - 5.45pm, starting 24th Jan
- 12METH: Wednesdays at 5.45pm - 7.15pm, starting 24th Jan

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. I forgot to mention during the trial session that Homework help on Sundays will recommence on the 4th of Feb

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,
Altitutor Admin



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

[Click to message parent](sms:61401342654)

Hi Amie Dobie, 

This message is just to confirm that your child Skyla Hardie has registered to be a student with us at Altitutor. We have organised the following session times for them:

- Class time, day, or subject not found
- Class time, day, or subject not found

Before Skyla Hardie’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Skyla Hardie to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 21 January before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin

[Click to message parent](sms:61401342654)

Hi Amie, 

This message is just to confirm that your child Skyla has registered to be a student with us at Altitutor. We have organised the following session times for them:

- 12CHEM: Wednesdays at 4.15pm - 5.45pm, starting 24th Jan
- 12METH: Wednesdays at 5.45pm - 7.15pm, starting 24th Jan

Before Skyla Hardie’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

I forgot to mention during the trial session that Homework help on Sundays will recommence on the 4th of Feb

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin

