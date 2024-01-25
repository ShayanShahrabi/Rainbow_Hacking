# Rainbow Hash
> The main idea of the project comes from the **Python Programming for Beginners ** course, then, after about a year I thought it would be a good idea to add some more stuff to it and share it on my github :)
## What's rainbow hash?
Rainbow hash refers to a technique used in cryptography and password cracking. It is a time-memory trade-off method that optimizes the process of reversing hashed values back to their original input, usually passwords.

When passwords are stored in a database or transmitted over a network, they are often hashed, which means they are transformed into a fixed-length string of characters using a mathematical algorithm. Hashing is a one-way process, meaning it is computationally difficult to retrieve the original password from its hash.

However, attackers can employ rainbow tables to crack hashed passwords. A rainbow table is a precomputed table containing a large number of potential passwords and their corresponding hash values. These tables are generated in advance, saving time during the cracking process.

Rainbow hash reduces the storage requirements of rainbow tables by using a technique called "reduction functions." These functions map hash values back to potential passwords, significantly reducing the size of the table. By applying these functions iteratively, the rainbow table can cover a larger password space.

In summary, rainbow hash is a method used to optimize password cracking by precomputing and storing a reduced set of potential passwords and their corresponding hash values, making it faster to reverse hashed passwords.

## How to run the code?
Open the `main.ipynb` file and run the cells. There is information provided on the steps.