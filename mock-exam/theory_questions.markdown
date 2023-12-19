## Theory Questions 31 marks

#### What does SDLC stand for?
- SDLC stands for Software Development Life Cycle, which is a process used to design, develop, and test high-quality software.

#### What exception thrown when you divide a number by 0?
- In python, attempting to divide by zero will throw a ZeroDivisionEror. 

#### What is the git command that moves code from the local repository to the remote repository?
- The git command that moves code from the local repositoryd to the remote repository is git push. 

#### What does NULL represent in a database?
- In database, NULL represents the absence of a value or that it is unknown. NULL indicates that no value has been assigned to the field in the database record.

#### Name 2 responsibilities of the Scrum Master

1.  One of the responsibilities of a scrum master is to facilitate Scrum ceremonies which includes: daily stand-ups, sprint planning, sprint review, and sprint retrospective. 

2. Another responsibilities of a Srum master is identifying and removing obstacles that are obstructing the teams progress towards the end of the sprint goals. This could be andything from personal issues to technical debt or organisation red tape. 

#### Name 2 debugging methods, and when you would use them. 4marks

Debugging method is a way to identify, and fix bugs in software. Debugging helps developers to understand the cause of a problem in their code, and whats the best approach to fixicng it. 

1. one of the methods is code reviews - this involves going through your code to identify potential issues. This is more effective with a colleague. Code reviews are aparticularly useful for catching logical erros, understanding complaex code etc. 

2. Another debugging method is breakpoints. This method is putting logic somehwere to stop the code at a certain point. 

- You'll stop the operation of your program at a specific point to check the state of it  , including variable values, the call stack, and program flow.
In essence: You set breakpoints at lines in the code where you want the debugger to pause execution. When the program is run in debugging mode, it stops at these breakpoints, allowing for inspection and interaction.

#### Looking at the code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you'll need. (5marks)


- In the provided function, the issue is the lack of input validation. The function assumes that the inputs will be numbers without verifying. In particular its expecting numerical inputs for 'price' and 'cash_given'. In this case, the comparison operator >= will throw a TypeEror because it's not possible to compare a string with an integer. 

- To rectify this: we could include a try-except 

def can_pay(price, cash_given):
    try:
        if cash_given >= price:
            return True
        else:
            return False
    except TypeError:
        print("Input values must be numbers.")
        return False

- While not an error, if negative values are passed for price or cash_given, the function might return unexpected results as it doesn't handle these cases explicitly.

- To handle these potential issues, you could add exception handling to check the input types and values:

def can_pay(price, cash_given):
    try:
        if not (isinstance(price, (int, float)) and isinstance(cash_given, (int, float))):
            raise ValueError("Both price and cash_given must be numbers.")
        if price < 0 or cash_given < 0:
            raise ValueError("Neither price nor cash_given can be negative.")
        return cash_given >= price
    except ValueError as e:
        print(e)
        return False


#### What is git branching? Explain how it is used in Git. (6marks)

- In Git, branching is a key notion. It lets developers make their own side project that's separate from the main work. This is super handy for adding new features or sorting out bugs because you can make changes without messing up the main codebase.

**What is it used for?**
- Git branches are used for isolating development work. For example, when developing a new feature, a developer would create a new branch and make their changes there. This keeps the new changes separate from the main code until they're ready to be merged back in.

**Why should you use it?**
- Using branches makes it easier to manage complex development processes. It allows multiple developers to work on different features simultaneously without interfering with each other's work. It also makes it easier to track changes and roll back to previous versions if something goes wrong.

**When should you use it?**
- You should use branches whenever you're working on a new feature, fixing a bug, or generally whenever you're making changes that you want to keep separate from the main code. It's also common to use branches when you're experimenting with new ideas that you're not sure will work.

**What makes a good Git branch?**
- A good Git branch is short-lived and focused on a single task. It should be named descriptively so that others can understand what work is being done on that branch. It's also important to regularly pull in changes from the main branch/project to keep your branch up-to-date and avoid merge conflicts.

- once the work on the branch is complete and has been tested, it should be merged back into the main branch and then deleted to keep the repository clean and manageable.

#### Design a restaurant ordering system.
You do not need to write code, but describe a high-level approach: a. Draw a list of key requirements
b. What are your main considerations and problems?
c. What components or tools would you potentially use?

- Designing a restaurant ordering system is a complex process that blends technology with the practical needs of a restaurant's operation. It's about creating a system that's easy for customers to use, helps staff manage orders efficiently, and streamlines the kitchen's workflow. Here's what the process is like:

### Here are the Key Requirements:

1. User Interface (UI) for Customers:
   - A menu display with categories, items, descriptions, and prices.
   - Ability to add items to an order with customisations (e.g., no sauce, extra bacon).
   - Order summary with itemised costs, taxes, and total amount.
   - Options for dine-in, takeaway, or delivery.
   - Payment processing (credit card, digital wallet, Apple/Google pay cash on delivery).

2. UI for Staff:
   - Display of orders.
   - Order management with status updates (received, in preparation, ready for serving/delivery).
   - Inventory management to track ingredients and supplies.
   - Payment and sales tracking.

3. Backend System:
   - Database to store menu items, prices, orders, and customer information.
   - Integration with payment gateways.
   - Security to protect customer data and payment transactions.

4. Notification System:
   - Real-time updates to customers on order status.
   - Alerts for staff for new orders or cancellations.

5. Reporting and Analytics:
   - Sales reports, popular items, peak times.
   - Customer feedback and ratings system.

### Some of the Main Considerations and Problems

- Usability: The system must be user-friendly for both customers and staff.
- Performance: The system should handle high volumes of - orders during peak hours.

-Scalability: It should be able to grow with the restaurant, adding more menu items or integrating with other systems.
- Reliability: The system should be reliable with minimal downtime.
- Security: Sensitive data, especially payment information, needs to be securely handled.
- Integration: The system might need to integrate with existing Point of Sale (POS) systems or delivery platforms.

### Components or Tools Potentially Used

Frontend: HTML/CSS/JavaScript frameworks (React, Angular,) for building the user interfaces.
Backend: A server-side language (Node.js, Python) and a framework (Express.js, Django).
-Database: A relational database (PostgreSQL, MySQL) or NoSQL database (MongoDB) for storing data.
- Payment Gateway: Services like Dojo, Stripe, PayPal for handling payments.
- Hosting/Cloud Services: AWS, Google Cloud, or Azure to host the application and manage the infrastructure.
- Containerization: Docker for containerising the application, Kubernetes for orchestration if scaling is necessary.
- Version Control: Git for source code management.
- CI/CD Tools: CI/CD for continuous integration and deployment.

