---
Student_name: Fadwa Osman
Current: Current
School: Islamic College, SA
Student_year_level:
  - Year 11
Student_email: fadwaosman227@gmail.com
Student_mobile: 61468343395
Parent_name: Idris Osman
Parent_email: abofaris.sat@gmail.com
Parent_mobile: 61413656882
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: I can make myself available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
SACE_or_IB: SACE
Subjects:
  - SACE 11CHEM
  - SACE 11METH
Subsidy: $25/session
---
Classes:: 
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
	- Year level: 11
	- Subjects: chem, methods
	- 
2. **Motivation** - why do you want tutoring?
	- 
3.  What do you want to do after you leave school?
	- vet science
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 
5. **Grades** - what grades are you currently on for each of these subjects?
	- As and Bs
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- starting year 11 in term 4
	- Starting the following year content in term 4 so need to be in a class by himself 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview questions
type command
action QuickAdd: Insert subsidy interview questions
```

## Subsidy
### Application email
I am applying for the subsidy program on behalf of both my sister and I (Wahaj). Our dad is a full time uni student and so our income is limited however we would still like receive tutoring at an affordable price, hence why we’re applying for the subsidised cost.

### Interview
1. **About** - tell me about yourself and your family
	- Dad - full time uni student
			- Has a satellite business but not much clients 
	- Mum - unemployed 
	- Seven siblings - all of them are school students (youngest sibling is 9; parents have to pay tuition for most siblings) 
	- Goes to Australian Islamic college - all siblings go to this school 
	- Dad is looking for job and can pay full rate once the family is stable
1. **Income** - what are all of the income sources for your family?
	- Dad's satellite company 
	- Centrelink payments
1.  **Expenses** - what are all the sources of expenses for your family?
	- School tuition 
	- Rent/mortgage 
	- Everyday necessities - food, water, bills, etc. 
1. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- Fadwa is thinking of dropping Chemistry and just do Methods 
		--> Wahaj - 12CHEM 
		--> Fadwa - 11CHEM 

$25.00 per subject so $50.00/week 
$25.00 per 1.5 hours* 

Fadwa - has gone to 1
Wahaj has gone to 2


