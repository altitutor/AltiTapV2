---
SACE_or_IB: SACE
Student_name: Alannah Vu
Current: Current
School: Glenunga school
Student_year_level: Year 11
Student_email: phuongquedo@gmail.com
Student_mobile: 61412815187
Parent_name: Fiona Vu
Parent_email: phuongquedo@gmail.com
Parent_mobile: 61412815187
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - UCAT
---
Classes:: [[1.2 Classes/UCAT C.md|UCAT C]]
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
> where icontains(file.name,"Alannah Vu")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Alannah Vu")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Alannah Vu")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Alannah Vu")
> ```


## Trial session questions to ask
1. **Student details** - year level, school, subjects 
	- Year level: 10
	- Subjects: 11CHEM
	- 
- 
1. **Motivation** - why do you want tutoring?
	- 
2.  What do you want to do after you leave school?
	- 
3. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 
4. **Grades** - what grades are you currently on for each of these subjects?
	- 
5.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- 

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
type line (1000) template
action MESSAGE - class times student
```



```button
name Generate parent message
type line (1000) template
action MESSAGE - class times parent
```


[Click to message student](sms:undefined)

Hi Alannah, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- UCAT: Sundays at 9.30am - 12.30pm, starting 3 March

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,
Altitutor Admin