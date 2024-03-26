---
Student_name: Janeeta Wahid
Current: Current
School: GIHS
Student_year_level:
  - Year 12
Student_email: jwahid2006@gmail.com
Student_mobile: 61478583374
Parent_name: Rubana Munni
Parent_email: rubana82@yahoo.com
Parent_mobile: 61444509679
Monday: Currently available
Tuesday: Currently available
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: Currently available
SACE_or_IB: SACE
Subjects:
  - SACE 12CHEM
  - SACE 12METH
Subsidy: $30 per subject
---
Classes:: [[1.2 Classes/12CHEM B1.md|12CHEM B1]], [[1.2 Classes/12BIO A1.md|12BIO A1]], [[1.2 Classes/UCAT B.md|UCAT B]]

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
1. **Student details** - year level, school, subjects 
	- 
2. **Motivation** - why do you want tutoring?
	- 
3.  What do you want to do after you leave school?
	- 
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 
5. **Grades** - what grades are you currently on for each of these subjects?
	- 
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview questions
type command
action QuickAdd: Insert subsidy interview questions
```
## Subsidy
### Application email
Which course would you like to apply for? Select all that apply.: SACE Mathematical Methods, SACE Chemistry  
Why are you applying for the subsidy program?: First of all my father is the only income earner in the family while my mother can't work due to her family commitments. Also, my other sister Wania Wahid will start her lessons in 2 weeks' time at Altitutor and will do two subjects as well. This would mean the total for one week would be $240 dollars which will be very difficult to pay considering other expenses and payments that have to be considered for the family.
### Interview
1. **About** - tell me about yourself and your family
	- 
2. **Income** - what are all of the income sources for your family?
	- 
3.  **Expenses** - what are all the sources of expenses for your family?
	- 
4. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- 


# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```

[Click to message student](sms:61478583374)

Hi Janeeta Wahid, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- Class time, day, or subject not found
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



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

