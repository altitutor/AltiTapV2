---
Student_name: Elisha Moore
Current: Current
School: Roma Mitchell
Student_year_level:
  - Year 12
Student_email: elishamariana@gmail.com
Student_mobile: 61480194443
Parent_name: Lyall Moore
Parent_email: cooltoyemporium@hotmail.com
Parent_mobile: 61404288438
Monday: I can make myself available
Tuesday: I can make myself available
Wednesday: Currently available
Thursday: I can make myself available
Friday: I can make myself available
Saturday_AM: Currently available
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - UCAT
  - SACE 12CHEM
  - SACE 12CHEM
SACE_or_IB: SACE
Subsidy: $30
---
Classes:: [[1.2 Classes/UCAT A.md|UCAT A]], [[12CHEM B2|12CHEM B2]]
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
	- Subjects: UCAT
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
My dad, Lyall Moore has a concession card. I would like to reduced the fees. Thank you
I am a disabled pensioner so any subsidy would be helpful. Thanks Lyall Moore father of Elisha Moore

UCAT, Chemistry and Biology - Year 12 

### Interview
1. **About** - tell me about yourself and your family
	- Dad is a pensionner but wife is working
2. **Income** - what are all of the income sources for your family?
	- Small amount of pension - 140 a fortnight
	- Wife is on 1100 a week
1.  **Expenses** - what are all the sources of expenses for your family?
	- School tuition 
	- Three children in the house - tuition for Elisha and Tessa
	- Car registration
	- Mortgage - high interest rates
	- Building a house currently 
	- Insurance - RAA 

1. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	-  Three subjects 
	-  $30 per subject per week ($90 per week)



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