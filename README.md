# English Station


## Sequence Diagrams
### Sequence diagram for Student Registration
```mermaid
sequenceDiagram
    actor Student
    participant App
    participant Admin
    participant DB
    
    Student->>App: Click Register()
    App-->>Student: Redirect to Form Register
    Student->>App: Fill Form('name','class','Group'...)
    Note over Student,App: Password not requested yet
    
    App->>App: Validate Data
    
    App->>Admin: Send Email to approve
    Admin->>DB: Check student info in database
    DB-->>Admin: Return student data
    
    alt Admin Validates == True
        Admin->>App: Generate Access Token
        App-->>Student: Send Access Token
        Student->>App: Create password
        App->>App: Validate password
        App->>DB: Insert New Student in DB
        DB-->>App: Confirmation
        App-->>Student: Registration successful
    else Admin Rejects
        App-->>Student: Registration not allowed
    end
```

### Sequence diagram Login Student

```mermaid
sequenceDiagram
    actor Student
    participant App
    participant DB

    Student->>App:Login()
    App->>DB:Check if student in database (Student)
    alt Student in DATABASE
        DB->>App: Student exits count(1)
        App->>Student:redirect to home_page()
    else Student not in DATABASE
        DB-->>App:Student does not exists
        App-->>Student:email or Password incorrect. please try again with correct creadentials
    end
```

### Sequence diagram Admin create class Group like (1st)
we have 3 years in the heigh school 1st year, 2nd year and 3rd year 
for each year we have a speciality like luangues, scientific, mathematics, technique mathematics and so on 

### Sequence diagram admin create cours 

### Sequence diagram admin create chapter

### Sequence diagram admin affect cour to chapter

### Sequence diagram admin affect cours to class


## Class diagram

# Class Diagram

```mermaid
classDiagram
    class User {
        #userId: int
        #email: string
        #password: string
        #name: string
        #createdAt: date
        +login()
        +logout()
        +updateProfile()
    }

    class Student {
        +studentId: int
        +specialityId: int
        +accessToken: string
        +viewCourses()
        +takExam()
        +downloadCourse()
        +submitAssignment()
    }

    class Admin {
        +adminId: int
        +approvPermissions: boolean
        +approvStudent()
        +rejectStudent()
        +addCourse()
        +addExam()
        +deleteStudent()
        +viewAllStudents()
    }

    class AcademicLevel {
        <<enumeration>>
        FIRST_YEAR
        SECOND_YEAR
        THIRD_YEAR
    }

    class Speciality {
        +specialityId: int
        +name: string
        +description: string
        +level: AcademicLevel
        +addCourse()
        +getStudents()
        +getCourses()
    }

    class Course {
        +courseId: int
        +title: string
        +description: string
        +specialityId: int
        +createdBy: int
        +format: string
        +addSection()
        +addMaterial()
    }

    class Section {
        +sectionId: int
        +courseId: int
        +title: string
        +order: int
        +addMaterial()
    }

    class Material {
        +materialId: int
        +sectionId: int
        +type: string
        +content: file
        +uploadedDate: date
    }

    class Exam {
        +examId: int
        +courseId: int
        +title: string
        +passingScore: int
        +duration: int
        +createQuestion()
        +evaluateExam()
    }

    class Question {
        +questionId: int
        +examId: int
        +text: string
        +options: string[]
        +correctAnswer: string
        +difficulty: string
    }



    User <|-- Student
    User <|-- Admin
    
    Speciality "1" -- "0..*" Student : enrolls
    Speciality "1" -- "0..*" Course : contains
    AcademicLevel "1" -- "0..*" Speciality : has
    
    Course "1" -- "0..*" Section : contains
    Section "1" -- "0..*" Material : has
    
    Course "1" -- "0..*" Exam : has
    Exam "1" -- "0..*" Question : contains
    
    Admin "1" -- "0..*" Course : creates
    Admin "1" -- "0..*" Exam : creates
    
    Student "0..*" -- "0..*" Course : takes


    
```