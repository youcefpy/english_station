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

### Sequence diagram Admin create class


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
        +login()
    }

    class Student {
        +studentId: int
        +class: string
        +viewCourses()
    }

    class Admin {
        +adminId: int
        +approvStudent()
    }

    User <|-- Student
    User <|-- Admin
```