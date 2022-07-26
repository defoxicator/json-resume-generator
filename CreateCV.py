# JSON CV Builder

from click import edit


def main():
    import json

    # data dictionaries  
    
    basics_dict = {
        "name": "Full name: ",
        "label": "Desired position: ",
        "image": "URL to your picture: ",
        "email": "E-mail address: ",
        "phone": "Phone number: ",
        "url": "URL to your website: ",
        "summary": "Description: ",
    }
    
    location_dict = {
        "address": "Address: ",
        "postalCode": "Postal code: ",
        "city": "City: ",
        "countryCode": "Country: ",
        "region": "Region: "
    }
 
    profile_dict = {
        "network": "Social network: ",
        "username": "Username: ",
        "url": "URL: "
    } 

    work_dict = {
        "company": "Company: ",
        "url": "Company's website: ",
        "position": "Position: ",
        "startDate": "Start: ",
        "endDate": "End: ",
        "summary": "Description: ",
        "hightlights": "Highlights: ",
    }

    education_dict = {
        "institution": "Institution: ",
        "url": "institution's website: ",
        "area": "Subject: ",
        "studyType": "Study type: ",
        "startDate": "Start: ",
        "endDate": "End: ",
        "score": "GPA: ",
        "courses": "Relevant courses: ",
    }

    skills_dict = {
        "name": "Category/Name: ",
        "level": "Level: ",
        "keywords": "Keywords: "
    }

    languages_dict = {
        "language": "Language: ",
        "fluency": "Fluency: "
    }

    interests_dict = {
        "name": "Name: ",
        "keywords": "Keywords: "
    }
    
    projects_dict = {
      "name": "Name: ",
      "description": "Description: ",
      "highlights": "Highlights: ",
      "keywords": "Keywords: ",
      "entity": "Entity: ",
      "type": "Type of project: "
    }

    # keywords and highlights

    # data lists

    work_list = []
    education_list = []
    skills_list = []
    languages_list = []
    interests_list = []
    projects_list = []

    # resume template

    # resume = {"basics": basics,
    #     "work": work_list,
    #     "education": education_list,
    #     "skills": skills_list,
    #     "languages": languages_list,
    #     "interests": interests_list,
    #     "projects": projects_list,
    # }
    

    def more_entries(category = None):
        if category == None:
            agree = input("Do you want to add another entry? (y/n) ")
        else:
            agree = input(f"Do you have anything to add to {category}? (y/n) ")

        if agree.lower() == "y" or agree.lower() == "yes":
            return True
        else:
            return False

    def listed_content(name, category):
        list_cont = []

        if more_entries(name) == True:
            list_cont.append(str(input(f'Input one of your {name}: ')))
        
            while more_entries() == True:
                list_cont.append(str(input(f'Input one of your {name}: ')))

        category.update({name: list_cont})

    ### CATEGORY UPDATE?!
    
    def single_section(list):
        template_copy = template.copy()

        for k, v in template_copy.items():
            template_copy[k] = str(input(template[k]))
            
        list.append(template_copy)

    def section(category, names):
        if more_entries(category) == True:
            list = []
            single_section(list)
            for name in names:
                listed_content(category, name)
            
            while more_entries() == True:
                single_section(list)

            if category == "profiles":
                basics.update({"profiles": list})
                resume.update({"basics": basics})
            else:
                resume.update({category: list})

    print("""
    Welcome to CV Builder.
    """)

    templates = [basics_dict, location_dict, profile_dict, work_dict, education_dict, skills_dict, languages_dict, interests_dict, projects_dict]
    
    resume = {}
    basics = {}

    for template in templates:

        if template == basics_dict:
            template_copy = template.copy()

            for k, v in template_copy.items():
                template_copy[k] = str(input(template[k]))
                basics.update(template_copy)

        if template == location_dict:
            template_copy = template.copy()

            for k, v in template_copy.items():
                template_copy[k] = str(input(template[k]))
                basics.update({"location": template_copy})
        
        if template == profile_dict:
            section("profiles")

        if template == work_dict:
            section("work")

    print(resume)

if __name__ == "__main__":
    main()