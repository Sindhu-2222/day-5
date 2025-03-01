Setting Up Jenkins on Google Cloud Platform (GCP)
Documented Steps
Prerequisites
A Google Cloud Platform (GCP) account with the necessary permissions to create and manage Compute Engine instances.
Basic knowledge of GCP, SSH, and Jenkins.
Steps:
1. Open the Google Cloud Console and Navigate to Compute Engine
Open a web browser and navigate to the Google Cloud Console.
Log in with your Google Cloud credentials.
In the Google Cloud Console, click on the menu icon (☰) in the top-left corner.
Navigate to "Compute Engine" and click on "VM instances."
2. Create a New VM Instance with Ubuntu
Click the "Create Instance" button at the top of the VM instances page.

Provide the necessary details for your VM instance:

For Name and Region:

Name: Enter a name for your VM (e.g., jenkins-vm).
Region: Select a region close to your location or application requirements.
Zone: Select a zone within the chosen region.
For Machine Type:

Series: Choose the appropriate series (e.g., N1).
Machine type: Select a machine type suitable for Jenkins. A basic recommendation is n1-standard-1 or n1-standard-2.
For Boot Disk:

Click on "Management, security, disks, networking, sole tenancy" to expand the additional options.
Under the "Boot disk" section, click on "Change."
In the "Choose an operating system" dropdown, select "Ubuntu."
In the "Version" dropdown, select "Ubuntu 20.04 LTS" (or the latest available version).
Click "Select."
3. Configure VM Sizes, Disk, and Network Settings
For Boot Disk:

The boot disk should already be configured in the previous step.
For Firewall:

In the "Firewall" section, check the boxes for "Allow HTTP traffic" and "Allow HTTPS traffic."
4. Allow SSH (Port 22) and HTTP (Port 8080) Traffic
By default, SSH (port 22) traffic is allowed for all GCP VMs.
To allow HTTP (port 8080) traffic:
Add a firewall rule to allow ingress traffic on port 8080.
Navigate to the "VPC network" section in the Google Cloud Console.
Click on "Firewall rules" and then "Create firewall rule."
Provide a name for the rule (e.g., allow-jenkins-8080).
Set the "Targets" to "All instances in the network."
Set the "Source IP ranges" to 0.0.0.0/0.
Set the "Protocols and ports" to "Specified protocols and ports" and add tcp:8080.
Click "Create."
5. Connect to the VM Using SSH
In the Compute Engine VM instances page, find your newly created VM.
Click on the "SSH" button next to your VM instance to open an SSH connection directly in the browser, or use the provided command to connect via your terminal:
Open your terminal.
Use the command from the GCP console to connect to your VM:
sh
Copy Code


gcloud compute ssh your-username@instance-name --zone=your-zone
Replace your-username, instance-name, and your-zone with the appropriate values.
6. Install Java and Jenkins
Update the package list:

Update the list of available packages to their latest versions.
Install Java:

Install OpenJDK (Jenkins requires a supported version of Java).
Add Jenkins repository and import GPG keys:

Add Jenkins repository to the package manager.
Import Jenkins GPG keys to authorize the packages.
Install Jenkins:

Install Jenkins using the package manager.
7. Start Jenkins and Complete the Initial Setup
Start Jenkins service:

Start Jenkins and enable it to start on boot using system commands.
Open Jenkins in a Web Browser:

Navigate to http://<your-vm-ip>:8080 in your web browser.
Retrieve Initial Admin Password:

Obtain the initial admin password from the appropriate Jenkins directory using system commands.
Complete Setup Wizard:

Use the admin password to unlock Jenkins.
Follow the setup wizard to install suggested plugins and create your admin user account.
These documented steps provide a thorough guide for setting up Jenkins on a GCP VM, ensuring smooth installation and initial configuration of Jenkins to support your continuous integration and continuous delivery (CI/CD) pipeline needs. This optimized approach is designed to handle typical competitive programming scenarios and real-world requirements effectively.