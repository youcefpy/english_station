# English Station

---
## Sequence Diagrams
### Sequence diagram for Student Registration
```mermaid
sequenceDiagram
    actor Student
    participant App
    actor Admin
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
---
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
---
### Sequence diagram Admin create academicLevel Group like (1st, 2nd, 3rd)
```mermaid
sequenceDiagram
    actor Admin
    participant App
    participant DB

    Admin->>App:Create AcadimicLevel()
    App->>Admin:FormAcadimicLevel()
    Admin->>App:Fill form()
    App->>App:validate data
    App->>DB:Save()
```
---
### Sequence diagram admin create streams (Scientific, Leterary, Mathematic, Technical math)
```mermaid
sequenceDiagram
    actor Admin
    participant App
    participant DB

    Admin->>App:Create CreateSteam()
    App->>Admin:FormStream()
    Admin->>App:Fill form()
    App->>App:validate data
    App->>DB:Save()
```


---
### Sequence diagram Create Unit
```mermaid
sequenceDiagram
    actor Admin
    participant App
    participant DB

    Admin->>App:Create CreateUnit()
    App->>Admin:FormUnit()
    Admin->>App:Fill form()
    App->>App:validate data
    App->>DB:Save()
```
---
### Sequence diagram admin create cours
```mermaid
sequenceDiagram
    actor Admin
    participant App
    participant DB
    
    Admin->>App:Create CreateCours()
    App->>Admin:FormCours()
    Admin->>App:Fill form()
    App->>App:validate data
    App->>DB:Save()
```
---
### Sequence diagram admin affect cours to Unit
```mermaid
sequenceDiagram
    actor Admin
    participant App
    participant DB

    Admin->>App:AffectCourseToUnit()
    App->>DB:Save()
```

---
### Sequence diagram admin affect Unit to AcadimicLevel
```mermaid
sequenceDiagram
    actor Admin
    participant App
    participant DB

    Admin->>App:AffectUnitToAcadimicLevel()
    App->>DB:Save()
```

---
# Class diagram

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
        +streamId: int
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

    class Stream {
        +streamId: int
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
        +streamId: int
        +createdBy: int
        +format: string
    }

    class AcademicLevelStream{
        +idAcadimicLevel: int
        +idStream: int
        +idStudent: int
    }


    class Unit{
        +idUnit: int
        +name: string
        +description: string
        +stream: Stream
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
    
    Unit "1" -- "1..*" Course : contains
    AcademicLevel "1" -- "1..*" Stream : has
    
    Course "1" -- "1..*" Exam : has
    Exam "1" -- "1..*" Question : contains
    
    Admin "1" -- "1..*" Course : creates
    Admin "1" -- "1..*" Exam : creates
    
    Student "1..*" -- "1..*" Course : takes

    Stream "1" -- "1..*" Unit : contains

    Stream -- AcademicLevelStream
    AcademicLevel -- AcademicLevelStream
    AcademicLevelStream "1" -- "1..*" Student: contains

```