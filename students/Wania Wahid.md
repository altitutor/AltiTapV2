---
Student_name: Wania Wahid
Current: Current
School: Glenunga
Student_year_level:
  - Year 11
Student_email: wania.wahid84891@gmail.com
Student_mobile: 61483860810
Parent_name: Wahid Murad
Parent_email: mwmurad@gmail.com
Parent_mobile: 61469198052
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: I can make myself available
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: I can make myself available
Sunday_PM: Currently available
Subsidy: $30 per session
SACE_or_IB: SACE
Subjects:
  - SACE 11METH
---
Classes:: [[1.2 Classes/11CHEM A1.md|11CHEM A1]], [[1.2 Classes/11METH B2.md|11METH B2]], [[1.2 Classes/UCAT A.md|UCAT A]]
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

## Trial session
1.  **Motivation** - why do you want tutoring?
	- Year 10 student, PreSACE Maths 
	- Can improve on grades - A+ overall for PreSACE Maths 
	- Put Janeeta and Wania on the same day 
1.  **Topic** - which topic are you up to for each subject?
	- Quadratics (just started)
2. **Grades** - what grades are you currently on for each subject?
	- PreSACE Maths - A-/B+

## Subsidy
### Application email
Which course would you like to apply for? Select all that apply.: SACE Mathematical Methods, SACE Chemistry  
Why are you applying for the subsidy program?: First of all my father is the only income earner in the family while my mother can't work due to her family commitments. Also, my other sister Wania Wahid will start her lessons in 2 weeks' time at Altitutor and will do two subjects as well. This would mean the total for one week would be $240 dollars which will be very difficult to pay considering other expenses and payments that have to be considered for the family.
### Interview
1. **About** - tell me about yourself and your family
	- Moved from Bangledesh, to malaysia in '97
	- Kids born in malaysia
	- Moved to aus in 2010
	- Father: business stats and economics lecturer at uniSA
	- Mother: works as a housewife
1. **Income** - what are all of the income sources for your family?
	- Only father's job
2.  **Expenses** - what are all the sources of expenses for your family?
	- Mortgage 3.5k monthly
	- Living expenses
	- Sometimes relatives in home country want support
3. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- $20 = $30 per session for both Wanita and Janeeta


> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Wania Wahid")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Wania Wahid")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Wania Wahid")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Wania Wahid")
> ```


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



# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

