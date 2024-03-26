---
SACE_or_IB: SACE
Student_name: Dennis Lau
Current: Current
School: Cedar College
Student_year_level: Year 11
Student_email: dennislau113@gmail.com
Student_mobile: 61432605782
Parent_name: Virginia Wong
Parent_email: virginiawkwong@gmail.com
Parent_mobile: 61481781882
Monday: Currently available
Tuesday: I can make myself available
Wednesday: Currently available
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
Subjects:
  - SACE 11METH
---
Classes:: [[1.2 Classes/11METH A2.md|11METH A2]]
```button
name Insert student details
type line(100) template
action Student details template
```
> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Dennis Lau")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Dennis Lau")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Dennis Lau")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Dennis Lau")
> ```


## Trial session questions to ask
### 1. How did you hear about us?
- He's a Gripper
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: 11 Methods, English, PE, Physics, Biology
- 
### 3. **Motivation** - why do you want tutoring?
- Get smarter
- Struggling a little bit with Methods last year
	- Mostly tests, wasn't sure which formulas to use
### 4.  What do you want to do after you leave school?
- No idea
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Methods and maybe physics
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Methods: B-, C+
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Trig

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



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```





<%*
// Function to replace the current YAML frontmatter content
function replaceYAML(newContent, app) {
    // Get the current active file
    const file = app.workspace.getActiveFile();
    
    // Read the content of the file
    let content = app.vault.read(file);
    
    // Define a regular expression to find YAML frontmatter
    const yamlRegex = /^---\n[\s\S]*?\n---/gm;

    // Wait for the content to be read
    content.then(data => {
        // Replace the current YAML frontmatter with the new content
        const newData = data.replace(yamlRegex, `---\n${newContent}\n---`);

        // Write the updated content back to the file
        app.vault.modify(file, newData);
    });
}

// Function to translate subject codes to names and determine SACE_or_IB
function translateSubjectsAndDetermineType(subjectsStr) {
    const subjectMap = {
        "15069": "SACE 12SPEC",
        "8553": "SACE 12METH",
        "9931": "SACE 12PHYS",
        "9837": "SACE 12CHEM",
        "9880": "SACE 12BIO",
        "15208": "SACE 11SPEC",
        "15154": "SACE 11METH",
        "21135": "SACE 11PHYS",
        "20921": "SACE 11CHEM",
        "21177": "SACE 11BIO",
        "21187": "SACE English Lit",
        "21185": "SACE English",
        "8709": "UCAT",
        "21189": "Medicine interview course",
        "21179": "PreSACE Maths",
        "21181": "PreSACE Science",
        "21183": "PreSACE English",
        "24994": "IB MATH AA",
        "24996": "IB MATH AI",
        "25000": "IB PHYS",
        "24998": "IB CHEM",
        "25002": "IB BIO",
        "25004": "IB ENG",
        // Add all other mappings here
    };

    let saceOrIb = '';
    const translatedSubjects = subjectsStr.split(',').map(code => {
        const subjectName = subjectMap[code.trim()];
        if (!saceOrIb) {
            if (subjectName.startsWith("SACE")) saceOrIb = 'SACE';
            else if (subjectName.startsWith("IB")) saceOrIb = 'IB';
            else if (subjectName.startsWith("PreSACE")) saceOrIb = 'PreSACE';
            // UCAT and Medicine interview course will leave saceOrIb as blank
        }
        return `  - ${subjectName}`;
    }).join('\n');

    return { translatedSubjects, saceOrIb };
}

// Prompt the user to paste something
const userInput = await tp.system.prompt("Paste your text here:");

// Replace double spaces with line breaks in user input
let formattedInput = userInput.split("  ").join("\n");

// Check for Subjects field and format it if present
const subjectsRegex = /Subjects:\s*([0-9,]+)/;
const match = formattedInput.match(subjectsRegex);
let saceOrIbValue = '';
if (match) {
    const subjectsStr = match[1];
    const { translatedSubjects, saceOrIb } = translateSubjectsAndDetermineType(subjectsStr);
    formattedInput = formattedInput.replace(subjectsRegex, `Subjects:\n${translatedSubjects}`);
    saceOrIbValue = saceOrIb;
}

// Insert the SACE_or_IB field
formattedInput = `SACE_or_IB: ${saceOrIbValue}\n${formattedInput}`;

// Replace the YAML metadata with the user's input
replaceYAML(formattedInput, this.app);

// Get the current active file
const file = this.app.workspace.getActiveFile();

// Delete the script itself
deleteScript(this.app, file);
%>




