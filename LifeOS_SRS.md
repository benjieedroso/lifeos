# LifeOS — Software Requirements Specification (SRS)

**Document Version:** 1.0  
**Status:** Draft  
**Application Type:** Personal Life Management Web Application  
**Primary Users:** Individual users  
**Target Platform:** Web  
**Technology Direction:** Django Full-Stack + PostgreSQL  
**Frontend:** Django Templates + Bootstrap  
**API:** Not required for the initial system

---

# 1. Introduction

## 1.1 Purpose

LifeOS is a personal life-management web application designed to help individuals organize and manage different aspects of their daily lives from one centralized system.

The application will allow users to manage:

- Tasks
- Goals
- Habits
- Routines
- Notes
- Calendar events
- Reminders
- Projects
- Personal documents
- Notifications
- Personal settings
- Activity history

The system should provide a single place where a user can understand **what they need to do, what they are working toward, and how they are progressing**.

# 2. Product Vision

LifeOS should answer three questions for the user:

### What do I need to do?

Tasks, routines, calendar events, and reminders.

### What am I trying to accomplish?

Goals and projects.

### How am I doing?

Habit tracking, progress tracking, statistics, and dashboards.

The core relationship is:

**Goals → Projects → Tasks → Completion**

while:

**Habits → Routines → Daily consistency**

# 3. Goals and Objectives

LifeOS shall:

1. Provide users with a centralized personal management system.
2. Allow users to organize daily tasks.
3. Allow users to establish and track personal goals.
4. Allow users to track habits.
5. Allow users to create routines.
6. Allow users to manage notes and personal information.
7. Allow users to schedule events.
8. Provide reminders and notifications.
9. Provide useful dashboards and statistics.
10. Allow users to upload personal documents.
11. Protect personal user data.
12. Provide search and filtering across personal information.
13. Maintain an activity history.
14. Provide reliable backups and recovery mechanisms.
15. Be usable on desktop and mobile browsers.

# 4. User Types

## 4.1 Registered User

The primary user of LifeOS.

A registered user can manage their own:

- Tasks
- Goals
- Habits
- Routines
- Projects
- Notes
- Events
- Documents
- Settings
- Notifications

## 4.2 System Administrator

A technical administrator responsible for operating the application.

The administrator can:

- Manage users
- Monitor system activity
- Review system logs
- Manage system configuration
- Investigate errors
- Manage backups

The administrator should not automatically have unrestricted access to private user content unless the application's privacy policy explicitly permits it.

# 5. Functional Requirements

## 5.1 Authentication

LifeOS shall provide account authentication.

### Features

- Registration
- Login
- Logout
- Password reset
- Password change
- Email verification
- User profile
- Session management
- Account deactivation
- Account deletion

### User Stories

**US-AUTH-01**

> As a visitor, I want to register an account so that I can use LifeOS. - done

**US-AUTH-02**

> As a registered user, I want to log in so that I can access my personal information. - done

**US-AUTH-03**

> As a user, I want to log out so that my account remains protected when I finish using LifeOS. - done

**US-AUTH-04**

> As a user, I want to reset my password if I forget it. - done

**US-AUTH-05**

> As a user, I want to change my password so that I can maintain account security. - done

**US-AUTH-06**

> As a user, I want to verify my email address so that LifeOS can confirm ownership of my account. - done

**US-AUTH-07**

> As a user, I want to deactivate or delete my account if I no longer want to use LifeOS. - done

---

## 5.2 Authorization

Because LifeOS is primarily personal, the main authorization requirement is **data ownership**.

### Requirements

Users shall only be able to access their own private data.

For example:

- User A cannot view User B's tasks.
- User A cannot edit User B's goals.
- User A cannot delete User B's documents.
- User A cannot access User B's notes.

### User Stories

**US-AUTHZ-01**

> As a user, I want my personal information to remain private from other users. - done

**US-AUTHZ-02**

> As a user, I want LifeOS to prevent unauthorized users from accessing my records. - done

**US-AUTHZ-03**

> As an administrator, I want administrative permissions separated from normal user permissions.

### Future Requirement

LifeOS may eventually support:

- Shared tasks
- Shared projects
- Family accounts
- Accountability partners

These should use explicit permissions rather than automatically exposing personal data.

---

## 5.3 Dashboard

The dashboard shall provide an overview of the user's current life-management information.

### Dashboard Components

- Today's tasks
- Overdue tasks
- Upcoming events
- Habit progress
- Active goals
- Project progress
- Upcoming reminders
- Recent notes
- Recent activity
- Daily/weekly statistics

### User Stories

**US-DASH-01**

> As a user, I want to see my most important information immediately after logging in. - done

**US-DASH-02**

> As a user, I want to see what I need to accomplish today.

**US-DASH-03**

> As a user, I want to see my upcoming deadlines.

**US-DASH-04**

> As a user, I want to see my progress toward my goals.

---

## 5.4 Task Management

Tasks are one of LifeOS's core features.

### Task Attributes

A task may contain:

- Title
- Description
- Status
- Priority
- Due date
- Start date
- Category
- Project
- Goal
- Tags
- Attachments
- Reminder
- Created date
- Updated date
- Completed date

### Task Statuses

- Not Started
- In Progress
- Completed
- Cancelled

### Features

- Create task
- View task
- Edit task
- Delete task
- Complete task
- Reopen task
- Assign priority
- Set due date
- Add tags
- Attach task to project
- Attach task to goal
- Add reminders

### User Stories

**US-TASK-01**

> As a user, I want to create a task so that I can remember something I need to accomplish.

**US-TASK-02**

> As a user, I want to mark a task as completed when I finish it.

**US-TASK-03**

> As a user, I want to assign a due date so that I know when a task needs to be completed.

**US-TASK-04**

> As a user, I want to prioritize tasks so that I know what requires my attention first.

**US-TASK-05**

> As a user, I want to edit a task if its information changes.

**US-TASK-06**

> As a user, I want to delete tasks that I no longer need.

---

## 5.5 Goals

Goals represent things the user wants to accomplish over a period of time.

Examples:

- Save ₱100,000
- Learn Django
- Exercise regularly
- Buy a car
- Read 20 books

### Goal Attributes

- Name
- Description
- Category
- Status
- Target date
- Progress
- Measurement type
- Target value
- Current value
- Tasks
- Projects
- Milestones

### Goal Status

- Not Started
- Active
- Completed
- Paused
- Cancelled

### User Stories

**US-GOAL-01**

> As a user, I want to create a goal so that I can define something I want to accomplish.

**US-GOAL-02**

> As a user, I want to set a target date so that I have a deadline.

**US-GOAL-03**

> As a user, I want to track my progress toward a goal.

**US-GOAL-04**

> As a user, I want to divide a large goal into smaller milestones.

**US-GOAL-05**

> As a user, I want to connect tasks and projects to my goal.

---

## 5.6 Habit Tracking

Users shall be able to create and track recurring habits.

Examples:

- Exercise
- Read
- Drink water
- Study
- Journal
- Sleep before 11 PM

### Features

- Create habit
- Edit habit
- Delete habit
- Daily tracking
- Weekly tracking
- Completion history
- Streak tracking
- Completion percentage
- Habit statistics

### User Stories

**US-HABIT-01**

> As a user, I want to create a habit so that I can develop consistent behavior.

**US-HABIT-02**

> As a user, I want to mark a habit as completed each day.

**US-HABIT-03**

> As a user, I want to see my habit streak.

**US-HABIT-04**

> As a user, I want to see my historical habit performance.

**US-HABIT-05**

> As a user, I want to edit or remove a habit.

---

## 5.7 Routines

Routines group recurring activities into structured periods.

Examples:

### Morning Routine

- Wake up
- Drink water
- Exercise
- Shower
- Breakfast
- Prepare for work

### Night Routine

- Prepare clothes
- Review tomorrow
- Journal
- Read
- Sleep

### User Stories

**US-ROUTINE-01**

> As a user, I want to create a routine so that I can structure recurring activities.

**US-ROUTINE-02**

> As a user, I want to define the steps in a routine.

**US-ROUTINE-03**

> As a user, I want to track whether I completed my routine.

**US-ROUTINE-04**

> As a user, I want to schedule routines for specific days or times.

---

## 5.8 Calendar & Events

LifeOS shall provide personal scheduling.

### Event Features

- Create event
- Edit event
- Delete event
- Event title
- Description
- Start time
- End time
- Location
- Recurrence
- Reminder
- Category

### User Stories

**US-CAL-01**

> As a user, I want to create an event so that I can remember appointments and activities.

**US-CAL-02**

> As a user, I want to see my upcoming events.

**US-CAL-03**

> As a user, I want to receive reminders before important events.

**US-CAL-04**

> As a user, I want recurring events for activities that happen regularly.

---

## 5.9 Projects

Projects group related tasks toward a larger outcome.

Example:

**Project:** Build Django Portfolio

- Learn Django
- Build application
- Write tests
- Dockerize
- Deploy

### User Stories

**US-PROJ-01**

> As a user, I want to create projects so that I can organize related tasks.

**US-PROJ-02**

> As a user, I want to track project progress.

**US-PROJ-03**

> As a user, I want to associate tasks with projects.

**US-PROJ-04**

> As a user, I want to mark projects as completed.

---

## 5.10 Notes

LifeOS shall provide personal note-taking.

### Features

- Create notes
- View notes
- Edit notes
- Delete notes
- Search notes
- Categories
- Tags
- Pin important notes
- Archive notes
- Attach files

### User Stories

**US-NOTE-01**

> As a user, I want to create notes so that I can store information I want to remember.

**US-NOTE-02**

> As a user, I want to organize notes using categories and tags.

**US-NOTE-03**

> As a user, I want to search my notes.

**US-NOTE-04**

> As a user, I want to archive notes that I no longer actively use.

---

## 5.11 Reminders

The system shall allow users to create reminders.

### Reminder Types

- Task reminder
- Event reminder
- Goal reminder
- Habit reminder
- Custom reminder

### User Stories

**US-REM-01**

> As a user, I want to create reminders so that I don't forget important activities.

**US-REM-02**

> As a user, I want to choose when I receive a reminder.

**US-REM-03**

> As a user, I want to dismiss reminders after seeing them.

---

## 5.12 Search, Filtering, Sorting & Pagination

Search shall be available across major data types.

### Search

Users should be able to search:

- Tasks
- Notes
- Goals
- Projects
- Habits
- Documents
- Events

### Filtering

Examples:

- Task status
- Priority
- Category
- Date
- Goal
- Project
- Completion status

### Sorting

Users should be able to sort by:

- Date
- Name
- Priority
- Status
- Recently updated

### Pagination

Large lists shall use pagination.

### User Stories

**US-SEARCH-01**

> As a user, I want to search my records so that I can quickly find information.

**US-SEARCH-02**

> As a user, I want to filter my tasks so that I can focus on relevant items.

**US-SEARCH-03**

> As a user, I want to sort records so that I can view them in the order I need.

**US-SEARCH-04**

> As a user, I want large lists divided into pages so that they remain easy to navigate.

---

## 5.13 Files & Documents

Users shall be able to store personal documents.

Examples:

- IDs
- Certificates
- Receipts
- Personal documents
- Work documents
- School documents

### Features

- Upload
- View
- Download
- Delete
- Rename
- Categorize
- Search
- Attach to records

### User Stories

**US-FILE-01**

> As a user, I want to upload personal documents so that I can keep them organized.

**US-FILE-02**

> As a user, I want to download my documents when I need them.

**US-FILE-03**

> As a user, I want documents protected from unauthorized users.

**US-FILE-04**

> As a user, I want to organize documents into categories.

---

## 5.14 Notifications

LifeOS shall provide notifications.

### Notification Types

- Task due
- Task overdue
- Event reminder
- Habit reminder
- Goal milestone
- System notification
- Account notification

### User Stories

**US-NOTIF-01**

> As a user, I want to receive notifications about important upcoming activities.

**US-NOTIF-02**

> As a user, I want to mark notifications as read.

**US-NOTIF-03**

> As a user, I want to control which notifications I receive.

---

## 5.15 Email Communication

The system may send:

- Email verification
- Password reset
- Reminder emails
- Important notifications
- Account notifications

### User Stories

**US-EMAIL-01**

> As a user, I want to receive an email when I need to verify my account.

**US-EMAIL-02**

> As a user, I want to receive password-reset instructions by email.

**US-EMAIL-03**

> As a user, I want to control optional email notifications.

---

## 5.16 Personal Statistics

LifeOS shall provide statistics about the user's activity.

### Tasks

- Completed today
- Completed this week
- Completion rate
- Overdue tasks

### Habits

- Current streak
- Longest streak
- Completion percentage

### Goals

- Active goals
- Completed goals
- Progress

### Projects

- Active projects
- Completed projects
- Project progress

### User Story

**US-STATS-01**

> As a user, I want to see statistics about my activities so that I can understand my progress over time.

---

## 5.17 Settings

Users shall be able to configure their account.

### Settings

- Profile
- Password
- Email
- Timezone
- Language
- Date format
- Time format
- Theme
- Notification preferences
- Email preferences
- Privacy settings

### User Stories

**US-SET-01**

> As a user, I want to configure my personal preferences.

**US-SET-02**

> As a user, I want to choose my timezone so that dates and reminders are correct.

**US-SET-03**

> As a user, I want to control my notification preferences.

---

## 5.18 Activity & Audit History

The system shall record important actions.

Examples:

- Created task
- Completed task
- Edited goal
- Deleted note
- Uploaded document
- Changed account settings
- Logged in
- Changed password

### User Stories

**US-AUDIT-01**

> As a user, I want to see important activity on my account so that I know what changes have occurred.

**US-AUDIT-02**

> As an administrator, I want system activity recorded so that security and operational issues can be investigated.

---

## 5.19 Administration

The system administrator shall have an administrative interface.

### Features

- User management
- User account status
- System configuration
- Category management
- System logs
- Error monitoring
- Backup management
- Administrative audit logs

### User Stories

**US-ADMIN-01**

> As an administrator, I want to view registered users so that I can manage the application.

**US-ADMIN-02**

> As an administrator, I want to deactivate problematic accounts.

**US-ADMIN-03**

> As an administrator, I want to monitor system errors.

**US-ADMIN-04**

> As an administrator, I want to review audit information when investigating problems.

---

## 5.20 Business Logic

Although LifeOS isn't a business application, it still has substantial application logic.

### Task Logic

- Determine overdue tasks
- Determine completion
- Calculate task statistics

### Goal Logic

- Calculate progress
- Determine milestones
- Determine completion

### Habit Logic

- Calculate streaks
- Calculate completion rates
- Determine missed days

### Routine Logic

- Determine completion
- Track recurring routines

### Reminder Logic

- Determine when reminders should trigger

### User Stories

**US-LOGIC-01**

> As a user, I want LifeOS to automatically calculate my progress.

**US-LOGIC-02**

> As a user, I want LifeOS to identify overdue tasks automatically.

**US-LOGIC-03**

> As a user, I want LifeOS to calculate my habit streak automatically.

---

## 5.21 Data Validation

The system shall validate all user input.

Examples:

- Required fields
- Valid dates
- Valid email addresses
- Valid file types
- Valid file sizes
- Valid numerical values
- Duplicate prevention where appropriate

### User Story

**US-VALID-01**

> As a user, I want the system to tell me when information I entered is invalid so that I can correct it.

---

## 5.22 Security

Security shall be considered throughout the application.

Requirements include:

- Password hashing
- Authentication
- Authorization
- CSRF protection
- XSS protection
- SQL injection protection
- Secure session management
- Secure cookies
- HTTPS
- Secure file uploads
- Input validation
- Rate limiting where appropriate
- Protection against unauthorized object access
- Secure secret management

### User Stories

**US-SEC-01**

> As a user, I want my personal information protected from unauthorized access.

**US-SEC-02**

> As a user, I want my password stored securely.

**US-SEC-03**

> As a user, I want only authorized requests to modify my data.

---

## 5.23 Error Handling

The system shall provide appropriate behavior when errors occur.

Examples:

- Invalid form submission
- Missing record
- Unauthorized access
- Database failure
- File upload failure
- Email failure
- Unexpected application error

Users should receive understandable messages rather than technical error details.

### User Story

**US-ERROR-01**

> As a user, I want understandable error messages when something goes wrong.

---

## 5.24 Logging

The system shall maintain application logs.

Logs may contain:

- Errors
- Warnings
- Authentication events
- Important system events
- Background job failures
- Database-related errors

Sensitive personal information shall not be unnecessarily written to logs.

### User Story

**US-LOG-01**

> As an administrator, I want application errors logged so that problems can be diagnosed.

---

## 5.25 Caching & Performance

The system should use appropriate performance mechanisms.

Potential areas:

- Dashboard queries
- Frequently accessed configuration
- Repeated statistics
- Expensive queries

The application shall avoid unnecessary database queries.

### Requirements

- Database indexes where appropriate
- Pagination for large datasets
- Efficient QuerySets
- Appropriate caching
- Optimized database queries

### User Story

**US-PERF-01**

> As a user, I want LifeOS to respond quickly when I navigate through my information.

---

## 5.26 Backup & Recovery

The system shall maintain backups of important application data.

Requirements:

- Scheduled database backups
- Backup retention policy
- Backup verification
- Recovery procedure
- Disaster recovery plan

### User Story

**US-BACKUP-01**

> As a user, I want my personal data protected against accidental loss.

---

## 5.27 Responsive Design

LifeOS shall support:

- Desktop
- Laptop
- Tablet
- Mobile browser

The application should remain usable on smaller screens.

### User Story

**US-UI-01**

> As a user, I want to use LifeOS from my phone without needing a separate mobile application.

# 6. Navigation Structure

The proposed primary navigation is:

- Dashboard
- Today
- Tasks
- Calendar
- Projects
- Goals
- Habits
- Routines
- Notes
- Documents
- Notifications
- Activity
- Settings

# 7. Core Data Relationships

Conceptually:

- A User owns Tasks.
- Tasks may belong to Projects and Goals.
- A User owns Projects.
- A User owns Goals.
- Goals may contain Projects, Tasks, and Milestones.
- A User owns Habits.
- A User owns Routines.
- A User owns Events.
- A User owns Notes.
- A User owns Documents.
- A User owns Notifications.
- A User owns Activity History.

# 8. Non-Functional Requirements

## 8.1 Security

The application must protect personal user information.

## 8.2 Performance

Normal pages should respond quickly under expected application load.

## 8.3 Availability

The production application should be available reliably with appropriate monitoring.

## 8.4 Scalability

The architecture should allow the application to grow from a small number of users to a substantially larger user base.

## 8.5 Maintainability

The application should use a clear modular architecture and consistent development standards.

## 8.6 Usability

Common actions should require minimal steps.

## 8.7 Accessibility

The UI should follow reasonable accessibility practices, including:

- Keyboard navigation
- Labels for form fields
- Appropriate contrast
- Semantic HTML
- Accessible error messages

## 8.8 Compatibility

The application should support current versions of major browsers.

# 9. Infrastructure Requirements

The production environment should support:

- Django application
- PostgreSQL database
- HTTPS
- Domain name
- Object/file storage where appropriate
- Email service
- Cache where appropriate
- Background task processing where appropriate
- CI/CD
- Monitoring
- Error tracking
- Database backups

# 10. Testing Requirements

The application shall be tested at multiple levels.

## Unit Tests

Test individual pieces of application logic.

Examples:

- Goal progress calculation
- Habit streak calculation
- Task status logic

## Integration Tests

Test interactions between components.

Examples:

- Creating a task
- Completing a task
- Creating a goal and associating tasks

## Authentication Tests

Test:

- Login
- Logout
- Registration
- Password reset
- Unauthorized access

## Authorization Tests

Test:

- A user cannot access another user's data.
- A user cannot modify another user's records.
- Administrator permissions work correctly.

## User Interface Tests

Test important user workflows.

# 11. Recommended MVP

The complete SRS is intentionally broad. The first usable version should contain:

- Authentication
- Dashboard
- Tasks
- Goals
- Projects
- Habits
- Notes
- Search
- Notifications
- Settings

Then add:

- Calendar
- Routines
- Documents
- Statistics
- Audit Logs
- Email
- Advanced infrastructure

# 12. Feature-to-Concept Map

| Area | LifeOS Features | Main Software Concepts |
|---|---|---|
| **Authentication** | Registration, login, logout, password reset | Authentication, sessions, forms, email |
| **Authorization** | Private data, ownership, admin access | Permissions, access control |
| **CRUD** | Tasks, goals, projects, habits, notes | Models, ORM, Forms, Views |
| **Search** | Search, filters, sorting, pagination | QuerySets, query parameters, database queries |
| **UI** | Dashboard, navigation, forms, tables | Templates, Bootstrap, template inheritance |
| **Communication** | Notifications, email, reminders | Email, background tasks, events |
| **Files** | Documents, receipts, attachments | File handling, storage, validation |
| **Business Logic** | Goals, streaks, progress, recurring tasks | Services, calculations, workflows |
| **Administration** | Users, settings, system management | Django Admin, permissions |
| **Audit** | Activity history | Audit trails, logging |
| **Security** | CSRF, XSS, authorization, secure sessions | Web security |
| **Performance** | Caching, indexes, optimized queries | PostgreSQL, caching, QuerySets |
| **Reliability** | Backups, recovery | Database operations, infrastructure |
| **Testing** | Unit, integration, authorization tests | Django testing, pytest |
| **Deployment** | Production hosting | Linux, web server, WSGI/ASGI |
| **DevOps** | Docker, CI/CD | Containers, GitHub Actions |
| **Monitoring** | Logs, errors, health | Observability |
| **Scalability** | Database optimization, caching | Architecture, PostgreSQL |

# 13. Definition of Done

LifeOS shall be considered production-ready when:

- Authentication works correctly.
- Users can only access their own data.
- Core CRUD operations work.
- Forms validate input.
- Search and filtering work.
- Dashboard displays accurate information.
- Goals calculate progress correctly.
- Habits calculate streaks correctly.
- Notifications work.
- Files are securely handled.
- Important actions are recorded.
- Errors are handled gracefully.
- Automated tests cover critical functionality.
- Database backups are configured.
- Security settings are configured.
- Application logging is configured.
- Performance has been reviewed.
- Production environment is configured.
- CI/CD is operational.
- Monitoring is operational.
- The application has been deployed successfully.

# 14. Overall System

LifeOS consists of the following major areas:

1. **Personal Management**
   - Goals
   - Habits
   - Notes

2. **Productivity**
   - Tasks
   - Projects
   - Calendar
   - Routines

3. **Organization**
   - Documents
   - Search
   - Tags
   - Categories

4. **Feedback**
   - Dashboard
   - Statistics
   - Notifications
   - Reminders
   - Activity history

5. **Account & Security**
   - Authentication
   - Authorization
   - Privacy
   - Settings

6. **Operations**
   - Logging
   - Backups
   - Monitoring
   - Performance
   - Deployment
   - CI/CD

The core product loop is:

**User → Plan → Act → Track → Review → Improve**

LifeOS should make that loop easy to perform repeatedly.
