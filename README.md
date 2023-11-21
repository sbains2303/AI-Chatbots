# ChatGPT enhanced webpage chatbots  

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Goals](#project-goals)
- [Documentation](#documentation)
- [License](#license)
- [Setup and Deployment](#setup-and-deployment)
- [Acknowledgements](#acknowledgements)
- [Initial Stakeholders](#initial-stakeholders)
- [User Stories](#user-stories)
- [Flow Steps](#flow-steps)
- [Team Members](#team-members)
- [Project Management](#project-management)

## Project Overview

The primary focus of this project is the development of an API-integrated chatbot, offering versatile capabilities that can be seamlessly integrated into any website. The chatbot serves as the main project component, designed to handle various user queries, including those related to recipes. Additionally, the Recipes website serves as a showcase, highlighting the chatbot's functionalities and its potential integration into different platforms.

## Features

- Recipe Repository: Collection of diverse and popular dish recipes
- Chatbot Interaction: Users can query the chatbot for recipes, ingredient alternatives, and upload their own recipe documents (PDF, docx, xlsx, txt etc)
- Meal Plans & Shopping Lists: Facility to create and manage meal plans and shopping lists
- Digital Receipts: Users can save and manage digital receipts
- Content Summarization: Ability to summarize lengthy recipes
- Versatile Querying: Supports varied user queries about recipes and ingredients
- Chatbot Integration Use Case: Serves as an exemplary use case for the chatbot technology and offfers flexible integration for websites to enable various user interactions and queries

## Project Goals

- Enable easy access to and creation of recipe content
- Allow users to upload various document types for recipes, meal plans, etc
- Develop a user-friendly interface for recipe browsing and interaction
- Seamlessly integrate a chatbot for recipe-related queries
- Develop a versatile and easily integrable chatbot API for websites
- Highlight the chatbot's adaptability for diverse user queries and website integration

## Documentation

For detailed documentation and usage instructions, refer to the Wiki.

## License

This project is licensed under MIT - see the [LICENSE](https://github.com/spe-uob/2023-Chatbots/blob/main/LICENSE) file for details.

## Setup and Deployment

### Prerequisites 
Clone our GitHub repository: https://github.com/spe-uob/2023-Chatbots.git

**Downloads**: 
- Python https://www.python.org/downloads/release/python-3120/
- Flask: 
  - via command lines in terminal, pip install flask
- SQL Alchemy: 
  - `pip install sqlalchemy`
  - Arch: `Pacman -S python-sqlalchemy`
- OpenAI
- Recommended IDE:
  - JetBrains PyCharm

### Usage

To run the flask server locally:
- navigate to `code/website`
- run: `flask run`


## Acknowledgements

**Front End**: Utilizes HTML, CSS, and JavaScript for website development

**Back End**: Powered by Python with Flask, facilitating web development, Jinja2 template integration, and interaction with SQL databases

**AWS Server**: Cost-effective and flexible server hosting solution

**ChatGPT API Integration**: Each website has its unique ChatGPT API key to avoid issues with running costs and provide distinct models for each site

**SQL Database (MariaDB)**: Familiar and scalable database solution, implemented through Amazon RDS, simplifying database management tasks

## Initial Stakeholders

1. Web developers
2. Webapp service providers
3. Users of websites
4. Our client
5. Legislators
6. General public
7. OpenAI

## User Stories

As a web developer, I want to integrate the chatbot so that the users of my website can quickly access information relating to the website’s content/helpful information. This allows users can find answers to their questions without navigating through the site extensively.

As a webapp service provider, I want to have the ability to replicate the chatbot so that I can offer it as a service. This will allow me to provide chatbot functionality to multiple clients and generate a new revenue stream.

As a website user, I want to ask questions so that I can better understand the website’s content/easily navigate the website. So that I can quickly grasp the main features and purpose of the website without searching through pages.

As a website user, I want to ask questions so that I can get filtered answers which is accuracy and helpful. This ensures that I receive precise and relevant information that enhances my experience.

As a website user, I want to upload my own files so that I can get the information which I want from the files to save time. This feature allows me to extract specific data or insights from files without manual searching.

As a content creator, I want the chatbot to assist me in generating ideas and content topics so that I can improve my productivity and creativity. This will help me brainstorm fresh and engaging content ideas, which is essential for maintaining a captivating online presence and retaining an audience.

As a website administrator, I want the chatbot to monitor user interactions and provide feedback so that I can continuously enhance the user experience. By analyzing user interactions and feedback, I can identify areas of improvement, fix issues promptly, and ensure a more user-friendly and satisfying website.

As a sales representative, I want the chatbot to provide product recommendations based on user preferences so that I can increase sales and customer satisfaction. By leveraging user preferences and the chatbot's capabilities, I can offer tailored product suggestions that enhance the shopping experience, boost sales, and satisfy customers.


## Flow Steps

1.  Input Acceptance: Receive input string, identifying the calling website to select the appropriate model and processing
2.  Pre-processing: Includes discarding irrelevant queries, document parsing, and database checks
3.  ChatGPT Processing: Utilizes LangChain to communicate with ChatGPT for text processing (skipped if input is rejected)
4.  Post-processing: Involves updating the database with the obtained information
5.  Output Delivery: Return processed string to the API caller (the respective website)

## Team members

| Members          | Email                                                 |
| ---------------- | ----------------------------------------------------- |
|Emir Abou Zaki    | [jk22756@bristol.ac.uk](mailto:jk22756@bristol.ac.uk) |
|Lifan Lei         | [kg21776@bristol.ac.uk](mailto:kg21776@bristol.ac.uk) |
|Seb Whipps        | [nk22674@bristol.ac.uk](mailto:nk22674@bristol.ac.uk) |  
|Saihajpreet Bains | [ia22870@bristol.ac.uk](mailto:ia22870@bristol.ac.uk) |    
|Hankang Wu        | [fq22652@bristol.ac.uk](mailto:fq22652@bristol.ac.uk) |  


## Project Management
[Kanban Board](https://github.com/orgs/spe-uob/projects/86)

[Gantt Chart](https://github.com/orgs/spe-uob/projects/86/views/3)

