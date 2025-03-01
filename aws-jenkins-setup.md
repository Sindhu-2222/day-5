Setting Up Jenkins on AWS
Prerequisites
AWS account with necessary permissions to create and manage EC2 instances.
Basic knowledge of AWS, SSH, and Jenkins.
Steps:
1. Open AWS Management Console and Navigate to the EC2 Dashboard
Open a web browser and go to the AWS Management Console.
Log in with your AWS credentials.
In the AWS Management Console, search for "EC2" in the search bar and select "EC2 - Virtual Servers in the Cloud" to open the EC2 Dashboard.
2. Launch a New EC2 Instance with Ubuntu AMI
In the EC2 Dashboard, click on the "Launch Instance" button.
In the "Choose an Amazon Machine Image (AMI)" step, select the following:
Ubuntu Server 20.04 LTS (HVM), SSD Volume Type (or the latest available version).
3. Select an Instance Type
In the "Choose an Instance Type" step, select an instance type based on your requirements. For Jenkins, a t2.medium instance type is recommended.
Click "Next: Configure Instance Details".
4. Configure Instance Details
In the "Configure Instance Details" step, you can keep the default settings or modify them based on your requirements (e.g., Network, Subnet).
Click "Next: Add Storage".
5. Add Storage
In the "Add Storage" step, you can modify the storage settings if needed. The default settings are usually sufficient.
Click "Next: Add Tags".
6. Add Tags (Optional)
In the "Add Tags" step, you can add tags to help you identify your instance (e.g., Key: Name, Value: Jenkins).
Click "Next: Configure Security Group".
7. Configure Security Group
In the "Configure Security Group" step, select "Create a new security group".

Add the following rules to allow SSH and HTTP access to your instance:

Type: SSH
Protocol: TCP
Port Range: 22
Source: Your IP (or custom IP range)
Type: Custom TCP Rule
Protocol: TCP
Port Range: 8080
Source: Anywhere (0.0.0.0/0) or a specific IP range for security purposes.
Click "Review and Launch".

8. Launch the Instance and Download the Key Pair for SSH Access
Review the instance configuration and click on the "Launch" button.
In the popup window, select "Create a new key pair", enter a name for the key pair, and click "Download Key Pair".
Make sure to store the key pair file (.pem) securely, as you will need it to connect to your instance.
9. SSH into the Instance
Open your terminal or command prompt.
Change to the directory where you saved the key pair file.
Set the appropriate permissions for the key pair file:
sh
Copy Code


chmod 400 your-key-pair.pem
Use the following command to connect to your instance:
sh
Copy Code


ssh -i your-key-pair.pem ubuntu@your-ec2-public-dns-address
Replace your-key-pair.pem with the name of your key pair file and your-ec2-public-dns-address with your instance's public DNS address.
10. Install Java and Jenkins
Update the package list:
sh
Copy Code


sudo apt update
Install Java (Jenkins requires Java):
sh
Copy Code


sudo apt install openjdk-11-jdk -y
Add Jenkins repository and import GPG keys:
sh
Copy Code


wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
Install Jenkins:
sh
Copy Code


sudo apt update
sudo apt install jenkins -y
11. Start Jenkins and Set Up Initial Configuration in the Web Interface
Start the Jenkins service:
sh
Copy Code


sudo systemctl start jenkins
Enable Jenkins to start on boot:
sh
Copy Code


sudo systemctl enable jenkins
Open a web browser and navigate to:
sh
Copy Code


http://your-ec2-public-dns-address:8080
Retrieve the initial Jenkins admin password from the server:
sh
Copy Code


sudo cat /var/lib/jenkins/secrets/initialAdminPassword
Copy the password and paste it into the Jenkins web interface to unlock Jenkins.

Follow the setup wizard to complete the initial configuration, install suggested plugins, and create an admin user.
This documentation provides a detailed step-by-step guide to setting up Jenkins on an AWS EC2 instance. Follow these instructions to deploy Jenkins and prepare it for your continuous integration and continuous deployment (CI/CD) pipeline.



